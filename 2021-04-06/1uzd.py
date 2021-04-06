# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:48:35 2021

@author: antons.sincovs
"""
import csv

with open('countries_1.csv') as f:
    csv_reader1 = csv.reader(f, delimiter='|')
    for row in csv_reader1:
        print(row)

with open('countries_2.csv') as f:
    csv_reader2 = csv.reader(f, delimiter=' ', quotechar="'")
    for row in csv_reader2:
        print(row)
        
with open('countries_1.csv') as f:
 dict_reader1 = csv.DictReader(f, delimiter='|', quotechar="'")
 for row in dict_reader1:
     print(dict(row))


with open('countries_2.csv') as f:
 dict_reader2 = csv.DictReader(f, delimiter=' ', quotechar="'")
 for row in dict_reader2:
     print(dict(row))
