import random
number = random.randint(1, 100)
attempt = 0
print("Отгадай число от 1 до 100")

while True:
	attempt += 1
	num = int(input(f"{attempt}-я попытка: "))
	if num > number:
		print('Много')
	elif num < number:
		print('Мало')
	else:
		print(f'Правильною Я загадал {number}')
		break