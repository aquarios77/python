# -*- coding: utf-8 -*-
"""
Definēt funkciju, kurai ir viens parametrs – saraksts ar kvadrātvienādojuma
koeficientiem. Funkcija atgriež sarakstu ar kvadrātvienādojuma saknēm. Ja
kvadrātvienādojumam nav reālu sakņu, funkcija atgriež None.
Pārbaudīt funkcijas darbību Python skriptā.
"""

def kvadrat_solver(li):
    d = (li[1]**2 - 4*li[0]*li[2])

    if(d>=0):
        x1 = (-li[1] + d**0.5)/(2*li[0])
        x2 = (-li[1] - d**0.5)/(2*li[0])
        return([x1 , x2])
    else:
        return None
    
print(kvadrat_solver([1 , -8 , 12]))