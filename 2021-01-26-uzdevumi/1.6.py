"""
Created on Tue Jan 26 18:59:37 2021

@author: antons.sincovs
"""

number = int(input("Enter int n: "))
sum = 0
fakt = 1

for i in range(1, number + 1):
    for k in range(1, i + 1):
        fakt *= k
    sum += fakt
    fakt=1
print(sum)