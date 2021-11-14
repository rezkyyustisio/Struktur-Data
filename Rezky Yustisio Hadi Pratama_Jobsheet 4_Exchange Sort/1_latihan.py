data = [3,2,1]
pivot = 0

# Proses 1
if data[1] < data[pivot+1]:
	data[1],data[pivot+1] = data[pivot+1],data[1]

if data[2] < data[pivot+1]:
	data[2],data[pivot+1] = data[pivot+1],data[2]

# Proses 2
if data[1] < data[pivot+2]:
	data[1],data[pivot+2] = data[pivot+2],data[1]
print(data)

