#utilizes the stack class to keep track of seen characters
import sys

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

def balancedBrackets(testString):
	balanced = False
	for c in testString:
		if (c == '(' or 
			c == '{' or 
			c == '['):
			stack.add(c)
		elif c == ')':
			if (
				stack.size() == 0 or
				stack.peek() != '('
			   ): 
				print "error at %s" %(c)
				return balanced
			else:
				stack.remove()
		elif c == '}':
			if (
				stack.size() == 0 or
				stack.peek() != '{'
			   ):
				return balanced
			else:
				stack.remove()	
		elif c == ']':
			if (
				stack.size() == 0 or
				stack.peek() != '['
			   ):
				return balanced
			else:
				stack.remove()
		else:
			print "only accepts '(', '{','[', ']', '}',']' as inputs!"			
			return balanced
	if stack.size() == 0:
		balanced = True	
	return balanced
		
	
stack = Stack()
input = sys.argv[1]	
if balancedBrackets(input):
	print "Balanced Brackets!"
else:
	print "Not balanced"
		
		
		
		
		
		
		
		
	
	
	
	
	
	
	
	
	
	
	
	