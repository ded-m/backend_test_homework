file_in='input.txt'
with open(file_in, 'r') as f:
	str1=f.readline().strip()
	str2=f.readline().strip()
output=''
list1=sorted(list(str1))
list2=sorted(list(str2))
for i in range(len(str1)):
	if list1[i]!=list2[i]:
		output=list2[i]
		break
if output=='':
	output=list2[-1]
print(output)
