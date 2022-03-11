digit = int(input('enter the num of digits'))
for num in range(10**(digit-1),10**digit):
	num2 = num
	s = 0
	while num > 0:
		x=num%10
		s+= x**digit
		num = num//10
	if num2==s:
		print(num2)
