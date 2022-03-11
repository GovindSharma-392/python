a = int(input('enter a number'))
count = 0
i = 1
while i<=a:
	if a%i == 0:
		count+=1
	i+=1
if count == 2:
	print('prime')
else:
	print('not prime')
