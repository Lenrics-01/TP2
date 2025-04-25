with open("data/journal.txt", "r", encoding="utf-8") as fichier:
    file=fichier.readlines()
for i, ligne in enumerate(file): 
     print(f"Ligne {i+1} : {ligne}")