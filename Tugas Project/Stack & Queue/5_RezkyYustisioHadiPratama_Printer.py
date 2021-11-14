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

class PrinterSpooler(Queue):
	def input_dokumen(self, nama_dokumen):
		return self.enqueue(nama_dokumen)

	def show_dokumen(self, daftar_dokumen):
		for i in range(0, len(daftar_dokumen)):
			print("+", daftar_dokumen[i])

	def print_dokumen(self):
		return self.dequeue()
print("""
	>> Aplikasi Printer Spooler Command Line <<

Created: Rezky Yustisio Hadi Pratama
""")
jumlah_dokumen = int(input("Masukan jumlah dokumen: "))
objek = PrinterSpooler(jumlah_dokumen)
print()
for i in range(jumlah_dokumen):
	input_dokumen = input("Masukan dokumen (doc, pdf): ")
	objek.input_dokumen(input_dokumen)
print()
print("List dokumen: ")
objek.show_dokumen(objek.que_array)
nomor_dokumen = objek.head
for i in range(jumlah_dokumen):
	print()
	print_dokumen = input("Print dokumen "+objek.que_array[nomor_dokumen]+" (ya, tidak): ")
	if print_dokumen == "ya":
		objek.dequeue()
		nomor_dokumen += 1
		print("# Dokumen berhasil di print")
	elif print_dokumen == "tidak":
		nomor_dokumen += 1
print()
print("Sisa dokumen yang belum di print: ")
if objek.is_empty():
	print("Kosong")
while(not objek.is_empty()):
	n = objek.dequeue()
	print("-",n, end=" ")
	print()
print()
print("Bye-bye!")
