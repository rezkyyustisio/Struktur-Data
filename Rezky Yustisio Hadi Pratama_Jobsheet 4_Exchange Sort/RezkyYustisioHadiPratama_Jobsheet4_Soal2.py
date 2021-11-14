jml_data = int(input("Masukkan jumlah data yang ingin di masukkan: "))
data = [int(s) for s in input("Masukkan data: ").split()]
if len(data) > jml_data:
	print("Maaf, data yang anda masukkan melebihi %s data" % (jml_data))
elif len(data) < jml_data:
	print("Maaf, data yang anda masukkan kurang dari %s data" % (jml_data))
else:
	for pivot in range(0, len(data) - 1):
		for j in range(pivot+1, len(data)):
			if data[j] < data[pivot]:
				data[j],data[pivot] = data[pivot],data[j]
	print(data)


