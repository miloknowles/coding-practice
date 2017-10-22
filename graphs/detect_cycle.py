"""
Detect a cycle in a directed graph.

Idea: recursively visit nodes and keep track of whether they are
unvisited, in progress (descendants being explored), or complete (all descendents visited)
"""

import sys
sys.setrecursionlimit(10000)

class Graph(object):
	def __init__(self):
		self.vertices = {}

	def add_vertex(self, v):
		self.vertices[v] = {}

	def add_edge(self, u, v, weight=1, directed=True):
		if u not in self.vertices:
			self.add_vertex(u)
		if v not in self.vertices:
			self.add_vertex(v)

		self.vertices[u][v] = weight
		if not directed: self.vertices[v][u] = weight

	def get_adjacent(self, v):
		if v in self.vertices:
			return self.vertices[v].keys()
		else:
			return None

	def get_vertices(self):
		return self.vertices.keys()

def detect_cycles(graph):
	unvisited = set(graph.get_vertices())
	inprogress = set()
	complete = set()

	def visit(v):
		if v in complete:
			return False
		elif v in inprogress:
			return True # Ran into a node that is on the current recursion stack.
		else:
			descendents = graph.get_adjacent(v)
			if v in unvisited: unvisited.remove(v)
			inprogress.add(v)
			for d in descendents:
				has_cycle = visit(d)
				if has_cycle: return True

			# All descendents recursed on without finding cycle.
			inprogress.remove(v)
			complete.add(v)
			return False

	while len(unvisited):
		node = unvisited.pop()
		has_cycle = visit(node)
		if has_cycle: return True
	return False

# Example with a cycle
print 'Example: has cycle'
g = Graph()
[g.add_vertex(i) for i in range(6)]
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

result = detect_cycles(g)
print 'Result:', result

# Example without a cycle
print 'Example: has no cycle'
g = Graph()
[g.add_vertex(i) for i in range(1000)]
for ii in range(999):
	g.add_edge(ii, ii+1)
result = detect_cycles(g)
print 'Result:', result