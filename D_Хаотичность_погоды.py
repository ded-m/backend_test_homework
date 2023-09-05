file_in='input.txt'
with open(file_in, 'r') as f:
	n=int(f.readline())
	arr=list(map(int,f.readline().split()))
output=0
if n==1:
	output=1
else:
	if arr[0]>arr[1]:
		output += 1
	if arr[n-1]>arr[n-2]:
		output += 1
	for day in range(1,n-1):
		if arr[day-1]<arr[day] and arr[day+1]<arr[day]:
			output += 1
print(output)
