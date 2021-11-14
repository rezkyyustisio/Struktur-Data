# Soal 2
mylist = list(input("Masukkan sebuah kata/kalimat: "))
jml_vokal = 0
for element in mylist:
	if element == 'a' or \
		element == 'i' or \
		element == 'u' or \
		element == 'e' or \
		element == 'o':
			jml_vokal += 1
print("Jumlah vokal = ", jml_vokal)
print("Jumlah selain vokal = ", len(mylist) - jml_vokal)


