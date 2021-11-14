def binary_search(data, key):
	l = 0
	r = len(data) - 1
	ditemukan = False
	perbandingan = 0
	while l <= r and (not ditemukan):
		m = int((l + r) / 2)
		perbandingan += 1
		if data[m] == key:
			ditemukan = True
		elif key < data[m]:
			r = m - 1
		elif key > data[m]:
			l = m + 1
	if not ditemukan:
		print("Data tidak ditemukan")
	else:
		print("Sorted: ", end="")
		for d in data:
			print(d, end=" ")
		print()
		print(key, "berada di indeks", m)
		
data = sorted([int(s) for s in input("Masukan angka: ").split()])
key = 5
binary_search(data, key)