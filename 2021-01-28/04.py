# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 19:07:49 2021

@author: antons.sincovs
"""

import string
alphabet = string.ascii_lowercase
length = len(alphabet)
for i in range (length):
    if(len(alphabet[i:])>=3):
        print(alphabet[i:i+3])