data = [12,15,7,10,25,2,17,25,5,20]
for i in range(0,len(data) - 1):
	if data[i] > data[i+1]:
		data[i],data[i+1] = data[i+1],data[i]	
print(data)

