# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 17:57:42 2021

Definēt funkciju devides_evenly, kurai ir divi parametri: veseli skaitļi a un b. Funkcija
atgriež True, ja a var izdalīt ar b bez atlikuma. Pretējā gadījumā funkcija atgriež False
"""

def devides_evenly(x=0,y=0):
    if x % y == 0:
        return True
    else:
        return False
    
if devides_evenly(int(input("Enter the 1st number: ")), int(input("Enter the 2nd number: "))):
    print("Devides evenly!")
else:
    print("Does not devide evenly!")
    