""" Given a directed graph (possibly disconnected), find a topological sort on the graph. """
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

def topological_sort(graph):
	"""
	Return a topological sort of a graph if it is a DAG,
	otherwise return None if one does not exist.
	"""
	sort = []

	complete = set()
	inprogress = set()
	unvisited = set(graph.get_vertices())

	def visit(v):
		""" Recursively performs DFS on a node and detects cycles
		if they occur.
		"""
		# print 'Visiting:', v
		if v in complete: # Hit a node whose dependencies are already satisfied.
			# print 'Hit complete node'
			return True
		elif v in inprogress: # This means we depend on something whose dependencies are still being satisfied (cycle)
			# print 'Hit in progress node'
			return False
		else:
			dependencies = graph.get_adjacent(v)
			if v in unvisited: unvisited.remove(v)
			inprogress.add(v)
			for d in dependencies:
				acyclic = visit(d)
				if not acyclic:
					# print 'Dependency returned false:', d
					return False

			# All dependencies have returned succesfully
			inprogress.remove(v)
			complete.add(v)
			sort.append(v) # Add a node to the topological sort if all dependencies have been satisfied.
			return True

	while (len(unvisited)):
		node = unvisited.pop()
		acyclic = visit(node)
		if not acyclic: return None

	return sort

# Examples

# 1. Example that IS a DAG
print 'Example 1: has a solution'
g = Graph()
[g.add_vertex(i) for i in range(6)]
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

topo_sort = topological_sort(g)
print 'Topological Sort:', topo_sort

# 2. Example with a cycle
print 'Example 2: no solution'
g = Graph()
[g.add_vertex(i) for i in range(6)]
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 2)

topo_sort = topological_sort(g)
print 'Topological Sort:', topo_sort

# 3. Example with no dependencies (no edges in graph)
print 'Example 3: no edges, any order should work'
g = Graph()
[g.add_vertex(i) for i in range(100)]
topo_sort = topological_sort(g)
print 'Topological Sort:', topo_sort