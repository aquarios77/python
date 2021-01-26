"""
Created on Tue Jan 26 18:59:37 2021

@author: antons.sincovs
"""

number = int(input("Enter int n: "))
sum = 0

for i in range(1, number + 1):
    sum+=i**3
print(sum)