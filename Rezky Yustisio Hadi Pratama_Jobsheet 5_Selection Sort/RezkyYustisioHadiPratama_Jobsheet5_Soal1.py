data = [3,10,4,6,8,9,7,2,5,1]
for indeks in range(len(data) - 1):
	if data[indeks+1] < data[0]:
		terkecil = data[indeks+1]
print(terkecil)


