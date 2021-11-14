# Soal 3
mylist = list(input("Masukkan sebuah kata/kalimat: ").lower())
jml_vokal = [0]*5
vokal = ['a', 'i', 'u', 'e', 'o']
for element in mylist:
	if element == 'a':
		jml_vokal[0] += 1
	elif element == 'i':
		jml_vokal[1] += 1
	elif element == 'u':
		jml_vokal[2] += 1
	elif element == 'e':
		jml_vokal[3] += 1
	elif element == 'o': 
		jml_vokal[4] += 1
for i in range(0, len(vokal)):
	print("Jumlah vokal %s = %s" % (vokal[i], jml_vokal[i]))
print("Jumlah seluruh vokal = ", sum(jml_vokal))
