import json
import csv

with open('data.json','r') as f, open('resultat.csv','w',newline='') as c:
    data = json.load(f)
    ecriture = csv.writer(c)
    ecriture.writerow(['reel', 'imaginaire'])
    for el in data:
        ecriture.writerow(el)
