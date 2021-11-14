data = sorted([int(s) for s in input("Masukan angka: ").split()])
i = 0
perbandingan = 0
ketemu = False
key = 5
while not ketemu and i < len(data):
	perbandingan = i + 1
	if data[i] == key:
		ketemu = True 
		indeks = i
	else:
		i += 1
if ketemu:
	print("Sorted: ", end="")
	for angka in data:
		print(angka, end=" ")
	print()
	print("Angka "+str(key)+" ditemukan di indeks "+str(indeks))
	print("Jumlah perbandingan "+str(perbandingan))
else:
	print("Angka tidak ditemukan")
	print("Jumlah perbandingan "+str(perbandingan))



		



