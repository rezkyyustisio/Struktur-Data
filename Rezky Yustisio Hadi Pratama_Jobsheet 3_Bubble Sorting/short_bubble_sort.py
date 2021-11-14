a = [40,30,20,5,10]
loop_count = 0
for i in range(1, len(a)):
	for indeks in range(len(a) - i):
		loop_count += 1
		if a[indeks + 1] > a[indeks]:
			a[indeks], a[indeks + 1] = \
			a[indeks + 1], a[indeks]
print(a)
print("Jumlah perulangan=", loop_count)

a = [40,30,20,5,10]
ada_pertukaran = True
proses = len(a) - 1
loop_count = 0
while proses > 0 and ada_pertukaran:
	ada_pertukaran = False
	for indeks in range(0, proses):
		loop_count += 1
		if a[indeks+1] > a[indeks]:
			ada_pertukaran = True
			a[indeks], a[indeks+1] = a[indeks+1], a[indeks]
print(a)
print("Jumlah perulangan=", loop_count)