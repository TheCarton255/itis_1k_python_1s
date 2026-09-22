def detect_type(value: str):
	value = value.strip()
	if value.lower() in ('true', 'false'):
		return value.lower == 'true', bool
	if value.lstrip('-').isdigit():
		return int(value), int
	try:
		return float(value), float
	except ValueError:
		return value, str

while True:
	num = input("Введите значение: ").strip()
	if num.lower() == 'стоп':
		print("Пока!")
		break
	value, val_type = detect_type(num)
	print(f"{num} -> {val_type}")