# -*- coding: utf-8 -*-
"""
1. uzdevums
Uzrakstīt Python skriptu, kas veic šādas darbības:
1) Nolasa failu month.txt tā, lai tiktu izveidots saraksts ar mēnešu nosaukumiem,
kur katrs mēneša nosaukums ir virkne, kas nesatur jaunas rindas rakstzīmi.
2) Sakārtot mēnešus alfabētiskā secībā un ierakstīt sakārtoto sarakstu failā.
Sākotnējo sarakstu neizmainīt.
3) Failā morse.py ierakstīta vārdnīca, kas veido Morzes kodu. Iekļaut šo failu
Python skriptā.
4) Izvadīt visu mēnešu nosaukumus, izmantojot Morzes kodu, starp katru kodēto
rakstzīmi izvada vienu atstarpes simbolu. Katru kodēto mēneša nosaukumu
izvada jaunā rindā.

"""
from morse import morse

f  = open("Months.txt","r")
line = f.readline()
months = []
while line:
    months.append(line.upper())
    line = f.readline()
f.close()

months.sort()

f = open("months_sorted.txt", "w")
f.writelines(months)
f.close()

f  = open("months_sorted.txt","r")
line = f.readline()
months = []
while line:
    months.append(line.strip())
    line = f.readline()
f.close()

print("Dipslaying Morse..")
for elem in months:
    for letter in elem:
        print(morse[letter.upper()], end=" ")
    print()


