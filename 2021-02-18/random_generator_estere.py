# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 18:57:09 2021

@author: antons.sincovs
"""

# Estere Kaulinju simulaacija
    # 2. uzdevums
import random

def divu_kaulinu_summma():
    return (random.randint(1, 6) + random.randint(1, 6))

# aprekina divu kaulinju uzmesto punktu varbutibu

kaulinu_summas = [k1 + k2 for k1 in range(1, 7) for k2 in range (1, 7)]
print(kaulinu_summas)

skaits = len(kaulinu_summas)
unik_kaulinu_summas = set(kaulinu_summas)
summu_skaits = {}
for s in unik_kaulinu_summas:
    summu_skaits[s] = kaulinu_summas.count(s)
print(summu_skaits)

# ieraksta vardnicaa divu kaulinju uzmesto punktu varbutibu
summu_procents = {}
for s in unik_kaulinu_summas:
    summu_procents[s] = round(summu_skaits[s] / skaits * 100, 2)
print(summu_procents)

# kaulinju mesanas simulaacija
# n = 1000 metienu skaits
n = 1000 

# visu uzmesto punktu summa
summa = 0

# veido vardnicu ar uzmesto punktu summam
fakt_summu_skaits = {s:0 for s in unik_kaulinu_summas}
print(fakt_summu_skaits)
for i in range(n):
    s = divu_kaulinu_summma()
    fakt_summu_skaits[s] += 1
print(fakt_summu_skaits)

# veido vardnicu ar uzmesto punktu summu procentiem
fakt_summu_procents = {s:round(fakt_summu_skaits[s] / n * 100, 2) for s in unik_kaulinu_summas}
print(fakt_summu_procents)    

# izvada rezultatu
print("Summa  Simulācija  Aprēkināts")
for s in unik_kaulinu_summas:
    print(f"{s:3d} {fakt_summu_procents[s]:10.2f}% {summu_procents[s]:10.2f}%")

    