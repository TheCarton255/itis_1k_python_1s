def to_grade(score: int) -> str:
    """Переводит балл 0-100 в оценку."""
    if score >= 86:
        return "Отлично"
    elif score >= 71: #при строгом диапозоне 71 будет входить в удовлетворительно
        return "Хорошо"
    elif score >= 56:
        return "Удовлетворительно"
    else:
        return "Неудовлетворительно"


def count_grades(scores: list[int]) -> dict[str, int]:
    """Считает, сколько раз встречается каждая оценка."""
    counts = {}
    for s in scores:
        grade = to_grade(s)
        counts[grade] = counts.get(grade, 0) + 1 #сначало из-за того что counts[grade] ещё нет а потом только записать поэтому появляется KeyError
    return counts


def main() -> None:
    """Считывает баллы и печатает статистику."""
    raw = input("Баллы через пробел: ")
    scores = [int(x) for x in raw.split()] #сравнивает str и int  чего не может быть
    print(count_grades(scores))
    print("Средний балл:", sum(scores) / len(scores))


main()