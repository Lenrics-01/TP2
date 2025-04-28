import csv
donnée=[
   ["Nom","Note"],
   ["Alice",90],
   ["Bob",72],
   ["Chloe",88]
 ]
with open('data/notes.csv', "w", encoding="utf-8", newline='') as f:
  writer=csv.writer(f, delimiter=",")
  writer.writerows(donnée)

choix=input(int("faite votre choix:\n 1- ajouter des donnée\n 2- ne pas ajouter une donnée\n"))

if choix==1:
  new=[]
  i=input(int("Le nombre de donnée à ajouter:"))
  for b in range(i):
   nom=input("Nom:")
   note=input(float("Note:"))
   données=[nom, note]
   new.append(données)
  with open("data/notes.csv", "a", newline="", encoding="utf-8") as f:
    writer=csv.writer(f, delimiter=",")
    writer.writerows(new)
if choix==2:
  exit("Bonne journéé!")
