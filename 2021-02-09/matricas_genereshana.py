# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 17:57:59 2021

@author: antons.sincovs
"""
import random

#generate matrix with m rows and n columns (m x n)
m = 3 # row number
n = 4 # column number
matrix = []
for i in range (m):
    row = []
    for k in range (n):
        row.append(0)
    matrix.append(row)

print(matrix)
print()


# generate the same matrix with generator
matrix_02 = [[random.randint(1,6) for col in range(n)] for row in range(m)] # internal expression [random.randint(1,6) for col in range(n)] is repeated x row times
print(matrix_02)

# matrix_02 elements put into the list

saraksts = []
for row in matrix_02: # you take each element (3 lists) which is a list of 4 elements
    for elem in row:
        saraksts.append(elem)
print("Saraksts: ", saraksts)

# matrix_02 elements put into the list be means of generator
saraksts_02 = []

saraksts_02 = [[elem for row in matrix_02] for elem in row]
print(saraksts_02)
    