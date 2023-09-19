file_in='input.txt'
with open(file_in, 'r') as f:
	number=int(f.readline().strip())
output=[]
min_number=2
while min_number**2<=number:
	while number % min_number == 0:
		number = number // min_number
		output.append(min_number)
	min_number+=1
if number>1:
	output.append(number)
print(' '.join(map(str,output)))
