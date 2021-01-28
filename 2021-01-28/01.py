# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 18:54:34 2021

@author: antons.sincovs
"""

phrase = input("Enter a phrase of 2 words: ")
break_point = phrase.find(' ')
reverse_phrase = phrase[break_point+1:] + ' ' + phrase[:break_point]
print(reverse_phrase)