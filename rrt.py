from __future__ import division
from matplotlib import pyplot as plt
import numpy as np
import yaml
from shapely.geometry import Point, Polygon, LineString, box
from environment import Environment, plot_environment, plot_line, plot_poly
import math
import time

def envCheckContains(env, pt):
    """
    Checks whether 'pt' is contained in any of the obstacles in 'env'.
    env: (Environment instance) with some obstacles
    pt: (Point instance) i.e Point((3.5,1))
    """
    for i, obs in enumerate(env.obstacles):
        if obs.contains(pt):
            return True
    return False

def envCheckIntersects(env, line):
    """
    Checks whether 'line' intersects any of the obstacles in 'env'.
    env: (Environment instance) with some obstacles
    line: (Line instance) i.e LineString([start, end]).buffer(0.5, resolution=4)
    """
    for i, obs in enumerate(env.obstacles):
        if line.intersects(obs):
            return True
    return False

def findNearest(V, pt):
    smallest = float('inf')
    best = V[0]
    for v in V:
        dist = (pt[0] - v[0])**2 + (pt[1] - v[1])**2
        if dist < smallest:
            smallest = dist
            best = v
    return (best, math.sqrt(smallest))

def getPathLength(path):
    total = 0
    for i in range(1, len(path)):
        total += math.sqrt((path[i][0]-path[i-1][0])**2 + (path[i][1]-path[i-1][1])**2)
    return total


def plot_rrt(env, bounds, path, vertices, parents, radius, start_pose, end_region, time):
    ax = plot_environment(env, bounds=bounds)
    plot_poly(ax, Point(start_pose).buffer(radius, resolution=3), 'magenta')
    plot_poly(ax, end_region, 'brown', alpha=0.2)

    # plot the full tree
    for v in vertices:
        if v in parents:
            x, y = LineString([parents[v], v]).xy
            ax.plot(x, y, color='blue', linewidth=1, solid_capstyle='round', zorder=1)

    # plot the final path
    for i in range(1, len(path)):
        x, y = LineString([path[i-1], path[i]]).xy
        ax.plot(x, y, color='green', linewidth=3, solid_capstyle='round', zorder=1)
        
    # tree nodes, time, num obs, path length (nodes)
    pathLength = getPathLength(path)
    plt.title('Nodes: %d Time: %.3f sec Obstacles: %d Path Length: %.3f (%d nodes)' % (len(vertices), time, len(env.obstacles), pathLength, len(path)))
    plt.show()

def debug_plot(env, bounds, vertices, parents, start_pose, end_region):
    ax = plot_environment(env, bounds=bounds)
    plot_poly(ax, Point(start_pose).buffer(radius, resolution=3),'magenta')
    plot_poly(ax, end_region,'brown', alpha=0.2)

    for v in vertices:
        if v in parents:
            plot_line(ax, LineString([parents[v], v]))
    plt.show()

def rrt(bounds, environment, start_pose, radius, end_region):
    time0 = time.time()
    deltaX = bounds[2] - bounds[0]
    deltaY = bounds[3] - bounds[1]
    
    goalReached = False
    iters = 0
    maxIters = 100000
    maxDist = 0.2
    
    V = [start_pose]
    parents = {}
    lastPt = start_pose
    
    while (not goalReached and iters < maxIters):
        # Randomly sample the goal every 20 iters
        if iters % 20 == 0:
            sampleXY = end_region.representative_point().coords[0]
        else:
            sampleXY = np.random.rand(2) * [deltaX, deltaY] + [bounds[0], bounds[1]] # sample inside bounds
        
        # Check if point is inside an obstacle
        if not envCheckContains(environment, Point(sampleXY).buffer(radius, resolution=3)):
            parent, dist = findNearest(V, sampleXY) 
            
            if dist < maxDist:
                newPt = tuple(sampleXY)
            else: # Scale the new point so that it doesnt exceed certain length
                newPt = tuple([parent[0], parent[1]] + np.dot(maxDist/dist, [sampleXY[0]-parent[0], sampleXY[1]-parent[1]]))
            
            # Check that thick line from parent to newPt is legal
            line = LineString([parent, newPt]).buffer(radius, resolution=3)
            if not envCheckIntersects(environment, line):
                parents[newPt] = parent
                V.append(newPt)
                lastPt = newPt
                
                # Check if goal
                if end_region.contains(Point(newPt)):
                    goalReached = True

            iters += 1

    # debug_plot(environment, bounds, V, parents, start_pose, end_region)
    # Trace parent ptrs back through the path, then reverse
    path = []
    current = lastPt
    while (current != start_pose):
        path.append(current)
        current = parents[current]
    path.append(start_pose)
    path.reverse()
    
    # Call plotting function
    plot_rrt(environment, bounds, path, V, parents, radius, start_pose, end_region, time.time()-time0)
    return path

if __name__ == '__main__':
    environment = Environment('simple.yaml')
    radius = 0.3
    bounds = (-2, -3, 12, 8)
    start = (0, 0)
    goal_region = Polygon([(10,5), (10,6), (11,6), (11,5)])
    path = rrt(bounds, environment, start, radius, goal_region)