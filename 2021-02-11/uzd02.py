# -*- coding: utf-8 -*-
"""
Definēt funkcijas:
1) difference_max_min, kurai ir viens parametrs - saraksts (list). Funkcija atgriež
saraksta lielākās un mazākās vērtības starpību
2) max_min, kurai ir viens parametrs - saraksts (list). Funkcija atgriež sarakstu ar
lielāko un mazāko vērtību
Funkciju difference_max_min un max_min izsaukšanas piemēri:
"""
def difference_max_min(list01):
    return ( max(list01) - min(list01) )

def max_min(list01):
    return ([max(list01) , min(list01)])

list01 = [1 , 2 , 3 , 4]

print (difference_max_min(list01))
print (max_min(list01))
