try:
    with open("songs.txt", "r", encoding="utf-8") as file:
        for line in file:
            song_name, artist_name = line.strip().split(";")
            print(song_name, "-", artist_name)
except FileNotFoundError:
    print("Файл не найден:")

new_song = input("Новая песня: ")

try:
    with open("songs.txt", "a", encoding="utf-8") as file:
        file.write("\n" + new_song)
except FileNotFoundError:
    print("Файл не найден:")