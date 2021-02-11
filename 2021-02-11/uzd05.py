# -*- coding: utf-8 -*-
"""
Definēt funkciju convert_to_sec, kurai ir trīs parametri: stundas, minūtes un sekundes.
Funkcija pārveido šīs vērtības sekundēs un atgriež attiecīgo vērtību.
Funkcijas otro parametru “minūtes” un trešo parametru “sekundes” definēt ar
noklusētajām vērtībām (0). Tas dos iespēju šo funkciju izsaukt gan ar vienu, gan ar
diviem, gan ar trīs parametriem.
"""
def convert_to_sec(h , m = 0 , s = 0):
    return h * 3600 + m * 60 + s

"""
Definēt funkciju convert_to_hms, kurai ir viens parametrs: sekundes. Funkcija
pārveido sekundes par stundām, minūtēm un sekundēm un atgriež attiecīgās vērtības
(arī ja kāda no tām ir 0).
Tā kā funkcija vienlaikus var atgriezt tikai vienu vērtību, tad šajā gadījumā funkcijai
jāatgriež saraksts (list) vai kortežs (tuple) ar attiecīgajām vērtībām. 
"""
def convert_to_hms(sec):
    h = sec // 3600
    m = (sec - h * 3600) // 60
    s = sec % 60
    return [h , m , s]

print(convert_to_sec(0))
print(convert_to_hms(13500))
