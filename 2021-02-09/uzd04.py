# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 19:34:10 2021

@author: antons.sincovs

Ģenerēt sarakstu ar kortežiem visām iespējamām divu metamo kauliņu uzmestām
vērtībām.
[(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (3, 1), (3, 2), (3,
3), (3, 4), (3, 5), (3, 6), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5),
(5, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]

"""

cub01 = [1, 2, 3, 4, 5, 6 ]
cub02 = [1, 2, 3, 4, 5, 6 ]
cub_2_cub = [[c1, c2] for c1 in cub01 for c2 in cub02]

print(cub_2_cub)

vertibas = list(range(1 , 7))

s1 = [(x, y) for x in vertibas for y in vertibas]

'''
4.2. Ģenerēt sarakstu ar kortežiem visām iespējamām divu metamo kauliņu uzmestām
vērtībām, kuru summa ir lielāka par 7.
'''
s2 = [(x , y) for x in vertibas for y in vertibas if x + y > 7]
print(s2)

