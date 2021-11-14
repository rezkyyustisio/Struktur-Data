jml_data = int(input("Masukkan jumlah data yang ingin di masukkan: "))
data = [int(s) for s in input("Masukkan data: ").split()]
if len(data) > jml_data:
	print("Maaf, data yang anda masukkan melebihi %s data" % (jml_data))
elif len(data) < jml_data:
	print("Maaf, data yang anda masukkan kurang dari %s data" % (jml_data))
else:
	for i in range(0,len(data)):
		for j in range(0, len(data) - 1):
			if data[j] > data[j+1]:
				data[j],data[j+1] = data[j+1],data[j]
	print(data)

