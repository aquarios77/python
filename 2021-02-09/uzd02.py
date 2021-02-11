# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 18:47:32 2021

@author: antons.sincovs
Doti divi saraksti ar vienādu garumu: n. Pirmo aizpildīt ar gadījuma skaitļiem no
intervāla [𝑎; 𝑏], otru ar nejauši izvēlētiem lielajiem burtiem.
Izmantojot saraksta ģenerēšanu, izveidot sarakstu, kas sastāv no elementu pāriem
(sarakstiem): [𝑥𝑖
, 𝑦𝑖
], kur 𝑥𝑖
ir pirmā saraksta i-tais elements un 𝑦𝑖
ir otrā saraksta i-tais
elements.
"""
import random
import string

n = 5

sar01 = []
sar02 = []

sar01 = [random.randint(1,5) for i in range(n)]
print("Random element list: ", sar01)

alphabet_string_u = string.ascii_uppercase
sar02 = [random.choice(alphabet_string_u) for i in range(n)]
print("Random uppercase letter list: ", sar02)

pair = []

for i in range(n):
    pair.append([sar01[i],sar02[i]])
print(pair)

list01 = [[sar01[i] , sar02[i]] for i in range(n)]
print(list01)

#list_obj = [expression for item in iterable]
