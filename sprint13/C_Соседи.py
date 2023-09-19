file_in='input.txt'
with open(file_in, 'r') as f:
	n=int(f.readline())
	m=int(f.readline())
	arr=[]
	for i in range(n):
		arr_s=list(map(int,f.readline().split()))
		arr.append(arr_s)
	x=int(f.readline())
	y=int(f.readline())
output=[]
if x>=1:
	output.append(arr[x-1][y])
if x<n-1:
	output.append(arr[x+1][y])
if y>=1:
	output.append(arr[x][y-1])
if y<m-1:
	output.append(arr[x][y+1])
print(" ".join(map(str,sorted(output))))
