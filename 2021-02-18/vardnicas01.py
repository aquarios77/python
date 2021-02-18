# -*- coding: utf-8 -*-
"""
Uzrakstīt funkciju char_frequency(), kurai ir viens parametrs – virkne. Funkcija atgriež
vārdnīcu ar rakstzīmju atkārtojumu skaitu virknē.
virkne = 'wawbbebacdagab'
print(char_frequency(virkne))
Rezultāts
{'a': 4, 'b': 4, 'c': 1, 'd': 1, 'e': 1, 'g': 1, 'w': 2}

"""
my_str = input("Enter a string:")
my_arr = list(my_str)

unique = set(my_arr)
dic = {}

for elem in unique:
    if elem in my_arr:
        dic[elem] = my_arr.count(elem)

print(dic)

'''
def char_frequency_2(virkne):
    #sar = sorted(set(virkne))
    vardnica = {elem : virkne.count(elem) for elem in sorted(set(virkne))}
    return vardnica
'''