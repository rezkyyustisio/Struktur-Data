class Queue:
	que_array = []
	head = 0
	tail = 0
	n_items = 0
	max_size = 0

	def __init__(self, x):
		self.max_size = x
		self.que_array = [0] * self.max_size
		self.head = 0
		self.tail = -1
		self.n_items = 0

	def enqueue(self, n):
		self.tail += 1
		self.que_array[self.tail] = n 
		self.n_items += 1

	def dequeue(self):
		tmp = self.que_array[self.head]
		self.head += 1
		self.n_items -= 1
		return tmp

	def peek_head(self):
		if not self.is_empty() > 0:
			return self.que_array[self.head]
		else:
			return None

	def is_empty(self):
		return self.n_items == 0

	def is_full(self):
		return self.tail == self.max_size - 1

	def size(self):
		return self.n_items

	def delete_element(self, j):
		self.que_array.remove(j)
		return j

	def search_element(self, j):
		if j in self.que_array:
			print(str(j)+ " Ditemukan")
		else:
			print(str(j)+" tidak ditemukan")

class RezkyYustisioHadiPratam_Queue_10:
	the_queue = Queue(5)
	the_queue.enqueue(10)
	the_queue.enqueue(20)
	the_queue.enqueue(30)
	the_queue.enqueue(40)

	the_queue.dequeue()
	the_queue.dequeue()
	the_queue.dequeue()

	the_queue.enqueue(50)
	the_queue.enqueue(60)
	the_queue.enqueue(70)
	the_queue.enqueue(80)
	the_queue.enqueue(90)

	while( not the_queue.is_empty()):
		n = the_queue.dequeue()
		print(n, end=" ")
	print()


