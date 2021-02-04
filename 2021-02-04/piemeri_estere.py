# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 20:53:57 2021

@author: antons.sincovs
"""

# Esttere piemeri ar saraksta generatoru
# izveidot sarakstu ar skaitlju no 1 liidz n kvadratiem
n = 10
saraksts = []
for i in range(1, n + 1):
    saraksts.append(i ** 2)
    
saraksts_2 = [i ** 2 for i in range(1, n + 1)]

print(saraksts)
print(saraksts_2)

# izveidot sarakstu ar paara skaitlju no 1 liidz n kvadratiem
saraksts_3 = []
for i in range(1, n + 1):
    if not i % 2:
        saraksts_3.append(i ** 2)
        
saraksts_4 = [i ** 2 for i in range(1, n + 1) if not i % 2]
print(saraksts_3)
print(saraksts_4)

# sarsksts ar skaitljiem, kas nedalas ar 2 un dalaas ar 5
n = 100
saraksts_4 = [i for i in range(1, n + 1) if i % 2 if not i % 5]
saraksts_5 = [i for i in range(1, n + 1) if i % 2 != 0 if i % 5 == 0]
saraksts_6 = [i for i in range(1, n + 1) if (i % 2 != 0 and i % 5 == 0)]
saraksts_7 = [i for i in range(1, n + 1) if (i % 2 != 0 and i % 5 == 0) or i % 7 == 0]
print(saraksts_7)

# ja skaitlis dalaas ar 5, tad pievienoja skaitja kvadratu, preteejaa gadiijumaa pasu skaitli
n = 25
saraksts_8 = []
for i in range(1, n + 1):
    if not i % 5:
        saraksts_8.append(i ** 2)
    else:
        saraksts_8.append(i)
saraksts_9 = [i ** 2 if not i % 5 else i for i in range(1, n + 1)]
print(saraksts_8)
print(saraksts_9)

