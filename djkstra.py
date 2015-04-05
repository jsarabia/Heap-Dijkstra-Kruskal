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

class Dijkstra:
	def __init__(self, graph):
		self.paths = {} #{'char', 'string'}
		self.s = [] #list of vertecies
		self.v = {} # {'char', weight}
		self.vp = {}
		self.total_nodes = 0
		self.initializeV(graph)
	def initializeV(self, graph):
		nodes = graph.getVertices()
		self.total_nodes = len(nodes)
		self.s = []
		for i in nodes:
			self.v[i] = float("inf")
			self.vp[i] = float("inf")
			self.paths[i] = ''
			#TODO: need to update the weight for initialization
	def shortestPath(self, f_vertex, t_vertex, graph):
		self.initializeV(graph)
		self.shortestPaths(f_vertex, graph)
		f_vertex = graph.getVertex(f_vertex)
		t_vertex = graph.getVertex(t_vertex)
		done = False
		path = []
		current = t_vertex.name
		while not done:
			path.append(self.paths[current])
			if self.paths[current] == f_vertex.name:
				done = True
			current = self.paths[current]
		string = 'Node ' + t_vertex.name + ': Path Value = ' + str(self.vp[t_vertex.name])
		string += ', Path is :  ' + f_vertex.name
		for x in range(len(path)-1):
			string += ' -> ' + path[len(path)-2-x]
		string += ' -> ' + t_vertex.name
		return string

	def shortestPaths(self, node, graph):
		self.initializeV(graph)
		node = graph.getVertex(node)
		self.s.append(node)
		self.vp[self.s[0].name] = 0
		curr_node = 0
		#iniialize v' list for start node
		neighbors = self.s[curr_node].getNeighbors()
		for x in neighbors:
			t_weight = self.s[curr_node].getWeight(x)
			if (t_weight < self.vp[x]):
				self.vp[x] = t_weight
		for x in self.vp.keys():
			self.paths[x] = self.s[curr_node].name
		names = [x.name for x in self.s]
		while len(self.s) < self.total_nodes:
			tmin = float("inf")
			tname = ''
			for x in set(self.vp.keys()).difference(names):
				if self.vp[x] < tmin:
					tmin = self.vp[x]
					tname = x
			node = graph.getVertex(tname)
			self.s.append(node)
			for x in self.vp.keys():
				self.v[x] = self.vp[x]
			curr_node += 1
			neighbors = self.s[curr_node].getNeighbors()
			names = [x.name for x in self.s]
			for x in set(neighbors).difference(names):
				val1 = self.vp[x]
				val2 = self.vp[self.s[curr_node].name] + self.s[curr_node].getWeight(x)
				if val2 < val1:
					self.paths[x] =  self.s[curr_node].name
					self.vp[x] = val2
		return self.vp


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

	d = Dijkstra(g)
	print(d.shortestPath('A', 'A', g))
	print(d.shortestPath('A', 'B', g))
	print(d.shortestPath('A', 'C', g))
	print(d.shortestPath('A', 'D', g))
	print(d.shortestPath('A', 'E', g))
	print(d.shortestPath('A', 'F', g))
	print(d.shortestPath('A', 'G', g))
	print(d.shortestPath('A', 'H', g))
	print(d.shortestPath('A', 'I', g))

if __name__ == "__main__":
	main()
