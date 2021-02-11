# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:42:07 2021

@author: antons.sincovs
Doti divi saraksti ar garumiem m un n. Aizpildīt tos ar gadījuma skaitļiem no intervāla
[𝑎; 𝑏] (𝑚 < 𝑏 − 𝑎, 𝑛 < 𝑏 − 𝑎).
Izmantojot saraksta ģenerēšanu, izveidot sarakstu, ar elementu pāriem, kas sastāv no
elementiem, kas ir abos sarakstos. Izveidotajā sarakstā var būt vairāki vienādi elementu
pāri, tomēr viens un tas pats elementu pāris divas reizes netiek ierakstīts.

"""
import random

n = 5
m = 7

a = 1
b = 15

sar_n = []
sar_m = []

sar_n = random.sample(range(a, b + 1) , n)
print("Random element list: ", sar_n)

sar_m = random.sample(range(a, b + 1) , m)
print("Random element list: ", sar_m)

sar_par = [(x , y) for x in sar_n for y in sar_m if x == y]
print("Random element list: ", sar_par)