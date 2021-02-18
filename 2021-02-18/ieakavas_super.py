# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 17:48:08 2021

@author: antons.sincovs
"""


atverosas = '([{'
aizverosas = ')]}'
iekavu_virkne = input("ievadi iekavu virkni ==>")
iekavu_saraksts = [] # kur liekam ieksha vai njemam ara parus

for elem in iekavu_virkne:
    if elem in atverosas:
        iekavu_saraksts.append(elem)
    elif elem in aizverosas:
        index = aizverosas.index(elem)
        if atverosas[index] in iekavu_saraksts:
            iekavu_saraksts.remove(atverosas[index])
if len(iekavu_saraksts) == 0:
    print("Iekavas pareizas!")
else:
    print("Iekavas nepareizas!")