file_in='input.txt'
with open(file_in, 'r') as f:
	decimal=int(f.readline().strip())
if decimal>0:
	integer=decimal
	binary=''
	while integer>0:
		remain = integer % 2
		binary = str(remain) + binary
		integer = integer // 2
else:
	binary='0'

print(binary)