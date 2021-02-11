# -*- coding: utf-8 -*-
"""
1) Definēt divas virknes (str) (virkņu saturs nav noteikts, tas atkarīgs no
programmētāja izvēles, tomēr vēlams izveidot pēc iespējas garākas virknes). Izvadīt
tās.
2) Pārveidot šīs virknes par kopām (klases set objektiem) tā, ka katrs burts ir viens
kopas elements. Izvadīt tās.
3) Izmantojot klases set funkcijas vai operatorus, iegūt jaunas kopas, pielietojot
iepriekš definētajām kopām šādas kopu operācijas: apvienojums, šķēlums, starpība,
simetriskā starpība.
4) Izveidot kopas no vārdiem, kas ir dotajās virknes.
5) Pielietot vārdu kopām šādas kopu operācijas: apvienojums, šķēlums, starpība,
simetriskā starpība.
"""

s01 = "some text goes here"
s02 = "not everyone loves apples"

print("String 01: " , s01)
print("String 02: " , s02)

kopa01_words = s01.split(" ")
kopa01_words = set(kopa01_words)
kopa01_letters = set(s01)

kopa02_words = s02.split(" ")
kopa02_words = set(kopa02_words)
kopa02_letters = set(s02)

union_letters = kopa01_letters | kopa02_letters
crossing_letters = kopa01_letters & kopa02_letters

print("Kopa 01 letters: " , kopa01_letters)
print("Kopa 01 words: " , kopa01_words)
print("Kopa 01 : " , kopa01_words)