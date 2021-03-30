# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:08:43 2021

@author: antons.sincovs
"""

def is_int(check):
    try:
        isinstance(int(check), int)
        return True
    except:
        return False

while True:

    print(is_int(input("Enter a symbol (or ctrl+c to quit) ==> ")))