data = [12,15,7,10,25,2,17,25,5,20]
for i in range(0,len(data)):
	for j in range(0, len(data) - 1):
		if data[j] > data[j+1]:
			data[j],data[j+1] = data[j+1],data[j]
print(data)

