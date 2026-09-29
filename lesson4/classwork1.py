def is_prime(n: int) -> bool:
	if n < 2:
		return False
	for i in range(2, int(n ** 0.5) + 1):
		if n % i == 0:
			return False
	return True

def digit_sum(n: int) -> int:
	total = 0
	for digit in str(abs(n)):
		total = total + int(digit)
	return total

def reverse_number(n: int) -> int:
	reversed_str = str(abs(n))[::-1]
	result = int(reversed_str)
	if n < 0:
		return -result
	else:
		return result

def max_of_list(numbers: list[int]) -> int:
	if len(numbers) == 0:
		return None
	maximum = numbers[0]
	for num in numbers:
		if num > maximum:
			maximum = num
	return maximum

def count_even(numbers: list) -> int:
	count = 0
	for num in numbers:
		if num % 2 == 0:
			count += 1
	return count

def read_int(prompt: str) -> int:
	value = input(prompt)
	return int(value)

def read_int_list(prompt: str) -> list:
	line = input(prompt)
	parts = line.split()
	numbers = []
	for part in parts:
		numbers.append(int(part))
	return numbers

def main() -> None:
	while True:
		print("1 - простое ли число")
		print("2 - сумма цифр")
		print("3 - перевернуть число")
		print("4 - максимум списка")
		print("5 - количество чётных")
		print("0 - выход")

		choice = input("Выберите действие:")
		if choice == "0":
			print("Пока!")
			break
		elif choice == "1":
			n = read_int("Введите число:")
			if is_prime(n):
				print(f"{n} - простое")
			else:
				print(f"{n} - не простое")
		elif choice == "2":
			n = read_int("Введите число:")
			result = digit_sum(n)
			print(f"Сумма цифр: {result}")
		elif choice == "3":
			n = read_int("Введите число:")
			result = reverse_number(n)
			print(f"Результат: {result}")
		elif choice == "4":
			n = read_int("Введите число:")
			result = max_of_list(n)
			print(f"Максимум: {result}")
		elif choice == "5":
			numbers = read_int_list("Введите числа:")
			result = count_even(numbers)
			print(f"Количество чётных: {result}")
		else:
			print("Неверный ввод. Попробуйте снова.")
main()