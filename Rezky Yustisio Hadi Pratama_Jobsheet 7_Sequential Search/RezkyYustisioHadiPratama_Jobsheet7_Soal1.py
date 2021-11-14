data = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
ketemu = False
key = 5
perbandingan = 0
for i in range(len(data)):
	perbandingan = i + 1
	if data[i] == key:
		ketemu = True
		indeks = i
		break
if ketemu:
	print("Angka "+str(key)+" ditemukan di indeks "+str(indeks))
	print("Jumlah perbandingan "+str(perbandingan))
else:
	print("Angka tidak ditemukan")
	print("Jumlah perbandingan "+str(perbandingan))

	
