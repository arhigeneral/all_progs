def total(initial=5, *numbers, **keywords):
	count = initial
	for number in numbers:
		print('Это число номер',numbers)
		count += number
	for key in keywords:
		print('Это число номер',keywords)
		count += keywords[key]
	return count
print(total(10, 1, 2, 3, 4, vegetables=50, fruits=100, others=20))