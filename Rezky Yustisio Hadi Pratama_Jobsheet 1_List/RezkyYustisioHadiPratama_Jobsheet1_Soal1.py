# Soal 1
mylist = [int(s) for s in input("Masukkan angka dipisahkan ").split()]
total = sum(mylist)
print("Jumlah total data di list adalah", total)
print("Rata-rata:", total/len(mylist))

