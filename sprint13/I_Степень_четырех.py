file_in='input.txt'
with open(file_in, 'r') as f:
	number=int(f.readline().strip())
output=True
while number>1:
	if number%4 != 0:
		output=False
		break
	else:
		number = number // 4
print(output)
