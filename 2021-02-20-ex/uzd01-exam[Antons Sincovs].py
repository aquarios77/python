# -*- coding: utf-8 -*-
"""
Pieņemsim, ka sportistam ir mērķis dienā noskriet x kilometrus. 
Pirmajā dienā viņš noskrien y
kilometrus, katrā nākamajā dienā par 10 procentiem vairāk nekā iepriekšējā. 
Noskaidrot, cik dienās
viņš sasniegs savu mērķi.
Programma prasa ievadīt mērķi – kilometru skaitu un 
treniņu pirmajā dienā plānoto kilometru
skaitu.
Programma izvada treniņu plānu – katru dienu noskrienamo kilometru skaitu,
 līdz tiks sasniegts
mērķis.
Programma izvada, kurā dienā, sākot no pirmās, mērķis tiks sasniegts.
"""

start = int(input())
finish = int(input())

n = 1
result = start

while finish > result:
    print("*"*15, "Day ", n , "*"*15)
    print(" "*3 , "You have to run:", round(result, 2), "km")
    print("*"*38)
    result *= 1.1
    n+=1
    
print("*"*15, "Day ", n , "*"*15)
print(" "*3 , "You have to run:", finish, "km")
print("*"*38)  

print("Your goal of", finish , "km will be reached in" , n , "days")


