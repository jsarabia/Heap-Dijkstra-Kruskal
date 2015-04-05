'''
Joseph Sarabia
Programming Assignment 1
2/22/15
'''

class Vertex:
	def __init__(self, name):
		self.name = name
		self.connected_to = {}
	def addNeighbor(self, neighbor, weight = 0):
		self.connected_to[neighbor] = weight
	def getWeight(self, neighbor):
		if neighbor in self.connected_to:
			return self.connected_to[neighbor]
		else:
			return float("inf")
	def getName(self):
		return self.name
	def getNeighbors(self):
		return self.connected_to.keys()

class Graph:
	def __init__(self):
		self.vertex_list = {}
		self.n_vertices = 0
	def addVertex(self, name):
		self.n_vertices += 1
		self.vertex_list[name] = Vertex(name)
	def getVertex(self, name):
		if name in self.vertex_list:
			return self.vertex_list[name]
		else:
			return None
	def addEdge(self, f_vertex, t_vertex, weight):
		if f_vertex not in self.vertex_list:
			self.addVertex(f_vertex)
		if t_vertex not in self.vertex_list:
			self.addVertex(t_vertex)
		self.vertex_list[f_vertex].addNeighbor(t_vertex, weight)
	def getVertices(self):
		return self.vertex_list.keys()

class Kruskal:
	#Generate a unique list of edges
	def __init__(self, graph):
		self.edges = {}
		self.sets = {}
		T = []
		#create a sorted list of edges
		for x in graph.vertex_list.keys():
			connections = graph.vertex_list[x].connected_to
			for y in connections.keys():
				edge_name = x + '-' + y
				reverse  = y + '-' + x
				if reverse not in self.edges.keys():
					self.edges[edge_name] = connections[y]
		self.edges = sorted(self.edges.items(), key=lambda x: (x[1],x[0]))
		#create set for each vertex
		for x in graph.vertex_list.keys():
			self.sets[x] = [x, 1]
	def mst(self, graph):
		T = []
		for x in self.edges:
			u = x[0][0]
			v = x[0][2]
			if self.findSetParent(u) != self.findSetParent(v):
				T.append(x)
				self.union(u,v)
		weight = 0
		edges_string = ''
		for x in T:
			weight += x[1]
			edges_string += x[0] + ', '
		edges_string = edges_string[:len(edges_string)-2]
		print("Minimum Spanning Tree: Total Weights on MST Edges = " + str(weight))
		print("Node Set = " + str(sorted(graph.vertex_list.keys())) + ", Edge set = {" + edges_string + '}')
		return T

	#find the disjoint set the vertex belongs to
	def findSetParent(self, child):
		if(self.sets[child][0] == child):
			return child
		else:
			return self.findSetParent(self.sets[child][0])
	def union(self, u, v):
		if(self.sets[self.findSetParent(u)][1] > self.sets[self.findSetParent(v)][1]):
			self.sets[v][0] = self.sets[u][0]
		elif(self.sets[self.findSetParent(u)][1] > self.sets[self.findSetParent(v)][1]):
			self.sets[u][0] = self.sets[v][0]
		else:
			self.sets[self.findSetParent(u)][0] = self.sets[v][0]
			self.sets[self.findSetParent(v)][1] += 1

def main():
	g = Graph()

	
	g.addEdge('A', 'B', 22)
	g.addEdge('A', 'C', 9)
	g.addEdge('A', 'D', 12)

	
	g.addEdge('B', 'A', 22)
	g.addEdge('B', 'C', 35)
	g.addEdge('B', 'F', 36)
	g.addEdge('B', 'H', 34)

	
	g.addEdge('C', 'A', 9)
	g.addEdge('C', 'B', 35)
	g.addEdge('C', 'D', 4)
	g.addEdge('C', 'E', 65)
	g.addEdge('C', 'F', 42)

	
	g.addEdge('D', 'A', 12)
	g.addEdge('D', 'C', 4)
	g.addEdge('D', 'E', 33)
	g.addEdge('D', 'I', 30)

	
	g.addEdge('E', 'C', 65)
	g.addEdge('E', 'D', 33)
	g.addEdge('E', 'F', 18)
	g.addEdge('E', 'G', 23)

	
	g.addEdge('F', 'B', 36)
	g.addEdge('F', 'C', 42)
	g.addEdge('F', 'E', 18)
	g.addEdge('F', 'G', 39)
	g.addEdge('F', 'H', 24)

	
	g.addEdge('G', 'E', 23)
	g.addEdge('G', 'F', 39)
	g.addEdge('G', 'H', 25)
	g.addEdge('G', 'I', 21)

	
	g.addEdge('H', 'B', 34)
	g.addEdge('H', 'F', 24)
	g.addEdge('H', 'G', 25)
	g.addEdge('H', 'I', 19)

	
	g.addEdge('I', 'D', 30)
	g.addEdge('I', 'G', 21)
	g.addEdge('I', 'H', 19)

	k = Kruskal(g)
	k.mst(g)

if __name__ == "__main__":
	main()