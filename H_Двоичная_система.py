file_in='input.txt'
with open(file_in, 'r') as f:
	number1=f.readline().strip()
	number2=f.readline().strip()
sum=''
len1=len(number1)
len2=len(number2)
remain='0'
for i in range(max(len1,len2)):
	digit1='0'
	digit2='0'
	if i<len1:
		digit1=number1[len1-1-i]
	if i<len2:
		digit2=number2[len2-1-i]
	arr=''.join(sorted([remain, digit1, digit2]))
	if arr=='000':
		sum='0'+sum
		remain='0'
	if arr=='001':
		sum='1'+sum
		remain='0'
	if arr=='011':
		sum='0'+sum
		remain='1'
	if arr=='111':
		sum='1'+sum
		remain='1'
if remain=='1':
	sum='1'+sum
print(sum)