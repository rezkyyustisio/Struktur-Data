data = [12, 15, 7, 10, 25, 2, 17, 25, 5, 20]
for pivot in range(0, len(data) - 1):
	for j in range(pivot+1, len(data)):
		if data[j] < data[pivot]:
			data[j],data[pivot] = data[pivot],data[j]
print(data)


