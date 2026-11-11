from datetime import datetime

DAYS = ["понедельник", "вторник",
        "среда", "четверг", "пятница",
        "суббота", "воскресенье"]

text = input("Дата рождения (ДД.ММ.ГГГГ): ")
birth_day = datetime.strptime(text, '%d.%m.%Y')

date_now = datetime.now()
print("Вы родились: ", DAYS[bith_day.weekday()])
print("Прожито дней: ", (datetime.now() - birth_day).days)

birth = datetime(date_now.year, birth_day.month, birth_day.day)
if birth < date_now:
    print("До дня рождения: ",(datetime(date_now.year + 1, birth.month, birth.day) - date_now).days)
else:
    print("До дня рождения: ",(birth_day - date_now).days)