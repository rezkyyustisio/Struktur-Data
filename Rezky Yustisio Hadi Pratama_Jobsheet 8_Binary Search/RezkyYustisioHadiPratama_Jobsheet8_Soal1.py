data = sorted([12, 15, 7, 10, 25, 2, 17, 25, 5, 20])
key = 5
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
	




