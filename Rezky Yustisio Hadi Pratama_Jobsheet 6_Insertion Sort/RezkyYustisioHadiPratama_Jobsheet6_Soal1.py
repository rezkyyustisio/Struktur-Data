data = [4,3,2,1]
# 4 3 2 1
# 3 4 2 1
# 3 2 4 1
# 2 3 4 1
# 2 3 1 4
# 2 1 3 4
# 1 2 3 4
for i in range(len(data) - 1):
	# 0 1 2 -> indeks variabel i
	proses = i + 1
	# isi proses = 1
	# isi proses = 2
	# isi proses = 3
	for j in range(i + 1, 0, -1):
		# i awal di tambah 1
		# 0 + 1 = 1, j = 1
		# 1 + 1 = 2, j = 2
		# 2 + 1 = 3, j = 3
		if data[proses] < data[j-1]:
		# perulangan pertama
		# jika indeks 1 (3) < indeks 0 (4) maka tukar = 3 4  
		# [3,4,2,1]
		# 
		# perulangan kedua
		# jika indeks 2 (2) < indeks 1 (4) maka tukar
		# [3,2,4,1]
		# jika indeks 1 (2) < indeks 0 (3) maka tukar
		# [2,3,4,1]
		# 
		# perulagan ketiga 
		# jika indeks 3 (1) < indeks 2 (2) (ini di dapat dari j - 1 atas) maka tukar
		# [2,3,1,4]
		# jika indeks 2 (1) (ini di dapat dari j - 1 bawah) < indeks 1 (3) maka tukar
		# [2,1,3,4]
		# jika indeks 1 (1) < indeks 0 (2) maka tukar
		# [1,2,3,4]
			data[proses],data[j-1] = data[j-1],data[proses]
			proses = j - 1
	print(i, ".", data)
# print(data)

#  0 1 2 3 4
# [4,3,2,1]

# 1 < 0 ? tukar 
# [3,4,2,1]

# 2 < 1 ? tukar 
# [3,2,4,1]
# 1 < 0 ? tukar 
# [2,3,4,1]

# 3 < 2 ? tukar 
# [2,3,1,4]
# 2 < 1 ? tukar 
# [2,1,3,4]
# 1 < 0 ? tukar 
# [1,2,3,4]
# -------------
#  0 1 2 3
# [1,2,3,4]
# 
# 1 < 0 ? tidak
# 
# 2 < 1 ? tidak
# 2 < 0 ? tidak
# 
# 3 < 2 ? tidak
# 3 < 1 ? tidak
# 3 < 0 ? tidak
