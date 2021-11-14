# Soal 8
a = [5,10,6,0,4]
a.reverse()
b = []
for i in range(0, len(a)):
	if a[i] % 2 == 0 and a[i] > 0:
		b.insert(0, a[i])
	else:
		b.append("_")
print(b)


