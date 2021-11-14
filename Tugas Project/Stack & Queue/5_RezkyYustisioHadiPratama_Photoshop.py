class Stack:
	stack_list = []
	top = 0
	size = 4

	def __init__(self):
		self.top = -1
		self.stack_list = [""] * self.size

	def push(self, x):
		self.top += 1
		self.stack_list[self.top] = x
		return self.stack_list

	def pop(self):
		dummy = self.stack_list[self.top]
		self.top -= 1
		return dummy

	def is_full(self):
		return self.top == len(self.stack_list) - 1

	def clear(self):
		self.top = -1

class Photoshop(Stack):
	foto = ""

	def blur(self, inputan):
		self.push(inputan)
		print("# Foto "+self.foto+" di blur")

	def delete(self, inputan):
		self.push(inputan)
		print("# Foto "+self.foto+" di delete")

	def crop(self, inputan):
		self.push(inputan)
		print("# Foto "+self.foto+" di crop")

	def undo(self):
		back = self.pop()
		if back == "":
			print("Tidak ada perintah untuk di undo!")
			self.clear()
		else:
			print("# Perintah "+back+" dibatalkan")

	def quit(self):
		print("Bye-bye!")

print("""
	>> Aplikasi Photoshop 2019 <<

Created: Rezky Yustisio Hadi Pratama
""")
objek = Photoshop()
nama_foto = input("Masukan nama foto: ")
objek.foto = nama_foto
counter = 0
while(not objek.is_full()):
	print()
	inputan = input("Masukan perintah untuk edit (blur, crop, delete, undo, quit): ").lower()
	if counter == len(objek.stack_list) - 1:
		objek.stack_list.append("")
	if inputan == "blur":
		objek.blur(inputan)
	elif inputan == "crop":
		objek.crop(inputan)
	elif inputan == "delete":
		objek.delete(inputan)
	elif inputan == "undo":
		objek.undo()
	elif inputan == "quit":
		objek.quit()
		break
	else:
		print("# Perintah tidak ditemukan")
	counter += 1