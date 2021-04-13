import csv
import matplotlib.pyplot as plt

'''
Get a list of keys from dictionary which has value that matches with any value in given list of values
'''
def getKeysByValues(dictOfElements, value):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == value:
            listOfKeys.append(item[0])
    return  listOfKeys

sem_li = []

with open('temperaturas_2021.csv') as f:
    csv_reader = csv.reader(f, delimiter=';')
    for row in csv_reader:
        sem_li.append(row)
        
days = {}

for day in sem_li[1:]:
    days[day[0]] = (sum([float(temp) for temp in day[1:]])/len(day[1:]))  


 
plt.plot(*zip(*days.items()))
plt.ylabel('Average Temperature')
plt.xlabel('Days')

all_values = days.values()
max_value = max(all_values)
min_value = min(all_values)

for x in getKeysByValues(days , max_value):
    plt.plot(x , max_value, marker = 'o')
    plt.text(x, max_value , round(max_value , 2) , fontsize=7)


for x in getKeysByValues(days, min_value):
    plt.plot(x , min_value, marker = 'o')
    plt.text(x, min_value , round(min_value , 2), fontsize=7)

plt.show()    

print(days)
    