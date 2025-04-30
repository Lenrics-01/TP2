import numpy as np
import json
import csv

data = np.loadtxt("data/responses.csv", delimiter=",", skiprows=1, usecols=2)
print(data)
print("la moyenne est de :", np.mean(data))
print("la mediane est de :", np.median(data))
p=[]
for i in data:
  if i>=4:
    p.append(i)
print("le pourcentage de notes supérieures ou égales à 4 est:", sum(p)*100/sum(data),"%") 
    
if np.mean(data)<3:
  donnée={
  "alerte": true,
  "moyenne": 2.6,
  "seuil": 3.0,
  "message": "Satisfaction étudiante anormalement basse"
  }

  with open("data/alerte.json", "w", encoding="utf-8") as f:
    json.dump(donnée, f, ensure_ascii=False, indent=2)
else:
  print("rien ne se créér")   

