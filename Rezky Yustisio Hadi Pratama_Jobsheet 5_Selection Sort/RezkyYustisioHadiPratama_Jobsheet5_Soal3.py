a = [3,10,4,6,8,9,7,2,1,5]
for proses in range(0, len(a)-1):
	terkecil = proses
	for indeks in range(terkecil+1, len(a)):
		if a[indeks] < a[terkecil]:
			terkecil = indeks
	a[proses],a[terkecil] = a[terkecil],a[proses]
print(a)


