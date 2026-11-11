chat = {}
with open("chat.txt", "r", encoding="utf-8") as file:
    for line in file:
        if ":" not in line:
            continue
        name, text = line.strip().split(":", 1)
        if name not in chat.keys():
            chat[name] = []
        chat[name].append(text)

with open('report.txt', 'w') as file2:
    maximum_count = -1
    max_name = ''
    max_stroka = ''
    max_word = -1

    for key, value in chat.items():
        if len(value) > maximum_count:
            max_name = key
            maximum_count = len(value)
        for t in value:
            word_count = len(t.split())

            if word_count > max_word:
                max_stroka = t
                max_word = word_count
    file2.write(f"Количество сообщений: {max_name} '-' {maximum_count}\n")