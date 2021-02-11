# -*- coding: utf-8 -*-
"""
Definēt funkciju word_value, kas aprēķina vārda „vērtību”. Vārdam jābūt uzrakstītam,
izmantojot latīņu alfabēta burtus.
Vārda vērtību nosaka, summējot visus vārdā esošo burtu kārtas skaitļus alfabētā,
nešķirojot lielos un mazos burtus. Piemēram, burtu ‘A’ un ‘a’ kārtas skaitlis ir 1,
savukārt burtu ‘D’ un ‘d’ kārtas skaitlis ir 4.
"""
import string
def word_value(word):
    sum_of_in = 0
    low = string.ascii_lowercase
    word = word.lower()
    for letter in word:
        print("Letter \"", letter , "\"", sep="", end="")
        sum_of_in += low.index(letter) + 1
        print(" index is: ", low.index(letter) + 1)
    return sum_of_in

print("Sum of letter positions is: ", word_value('cloud'))
    