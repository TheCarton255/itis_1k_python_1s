def average(scores):
    total = 0
    for s in scores:
        total += s
    return total / len(scores)

def best_student(journal):
    best_name = ""
    best_avg = 0
    for name in journal:
        avg = average(journal[name])
        if avg > best_avg:
            best_name = name
            best_avg = avg
    return best_name, best_avg

journal = {"Иванов": [8, 9, 7],
            "Петрова": [10, 10, 9],
            "Сидоров": [5, 6, 4]}
name, avg = best_student(journal)
print(f"Лучший: {name} ({avg:.2f})")