class Stack:
	stack_list = []
	max_size = 0
	top = 0

	def __init__(self, size):
		self.max_size = size
		self.stack_list = [0] * size
		self.top = -1

	def push(self, x):
		self.top += 1
		self.stack_list[self.top] = x
		return self.stack_list

	def pop(self):
		dummy = self.stack_list[self.top]
		self.top -= 1
		return dummy

	def is_empty(self):
		return self.top == -1

	def is_full(self):
		return self.top == self.max_size - 1

	def clear(self):
		self.top = -1

import random
import time
mystack = Stack(20)
while(not mystack.is_full()):
	angka_random = random.randrange(0, 50, 5)
	print(f"Memasukan {angka_random} ke dalam Stack")
	time.sleep(0.1)
	mystack.push(angka_random)
mystack.clear()

while(not mystack.is_empty()):
	print(mystack.pop(), end=" ")
print()





