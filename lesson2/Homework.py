number = int(input("Введите основание треугольника: "))
if number % 2 == 0:
	number += 1

for i in range((number + 1) // 2):
	count = 2 * i + 1
	spaces = (number - count) // 2
	print(' ' * spaces + '*' * count)