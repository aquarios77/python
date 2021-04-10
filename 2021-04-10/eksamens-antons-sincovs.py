# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 10:16:57 2021

@author: antons.sincovs
"""

from soma import Soma
from random import randint
from random import choice
from prece import Prece 
import csv

def all_bags_full(bags):
    for bag in bags:
        if bag.vai_tuksa():
            return False 
        else:
            return True    

prece_li = [] # list for <Prece> objects


# 3.2.1 Reading from CSV and printing out a list with <Prece> objects read from the file      
print('======= 3.2.1 ================')
with open('preces_cenas.csv') as f:
    csv_reader = csv.reader(f, delimiter=';') # reading the csv file
    for row in csv_reader:
        prece_li.append(Prece(row[0],float(row[1]))) # creating <Prece> objects and appending them the object list
        
print(prece_li)

print("=============================")
#==========================================================================================================

# 3.2.2.
print('======= 3.2.2 ===============')
soma_li = [] # list for <Soma> objects
for i in range(5):
    soma_li.append(Soma(('Bag #' + str(i)), randint(1, 5)))

print(soma_li)

print("=============================")
#==========================================================================================================

# 3.2.3.
for soma in soma_li:
    while not soma.vai_pilna():
        soma.ielikt(choice(prece_li))
        
        
#==========================================================================================================
print('======= 3.2.3 - 3.2.4 =======')
# 3.2.4.

for soma in soma_li:
    print(soma)
    print(soma.ka_mani_sauc() + ":summa " + str(round(soma.summa() , 2)) + " EUR")

print("=============================")  
#==========================================================================================================
print('======= 3.2.5 ===============')
# 3.2.5.

print("Total sum: " + str(round(sum([soma.summa() for soma in soma_li]) , 2)) + " EUR")
print("=============================")
#==========================================================================================================
print('======= 3.2.6 ===============')
# 3.2.6.

soma_li[0].bag_swap(soma_li[1])
for soma in soma_li:
    print(soma)

print("=============================")      
#==========================================================================================================
print('======= 3.2.7 ===============')
# 3.2.7.
for soma in soma_li:
    soma.iznemt()

for soma in soma_li:
    print(soma)  
print("=============================")
#========================================================================================================== 
print('======= 3.2.8 ===============')
# 3.2.8.
soma_li[-1].iztukshot()

for soma in soma_li:
    print(soma)  
print("=========END=================") 

