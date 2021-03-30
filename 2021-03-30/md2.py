# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 19:23:31 2021

@author: antons.sincovs
"""

def is_int(s):
   try:
      s = int(s)
      return s
   except:
        try:
            s = float(s)
            return s
        except:
            return s

while True:

    print(is_int(input("Enter a symbol (or ctrl+c to quit) ==> ")))