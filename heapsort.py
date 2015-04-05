'''
Joseph Sarabia
Programming Assignment 1
2/22/15
'''

class Heap:
	def __init__(self, array):
		self.heap = []
		for x in range(len(array)):
			self.addChild(array[x])
		print(self.heap)
	def addChild(self, child):
		self.heap.append(child)
		self.siftUp(len(self.heap))
	def siftUp(self, i):
		#if i is the root, can't sift further up
		if i == 0:
			return;
		parent = 0
		if i % 2 == 0:
			parent = i//2-1
		else:
			parent = i//2
		largestChild = parent*2+2 if (len(self.heap) > parent*2+2) and (self.heap[parent*2+2] > self.heap[parent*2+1]) else parent*2+1
		if (largestChild < len(self.heap) and self.heap[largestChild] > self.heap[parent]):
			temp = self.heap[largestChild]
			self.heap[largestChild] = self.heap[parent]
			self.heap[parent] = temp
		self.siftUp(parent)
	def siftDown(self, i, length):
		#if i is the root, can't sift further up
		if i >= length:
			return;
		parent = i
		largestChild = parent*2+2 if (length > parent*2+2) and (self.heap[parent*2+2] > self.heap[parent*2+1]) else parent*2+1
		if (largestChild < length and self.heap[largestChild] > self.heap[parent]):
			temp = self.heap[largestChild]
			self.heap[largestChild] = self.heap[parent]
			self.heap[parent] = temp
		self.siftDown(largestChild, length)
	def reheap(self, length):
		self.siftDown(0, length)
		return

	def sort(self):
		length = len(self.heap)
		while length > 0:
			temp = self.heap[0]
			self.heap[0] = self.heap[length - 1]
			self.heap[length-1] = temp
			length -= 1
			self.reheap(length)
		print(self.heap)

def heapsort():
	edges = []
	edges.append(22)
	edges.append(34)
	edges.append(35)
	edges.append(36)
	edges.append(9)
	edges.append(42)
	edges.append(24)
	edges.append(12)
	edges.append(4)
	edges.append(65)
	edges.append(18)
	edges.append(39)
	edges.append(25)
	edges.append(19)
	edges.append(23)
	edges.append(33)
	edges.append(21)
	edges.append(30)
	print("Array: ")
	print(edges)
	print("Heapified Array: ")
	heap = Heap(edges)
	print("Sorted Array: ")
	heap.sort()

def main():
	heapsort()
if __name__ == "__main__":
	main()