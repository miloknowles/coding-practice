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