# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:12:18 2021

@author: antons.sincovs
"""

import string
import random
alphabet_string_u = string.ascii_uppercase
alphabet_string_l = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

password = ""

character_set = [alphabet_string_l, alphabet_string_u, digits, special_chars]

for i in range(3):
    password += random.choice(character_set[0])
    password += random.choice(character_set[1])
    password += random.choice(character_set[2])
    password += random.choice(character_set[3])

password = ''.join(random.sample(password, len(password)))

print("Generated password: ", password)