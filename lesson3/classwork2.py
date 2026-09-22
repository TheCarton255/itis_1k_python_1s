journal = {
 "Иванов": [8, 9, 7, 10],
 "Петрова": [10, 10, 9, 10],
 "Сидоров": [5, 6, 4, 7],
 "Козлова": [9, 8, 10, 9],
}

def avarange(scores: list[int]) -> float:
	if not scores:
		return 0.0
	return round(sum(scores) / len(scores), 2)

def rating(journal: dict) -> list[tuple[str, float]]:
	result = []
	for name, scores in journal.items():
		avg = avarange(scores)
		result.append((name, avg))
	result.sort(key = lambda item: item[1], reverse = True)
	return result

def best_student(journal: dict) -> tuple[str, float]:
	return rating(journal)[0]

def unique_scores(journal: dict) -> set[int]:
	result = set()
	for scores in journal.values():
		result.update(scores)
	return result

def add_score(journal: dict, name: str, score: int) -> None:
	if not (0 <= score <= 10):
		print("Ошибка: оценка должна быть от 0 до 10!")
		return
	if name not in journal:
		journal[name] = []
	journal[name].append(score)

def risk_students(journal: dict) -> list[str]:
	result = []
	for name, scores in journal.items():
		if any(score < 5 for score in scores):
			result.append(name)
	return result

print("Рейтинг:")
for i, (name, avg) in enumerate(rating(journal), start=1):
	print(f"{i}. {name} {avg}")

print(f"Лучший: {best_student(journal)}")
print(f"Все оценки: {sorted(unique_scores(journal))}")
print(f"В зоне риска:{risk_students(journal)}")

print("\n--- Проверка add_score ---")
add_score(journal, "", 8)
add_score(journal, "", 11)
print(f"Журнал после изменений:{journal}")

print(f"\n--- Типы промежуточных результатов ---")
print(f"rating: {type(rating(journal))}")
print(f"best_student: {type(best_student(journal))}")
print(f"unique_scores: {type(unique_scores(journal))}")
print(f"add_score: {type(add_score(journal, 'Тест', 5))}")
print(f"risk_students: {type(risk_students(journal))}")
