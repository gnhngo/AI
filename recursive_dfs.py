# CS 44201
# Giang Ngo
# 09/19/20
# Implement a “Recursive” DFS to search
# Output result starting with node A

class Vertex:
	def __init__(self, n):
		self.name = n # letter name of the vertex
		self.neighbors = list() # list of adjacent vertices of a specific vertex
		self.color = 'black' # not discovered

	def add_neighbor(self, v):
		# convert neighbor list to a set and check if vertex is in neighbor list
		nset = set(self.neighbors)
		if v not in nset:
			self.neighbors.append(v)
			self.neighbors.sort() # stores in sorted order

class Graph:
	vertices = {} # dictionary object

	def add_vertex(self, vertex):
		# check if it is vertex object and not in vertices list
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False

	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False

	# function to print out result to see how graph looks
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

	# Recursive Python implementation of DFS
	def _dfs(self, vertex): # function used internally
		vertex.color = 'red' # discovered
		for v in vertex.neighbors:
			if self.vertices[v].color == 'black':
				self._dfs(self.vertices[v])

	def dfs(self, vertex):
		self._dfs(vertex)

g = Graph() # assign new graph object
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('G')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', 'DF', 'EF']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.dfs(a) # call bfs function starting at vertex A (source)
g.print_graph()



