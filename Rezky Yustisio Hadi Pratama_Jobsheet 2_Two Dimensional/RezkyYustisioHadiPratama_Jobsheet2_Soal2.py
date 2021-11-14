# Matriks A
matA = []
jml_baris_a = int(input("Masukkan jumlah baris matriks A: "))
jml_klm_a = int(input("Masukkan jumlah kolom matriks A: "))
hasil = []
for i in range(jml_baris_a):
	hasil.append([]*jml_klm_a)
	matA.append([int(s) for s in input("Masukkan elemen matriks A baris ke-"+str(i+1)+" (pisahkan dengan spasi) ").split()])
	if len(matA[i]) > jml_klm_a:
		print("Kolom lebih dari", jml_klm_a)
		matA = []
		break
	elif len(matA[i]) < jml_klm_a:
		matA = []
		print("Kolom kurang dari", jml_klm_a)
		break
# Matriks B
matB = []
jml_baris_b = int(input("Masukkan jumlah baris matriks B: "))
jml_klm_b = int(input("Masukkan jumlah kolom matriks B: "))
# pengecekan baris dan kolom, kedua matriks harus sama
if jml_baris_a != jml_baris_b or jml_klm_a != jml_klm_b:
	print("Syarat tidak terpenuhi!")
else:
	for i in range(jml_baris_b):
		matB.append([int(s) for s in input("Masukkan elemen matriks B baris ke-"+str(i+1)+" (pisahkan dengan spasi) ").split()])
		if len(matB[i]) > jml_klm_b:
			print("Kolom lebih dari", jml_klm_b)
			matB = []
			break
		elif len(matB[i]) < jml_klm_b:
			print("Kolom kurang dari", jml_klm_b)
			matB = []
			break
# Proses
for baris_mat in range(len(matA)):
	for kolom_mat in range(len(matA)):
		hasil[baris_mat].append(matA[baris_mat][kolom_mat] + matB[baris_mat][kolom_mat])
# Hasil
for a in range(len(hasil)):
	for b in hasil[a]:
		print(b, end=" ")
	print()