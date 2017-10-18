""" Dijkstra's algorithm for shortest path on general graph

Dijkstra's only works with nonnegative weights.

Bellman ford works for the general case.

BFS works for shortest paths when weights are uniform (or small integers)

""" 

import heapq
import random

class Vertex(object):
	def __init__(self, name, data):
		self.name = name
		self.data = data
		self.adjacent = {}

	def add_adjacent(self, other, weight):
		self.adjacent[other] = weight

class Graph(object):
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, name, data=None):
		self.vertices[name] = Vertex(name, data)

	def add_edge(self, u, v, weight, directed=False):
		if not u in self.vertices:
			self.add_vertex(u)
		if not v in self.vertices:
			self.add_vertex(v)

		self.vertices[u].add_adjacent(v, weight)

		if not directed:
			self.vertices[v].add_adjacent(u, weight)

	def print_graph(self):
		print "Vertices:"
		for v in self.vertices.keys():
			print v, '->', self.vertices[v].adjacent

	def get_vertex(self, v):
		if v in self.vertices:
			return self.vertices[v]
		else:
			return None

class PriorityQueue(object):
	def __init__(self, items=None):
		if items == None:
			self.queue = []
		else:
			self.queue = heapq.heapify(items)

	def push(self, item):
		heapq.heappush(self.queue, item)

	def extract_min(self):
		if len(self.queue) > 0:
			return heapq.heappop(self.queue)
		else:
			return None

	@property
	def empty(self):
		return len(self.queue) == 0

def dijkstra_shortest_path(graph, start, goal=None):
	"""
	Runs Dijkstra's single source shortest path algorithm on a graph.
	start: the name of the start vertex
	goal: (optional) the name of the goal node. If given, the search
	will terminate early when the goal node is found.
	"""
	distances = {} # Maintain distance of every vertex from start.
	parents = {}
	Queue = PriorityQueue()

	# Initialize all distances to infinite distance (except start)
	distances[start] = 0
	parents[start] = None
	for v in graph.vertices.keys():
		if v != start:
			distances[v] = float('inf')
	Queue.push((distances[start], start))

	finished = False
	while (not Queue.empty and not finished):
		dist, node_name = Queue.extract_min()
		node = graph.get_vertex(node_name)

		# Improve distance of neighboring nodes.
		for adj_name in node.adjacent.keys():
			# adj = graph.get_vertex(adj_name)
			weight = node.adjacent[adj_name]
			if (dist + weight) < distances[adj_name]:
				# If relaxation can be made, update distances and parent pointers.
				distances[adj_name] = dist + weight
				parents[adj_name] = node.name
				# Early stopping condition.
				if (adj_name == goal): finished = True
			Queue.push((distances[adj_name], adj_name))

	return distances, parents

def construct_path(start, goal, parents):
	""" Trace parent pointers to reconstruct a path. """
	node = goal
	path = []
	while (node in parents):
		path.append(node)
		if node == start: break
		node = parents[node]

	if path[-1] == start:
		path.reverse()
		return path
	else:
		return None


G = Graph()
for i in range(10):
	G.add_vertex(i)

for i in range(10):
	for j in range(10):
		G.add_edge(i, j, random.randint(0, 10))

G.print_graph()

dist, par = dijkstra_shortest_path(G, 1, goal=6)
path = construct_path(1, 6, par)
print path

