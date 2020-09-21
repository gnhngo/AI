# CS 44201
# Giang Ngo
# 09/19/20
# Implement a BFS to search on given graph
# Output result starting with node A 
 
class Vertex:
	def __init__(self, n): # constructor to take a name argument 
		
		# letter name of each vertex
		self.name = n 

		# list of adjacent vertices of a specific vertex
		self.neighbors = list() # empty list for the neighbors

		self.color = 'black' # not visited 

	def add_neighbor(self, v):
		# check if adjacent vertex to add to the neighbor list
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort() # stores the neighbor(s) in a sorted list

class Graph:
	vertices = {} # empty dictionary object

	# function to add vertex to vertices dictionary object
	def add_vertex(self, vertex):

		# check if vertex var is vertex object
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
			return True # finish adding edge(s)
		else:
			return False

	# function to print out the list of vertices in order and 
	# the list of their neighbor(s)
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors))

	# breadth first search function
	def bfs(self, vert):
		q = list()
		vert.color = 'red' # visited

		for v in vert.neighbors:
			q.append(v)

		while len(q) > 0: # q is letter name of the vertex
			u = q.pop(0)
			node_u = self.vertices[u]
			node_u.color = 'red' # visited

			for v in node_u.neighbors:
				node_v = self.vertices[v]
				if node_v.color == 'black':
					q.append(v)

g = Graph() # assign new graph object
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('G')):
	g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AC', 'BC', 'BD', 'CD', 'CE', 'DE', 'DF', 'EF']
for edge in edges:
	g.add_edge(edge[:1], edge[1:])

g.bfs(a) # call bfs function starting at vertex A (source)
g.print_graph()

		
		