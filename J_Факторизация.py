file_in='input.txt'
with open(file_in, 'r') as f:
	number=int(f.readline().strip())
output=[]
simple = 2
limit = 
while number_set and number>1:
	min_number = min(number_set)
	while number % min_number == 0:
		number = number // min_number
		output.append(min_number)
	number_set -= set(range(min_number, number+1, min_number))
print(' '.join(map(str,output)))
