# print(a)
# for indeks in range(1, len(a)):
# 	if a[indeks] < a[terkecil]:
# 		terkecil = indeks
# a[0],a[terkecil] = a[terkecil], a[0]
# print(a)
# for indeks in range(2, len(a)):
# 	if a[indeks] < a[terkecil]:
# 		terkecil = indeks
# a[1],a[terkecil] = a[terkecil], a[1]
# print(a)
# for indeks in range(3, len(a)):
# 	if a[indeks] < a[terkecil]:
# 		terkecil = indeks
# a[2],a[terkecil] = a[terkecil], a[2]
# print(a)
#    0  1   2  3  4  5  6  7  8  9
a = [3,2,1]
for proses in range(0, len(a) - 1):
	terkecil = proses
	for indeks in range(terkecil + 1, len(a)):
		if a[indeks] < a[terkecil]:
			terkecil = indeks
	a[proses],a[terkecil] = a[terkecil],a[proses]
print(a)