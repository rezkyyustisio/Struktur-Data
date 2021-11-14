def bubble_sort(tipe, data):
	if tipe == 1:
		# Ascending 
		print()
		print("Proses Sorting Metode Bubble Sort Secara Ascending")
		for i in range(0,len(data) - 1):
			for j in range(0, len(data) - 1):
				if data[j] > data[j+1]:
					data[j],data[j+1] = data[j+1],data[j]
				print(data)
		return data
	elif tipe == 2:
		# Descending
		print()
		print("Proses Sorting Metode Bubble Sort Secara Descending")
		for i in range(0,len(data) - 1):
			for j in range(0, len(data) - 1):
				if data[j] < data[j+1]:
					data[j],data[j+1] = data[j+1],data[j]
				print(data)
		return data

def exchange_sort(tipe, data):
	if tipe == 1:
		# Ascending
		print()
		print("Proses Sorting Metode Exchange Sort Secara Ascending")
		for pivot in range(0, len(data) - 1):
			for j in range(pivot+1, len(data)):
				if data[j] < data[pivot]:
					data[j],data[pivot] = data[pivot],data[j]
				print(data)
		return data
	elif tipe == 2:
		# Descending
		print()
		print("Proses Sorting Metode Exchange Sort Secara Descending")
		for pivot in range(0, len(data) - 1):
			for j in range(pivot+1, len(data)):
				if data[j] > data[pivot]:
					data[j],data[pivot] = data[pivot],data[j]
				print(data)
		return data

def selection_sort(tipe, data):
	if tipe == 1:
		# Ascending
		print()
		print("Proses Sorting Metode Selection Sort Secara Ascending")
		for proses in range(0, len(data) - 1):
			terkecil = proses
			for indeks in range(terkecil + 1, len(data)):
				if data[indeks] < data[terkecil]:
					terkecil = indeks
			data[proses],data[terkecil] = data[terkecil],data[proses]
			print(data)
		return data
	elif tipe == 2:
		# Descending
		print()
		print("Proses Sorting Metode Selection Sort Secara Descending")
		for proses in range(0, len(data) - 1):
			terkecil = proses
			for indeks in range(terkecil + 1, len(data)):
				if data[indeks] > data[terkecil]:
					terkecil = indeks
			data[proses],data[terkecil] = data[terkecil],data[proses]
			print(data)
		return data

def insertion_sort(tipe, data):
	if tipe == 1:
		# Ascending
		print()
		print("Proses Sorting Metode Insertion Sort Secara Ascending")
		for i in range(len(data) - 1):
			proses = i + 1
			for j in range(i + 1, 0, -1):
				if data[proses] < data[j-1]: 
					data[proses],data[j-1] = data[j-1],data[proses]
					proses = j - 1
				print(data)
		return data
	elif tipe == 2:	
		# Descending
		print()
		print("Proses Sorting Metode Insertion Sort Secara Descending")
		for i in range(len(data) - 1):
			proses = i + 1
			for j in range(i + 1, 0, -1):
				if data[proses] > data[j-1]: 
					data[proses],data[j-1] = data[j-1],data[proses]
					proses = j - 1
				print(data)
		return data

def foreach_result_data(data):
	print("Sorted: ", end="")
	for d in data:
		print(d, end=" ")

print("""
_____________________________

# Program Pengurutan Angka # 
				
Pilih Algoritma Pengurutan : 	
1. Bubble Sort 				
2. Exchange Sort 				
3. Selection Sort 		
4. Insertion Sort 			

_____________________________
""")

metode_pengurutan = int(input("Masukkan nomor angka metode pengurutan(1,2,3,4): "))

print("""
+ Tipe Pengurutan -
1. Ascending
2. Descending
""")

tipe_pengurutan = int(input("Masukkan nomor angka tipe pengurutan(1,2): "))
print()

while(True):
	# Bubble
	if metode_pengurutan == 1:
		data = [int(s)  for s in input("Masukkan angka: ").split()]
		result = bubble_sort(tipe_pengurutan, data)
		print()
		foreach_result_data(result)
		print()

	# Exchange
	elif metode_pengurutan == 2:
		data = [int(s)  for s in input("Masukkan angka: ").split()]
		result = exchange_sort(tipe_pengurutan, data)
		print()
		foreach_result_data(result)

	# Selection
	elif metode_pengurutan == 3:
		data = [int(s)  for s in input("Masukkan angka: ").split()]
		print()
		print("Proses Sorting Metode Selection Sort")
		result = selection_sort(tipe_pengurutan, data)
		print()
		foreach_result_data(result)

	# Insertion
	elif metode_pengurutan == 4:
		data = [int(s)  for s in input("Masukkan angka: ").split()]
		print()
		print("Proses Sorting Metode Insertion Sort")
		result = insertion_sort(tipe_pengurutan, data)
		print()
		foreach_result_data(result)

	else:
		print("Nomor yang anda masukkan tidak di temukan")
	print()
	status = input("Apakah ingin mengulang? (y,n): ")
	if status.lower() != "y":
		print()
		print("Terimakasih telah menggunakan aplikasi kami :)")
		print("Creator: Rezky Yustisio Hadi Pratama")
		break