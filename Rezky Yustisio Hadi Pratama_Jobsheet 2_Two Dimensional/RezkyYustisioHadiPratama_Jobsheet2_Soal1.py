print("==== PROGRAM ARRAY MULTIDIMENSI ====")
array = []
jml_baris = int(input("Masukkan jumlah baris array: "))
jml_klm = int(input("Masukkan jumlah kolom array: "))
for i in range(jml_baris):
	array.append([]*jml_baris)
	for j in range(jml_klm):
		array[i].append(int(input("Masukkan jumlah elemen matriks baris "+str(i)+" kolom "+str(j)+" : ")))
print("Data yang anda masukkan adalah:")
for a in range(len(array)):
	for b in array[a]:
		print(b, end=" ")
	print()