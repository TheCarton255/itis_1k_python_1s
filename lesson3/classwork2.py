journal = {
 "Иванов": [8, 9, 7, 10],
 "Петрова": [10, 10, 9, 10],
 "Сидоров": [5, 6, 4, 7],
 "Козлова": [9, 8, 10, 9],
}

def avarange(scores: list[int]) -> float:
	if scores == []:
		return 0.0
	return round(sum(scores) / len(scores), 2)

def rating(journal: dict) -> list
	result = []
