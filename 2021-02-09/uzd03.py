# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:00:44 2021

@author: antons.sincovs

Doti divi saraksti ar garumiem m un n. Aizpildīt tos ar gadījuma skaitļiem no intervāla
[𝑎; 𝑏] (𝑚 < 𝑏 − 𝑎 − 5, 𝑛 < 𝑏 − 𝑎 − 5) tā, ka katrs skaitlis atkārtojas tikai vienu reizi.
Izmantojot saraksta ģenerēšanu, izveidot sarakstu, kas sastāv no elementiem, kas ir abos
sarakstos. Izveidotajā sarakstā elements parādās tikai vienu reizi
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

sar_rez = []

for elem in sar_m:
    if elem in sar_n:
        sar_rez.append(elem)
        
print(sar_rez)

sar_rez_02 = [elem for elem in sar_n if elem in sar_m]
print(sar_rez_02)
