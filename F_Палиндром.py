file_in='input.txt'
with open(file_in, 'r') as f:
	text=f.readline().strip()
clean_text=''
for symbol in text:
	if symbol.isalnum():
		clean_text += symbol.lower()
i=0
j=len(clean_text)-1
if j==0:
	output = True
else:
	output=False
while i<j and clean_text[i]==clean_text[j]:
	i+=1
	j-=1
	if i>=j:
		output=True
print(output)
