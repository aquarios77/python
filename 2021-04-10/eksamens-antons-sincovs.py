# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:16:57 2021

@author: antons.sincovs
"""

from soma import Soma
from random import randint
from prece import Prece 
import csv

prece_li = [] # list for <Prece> objects


# 3.2.1 Reading from CSV and printing out a list with <Prece> objects read from the file      
with open('preces_cenas.csv') as f:
    csv_reader = csv.reader(f, delimiter=';') # reading the csv file
    for row in csv_reader:
        prece_li.append(Prece(row[0],float(row[1]))) # creating <Prece> objects and appending them the object list
        
print(prece_li)
#==========================================================================================================

# 3.2.2.
soma_li = [] # list for <Soma> objects
for i in range(3):
    soma_li.append(Soma(('Bag #' + str(i)), randint(1, 5)))

print(soma_li)
#==========================================================================================================

# 3.2.3.