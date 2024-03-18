import numpy as np
from dataclasses import dataclass, field
from heapq import heappush, heappop


@dataclass
class ShortestPath:
  path: list[int]
  distance: int | float


@dataclass(order=True)
class PNode:
  priority: int | float
  id: any = field(compare=False)


def dijkstra_shortest_path(W: np.ndarray, source: int, target: int) -> ShortestPath:
  """Uses Dijkstra's Algorithm to compute a shortest path from `source` to `target`."""
  frontier = [PNode(0, source)]
  parents = {}
  distances = {u: float('inf') for u in range(len(W)) if u != source}
  distances[source] = 0
  visited = set()

  while len(frontier) > 0:
    # Get the lowest-cost frontier node and expand it.
    node_u = heappop(frontier)
    u = node_u.id

    # Because we push redundant nodes to the priority queue, we need to check
    # if they've already been visited here.
    if u in visited:
      continue

    visited.add(u)

    # Terminate when we've reached the goal node.
    if u == target:
      break

    neighbors = W[u].nonzero()[0]

    for v in neighbors:
      # Don't need to expand neighbors that have already been visited.
      if v in visited:
        continue

      # See if we can improve the distance from source to v by going through u.
      if (distances[u] + W[u, v]) < distances[v]:
        distances[v] = distances[u] + W[u, v]
        parents[v] = u

        # Since heapq doesn't support a `decrease-key` like operation, we simply
        # push the node with updated weight to the priority queue. The updated
        # node will be expanded before the stale one, and then the stale one
        # will be skipped later on as a duplicate.
        heappush(frontier, PNode(distances[v], v))

  # Failure if we never expanded the goal node.
  if target not in parents:
    return ShortestPath(path=[], distance=-1)

  # Retrace the optimal path using parent pointers.
  path = ShortestPath(path=[target], distance=0)

  v = target
  while v != source:
    path.distance += W[parents[v], v]
    v = parents[v]
    path.path.append(v)

  path.path.reverse()

  return path


if __name__ == "__main__":
  num_vertices = 6

  # Stores edge weights for edge (u, v)
  W = np.zeros((num_vertices, num_vertices))

  W[0, 1] = 1
  W[0, 2] = 1
  W[1, 3] = 1
  W[2, 3] = 2
  W[0, 3] = 3
  W[3, 4] = 1
  W[4, 5] = 1
  W[3, 5] = 1

  # Solution should be: 0, 1, 3, 5 with total distance 3
  solution = dijkstra_shortest_path(W, 0, 5)
  print(solution)