data = [3,10,4,6,8,9,7,2,1,5]
for indeks in range(len(data) - 1):
	if data[indeks+1] < data[indeks]:
		terkecil = indeks+1
data[0],data[terkecil] = data[terkecil],data[0]
print(data)



