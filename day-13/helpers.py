def gcf(num1, num2):
	num1_factors = set()
	for i in range(1, num1+1):
		if num1 % i == 0:
			num1_factors.add(i)

	num2_factors = set()
	for i in range(1, num2+1):
		if num2 % i == 0:
			num2_factors.add(i)


	return max(num1_factors & num2_factors)



def lcm(num1, num2):
	print('calculating lcm')
	return int((num1 * num2) / gcf(num1, num2))


