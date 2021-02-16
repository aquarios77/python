# -*- coding: utf-8 -*-
"""
Alisei un Vairim patīk spēlēties ar krāsainiem klucīšiem. Katram bērnam ir savs klucīšu
komplekts, un katrs klucītis ir savā krāsā. Viņi vēlas uzzināt, cik unikālu krāsu var iegūt,
ja apvieno abus klucīšu komplektus.
Lai to noskaidrotu, viņi katru krāsu apzīmēja ar skaitli no 0 līdz 108
.
Jums jāizveido programma, lai palīdzētu bērniem.
Programma vispirms nolasa divus skaitļus m un n, kas atbilst Alises un Vaira klucīšu
skaitam. Nākamās n rindas satur Alises klucīšu krāsu numurus, pēc tam sekojošās m
rindas satur Vaira klucīšu krāsu numurus.
Programma atrod trīs kopas: unikālo krāsu numurus, ko iegūst apvienojot abus klucīšu
komplektus; krāsu numurus, kas ir tikai Alises klucīšu komplektā, krāsu numurus, kas
ir tikai Vaira klucīšu komplektā.
Katrai kopai izvadīt elementu skaitu kopā, kuram uzreiz seko visu kopas klucīšu krāsu
numuri, kas ir sakārtoti augošā secībā.
Katru skaitli izvadīt jaunā rindā.

"""
a, v = [int(i) for i in input().split()]


a_arr = [0]*a
v_arr = [0]*v

for i in range(a):
    a_arr[i] = int(input())

for i in range(v):
    v_arr[i] = int(input())
    
a_set = set(a_arr.sort())
v_set = set(v_arr.sort())


print("Unique union: ", len(a_set.union(v_set)) , a_set.union(v_set))
print("Alice only:" ,len(a_set.difference(v_set)) , a_set.difference(v_set))
print("Vairis only:" , len(v_set.difference(a_set)) , v_set.difference(a_set))