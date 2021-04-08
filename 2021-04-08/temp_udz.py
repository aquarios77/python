import csv

sem_li = []

with open('temperaturas_2021.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    for row in csv_reader:
        sem_li.append(row)
        
days = {}

for day in sem_li[1:]:
    days[day[0]] = (sum([float(temp) for temp in day[1:]])/len(day[1:]))  
    
print(days)
    