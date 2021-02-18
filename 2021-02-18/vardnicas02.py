# -*- coding: utf-8 -*-
"""
Uzrakstīt programmu, kas simulē 1000 divu spēļu kauliņu metienus.
Definēt funkciju, kurai nav parametru. Funkcija simulē divu spēļu kauliņu metienu.
Funkcija atgriež ar diviem spēļu kauliņiem uzmesto punktu summu.
Galvenā programma izmanto definētu funkciju, lai simulētu 1000 divu spēļu kauliņu
metienus. Programma saskaita, cik reizes tiek uzmesta katra no iespējamām vērtībām
(divu kauliņu summa).
Programma izvada rezultātu izteiktu procentos. Programma izvada arī katras summas
teorētiski aprēķināto varbūtību (saskaņā ar varbūtību teoriju).
"""
import random
def metiens():
    return (random.randint(1,6)) + (random.randint(1,6))

vis_komb = [k1 + k2 for k1 in range(1,7) for k2 in range(1,7)]
my_dic = {}

for elem in vis_komb:
    my_dic[elem] = 0

n = 1000

'''
for i in range(n):
    my_dic[metiens()] += 1
'''
print(my_dic)

'''
# 2. uzdevums - kaulinju mesana
========
import random

def metiens():
    return (random.randint(1, 6) + random.randint(1, 6))

summas = [k1 + k2 for k1 in range(1, 7) for k2 in range(1, 7)]
print(summas)
unik_summas = set(summas)
print(unik_summas)

n = 1000

fakt_uzmesto_summu_skaits = {s:0 for s in unik_summas}
for i in range(n):
    s = metiens()
    fakt_uzmesto_summu_skaits[s] += 1
print(fakt_uzmesto_summu_skaits)

fakt_uzmesto_summu_proc = {s:0 for s in unik_summas}
for s in unik_summas:
    fakt_uzmesto_summu_proc[s] = round(fakt_uzmesto_summu_skaits[s] / n * 100,2)
    
print(fakt_uzmesto_summu_proc)
'''