class Stack(object):
	"""docstring for Stack"""
	def __init__(self):
		self.item=[]

	def isEmpty(self):
		return (len(self.item))==0

	def __len__(self):
		return len(self.item)

	def peek(self):
		if self.isEmpty() == True:
			return None
		else:
			return self.item[-1]

	def pop(self):
		if self.isEmpty() == True:
			print("Stack is Empty")	
		else:
			return self.item.pop()

	def push(self, data):
		self.item.append(data)

nilai=Stack()
for i in range(15):
	if i % 3==0:
		nilai.push(i)
	elif i % 4==0:
		nilai.pop()
	print(str(i) + ":" + str(nilai.peek()))

