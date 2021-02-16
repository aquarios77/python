# -*- coding: utf-8 -*-
"""
Dota skaitļu secība, secības garums iepriekš nav zināms. Nolasīt to. Katram skaitlim
secībā noteikt, vai šis skaitlis jau ir bijis vai nē – izvadīt “YES”, ja šis jau ir bijis, izvadīt
“NO”, ja šis skaitlis vēl nav bijis.
Lai nolasītu skaitļu secību un to pārveidotu par sarakstu, izmanto metodi split:
skaitli = input().split()
Lai nolasītos skaitļus pārveidotu uz skaitlisku datu tipu (int), izmanto saraksta
ģenerēšanu.
skaitli = [int(s) for s in input().split()]
Pēc tam pārstaigā sarakstu un izvada prasīto. Katru vārdu izvada jaunā rindā
"""

arr = [int(i) for i in input().split()]

test_arr = []

for elem in arr:
    if elem in test_arr:
        print("YES")
    else:
        print("NO")
        test_arr.append(elem)