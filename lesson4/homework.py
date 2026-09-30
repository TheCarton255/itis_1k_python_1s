def triangle(base: int) -> None:
	if base % 2 == 0:
		base += 1
	for i in range((base + 1) // 2):
		count = 2 * i + 1
		print(' ' * ((base - count) // 2) + '*' count)

def main():
	base = int(input("Введите основание треугольника: "))
	triangle(base)
main()