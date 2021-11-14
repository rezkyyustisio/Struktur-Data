# Program perkalian matriks
matA = []
matB = []
hasil_2 = [
	[0]*2,
	[0]*2
]
hasil_3 = [
	[0]*3,
	[0]*3,
	[0]*3
]
jml_baris_a = int(input("Masukkan jumlah baris matriks A : "))
for baris in range(jml_baris_a):
	matA.append([int(s) for s in input("Masukkan elemen matriks A baris ke-"+str(baris+1)+" (pisahkan dengan spasi) ").split()])
print(matA)
jml_baris_b = int(input("Masukkan jumlah baris matriks B : "))
for baris in range(jml_baris_b):
	matB.append([int(s) for s in input("Masukkan elemen matriks B baris ke-"+str(baris+1)+" (pisahkan dengan spasi) ").split()])
if len(matA[0]) == jml_baris_b:
	# Persyaratan perkalian matriks ordo 2 kali 2
	if len(matA[0]) == 2 and len(matB) == 2:
		# Perkalian matriks ordo 2 kali 2
		for baris_mat in range(len(matA[0])):
			for kolom_mat in range(len(matA[0])):
				row = 0
				for indeks_mat in range(len(matA[0])):
					row += matA[baris_mat][indeks_mat] * matB[baris_mat][kolom_mat]
					hasil_2[baris_mat][kolom_mat] = row
		print()
		print("Hasil perkalian matriks A dan matriks B adalah")
		for elemen in hasil_2:
			print(elemen)
	# Persyaratan perkalian matriks ordo 3 kali 3
	elif len(matA[0]) == 3 and len(matB) == 3:
		# Perkalian matriks ordo 3 kali 3
		for baris_mat in range(len(matA[0])):
			for kolom_mat in range(len(matA[0])):
				row = 0
				for indeks_mat in range(len(matA[0])):
					row += matA[baris_mat][indeks_mat] * matB[baris_mat][kolom_mat]
					hasil_3[baris_mat][kolom_mat] = row
		print()
		print("Hasil perkalian matriks A dan matriks B adalah")
		for elemen in hasil_3:
			print(elemen)
else:
	print("Perkalian matriks A dan B tidak bisa, karena tidak memenuhi persyaratan")


# Matriks 2 kali 2
# var baris_mat => 0 0 0 0 1 1 1 1
# var kolom_mat => 0 0 1 1 0 0 1 1
# var indeks_mat => 0 1 0 1 0 1 0 1

# hasil_2 = []
# hasil_2.append([0]*len(matB[0]))
