import csv
with open("data/notes.csv", "r", encoding="utf-8", newline='') as f:
    lecteur=csv.reader(f)
    next(lecteur)
    for ligne in lecteur:
        print(f"{ligne[0]} a obtenu {ligne[1]}")