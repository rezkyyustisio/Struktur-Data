# Matriks A
matA = []
jml_baris_a = int(input("Masukkan jumlah baris matriks A: "))
jml_klm_a = int(input("Masukkan jumlah kolom matriks A: "))
hasil = []
status = True
for i in range(jml_baris_a):
	matA.append([int(s) for s in input("Masukkan elemen matriks A baris ke-"+str(i+1)+" (pisahkan dengan spasi) ").split()])
	if len(matA[i]) > jml_klm_a:
		matA = []
		status = False
		print("Kolom lebih dari", jml_klm_a)
		break
	elif len(matA[i]) < jml_klm_a:
		matA = []
		status = False
		print("Kolom kurang dari", jml_klm_a)
		break
if status != False:
	# Matriks B
	matB = []
	jml_baris_b = int(input("Masukkan jumlah baris matriks B: "))
	jml_klm_b = int(input("Masukkan jumlah kolom matriks B: "))
	# pengecekan baris dan kolom, kedua matriks harus sama
	if jml_klm_a != jml_baris_b:
		print("Syarat tidak terpenuhi")
	else:
		for i in range(jml_baris_b):
			matB.append([int(s) for s in input("Masukkan elemen matriks B baris ke-"+str(i+1)+" (pisahkan dengan spasi) ").split()])
			if len(matB[i]) > jml_klm_b:
				matB = []
				status = False
				print("Kolom lebih dari", jml_klm_b)
				break
			elif len(matB[i]) < jml_klm_b:
				matB = []
				status = False
				print("Kolom kurang dari", jml_klm_b)
				break
		if status != False:
			# Proses
			for kolom_mat in range(len(matB[0])):
				hasil.append([0]*jml_klm_b)
				for baris_mat in range(len(matB[0])):
					total = 0
					for indeks_mat in range(len(matA[0])):	
						total += matA[kolom_mat][indeks_mat] * matB[indeks_mat][baris_mat]
						hasil[kolom_mat][baris_mat] = total
			# Hasil
			for a in range(len(hasil)):
				for b in hasil[a]:
					print(b, end=" ")
				print()


		