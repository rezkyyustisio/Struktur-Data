data = [12,15,7,10,25,2,17,25,5,20]
maks = []
indeks = []
for i in range(0, len(data) - 1):
	if data[i] >= max(data):
		maks.append(data[i])
		indeks.append(i)
print("Max : ", end="")
for m in maks:
	print(m, end=" ")
print()
print("Jum :",len(maks))
print("Indeks: ", end="")
for i in indeks:
	print(i, end=" ")


