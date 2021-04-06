# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:19:25 2021

@author: antons.sincovs
"""
import csv

with open('innovators.csv') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)
        
print(csv_reader)
print(type(csv_reader))