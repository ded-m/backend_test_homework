file_in='input.txt'
with open(file_in, 'r') as f:
	len_num1=int(f.readline().strip())
	list_num1=list(map(int,f.readline().split()))
	num2=f.readline().strip()
output=[]
list_num2=list(map(int,list(num2)))
len_num2=len(list_num2)
remain=0
for i in range(max(len_num1,len_num2)):
	digit1=0
	digit2=0
	if i<len_num1:
		digit1=list_num1[len_num1-1-i]
	if i<len_num2:
		digit2=list_num2[len_num2-1-i]
	sum = remain + digit1 + digit2
	output = [sum%10,] + output
	remain = sum // 10
if remain>0:
	output = [remain,] + output
print(' '.join(map(str,output)))
