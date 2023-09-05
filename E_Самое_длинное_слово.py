file_in='input.txt'
with open(file_in, 'r') as f:
	n=int(f.readline())
	arr=list(f.readline().strip().split())
output=0
arr_l=[len(_) for _ in arr]
index_max=arr_l.index(max(arr_l))
output=arr[index_max]
print(output)
print(len(output))
