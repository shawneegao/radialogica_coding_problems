class Stack:
	def __init__(self):
		self.data = []
	def showStack(self):
		return self.data;
	def remove(self):
		self.data.pop()
	def add(self, item):
		self.data.append(item)
	def size(self):
		return len(self.data);
	def peek(self):
		return self.data[len(self.data) - 1]

		