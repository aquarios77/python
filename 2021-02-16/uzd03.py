# -*- coding: utf-8 -*-
"""
Izveidot Python programmu, kas nolasa virkni ar iekavām un pārbauda, vai iekavas ir
pareizi sakārtotas, vai nē.
Iespējamas šādas iekavas: ( ), { }, [ ]
"""        
import time
import sys

my_str = input()
my_ar = []
for i in range(len(my_str)):
    my_ar.append(my_str[i])

c_ar =  ["{","}",0,0]
r_ar =  ["(",")",0,0]
s_ar = ["[","]",0,0]

c_ar[2] , c_ar[3] = my_ar.count(c_ar[0]) , my_ar.count(c_ar[1])
r_ar[2] , r_ar[3] = my_ar.count(r_ar[0]) , my_ar.count(r_ar[1])
s_ar[2] , s_ar[3] = my_ar.count(s_ar[0]) , my_ar.count(s_ar[1])


print(c_ar)
print(r_ar)
print(s_ar)


o_br = 0 # closing bracket pos
c_br = 0 # opening bracket pos



if len(my_ar) % 2 == 0 and c_ar[2] == c_ar[3] and r_ar[2] == r_ar[3] and s_ar[2] == s_ar[3]:
    print("Starting matching...")
    if r_ar[2] != 0:
        for i in range(len(my_ar)): # checking for all round brackets
            if my_ar[i] == r_ar[0]:
                o_br = i
                for z in range(i, len(my_ar)):
                    if my_ar[z] == r_ar[1]:
                        c_br = z
                        print("Found () match! positions:", o_br , c_br )
                        my_ar[i] = ""
                        my_ar[z] = ""
                        time.sleep(1)
                        print("String after elemination: ", ''.join(my_ar))
                        time.sleep(1)
                        break
              
                else:
                        print("No matching closing \")\"")
                        time.sleep(1)
                        print("Exiting...")
                        sys.exit()

    if c_ar[2] != 0:   
        for i in range(len(my_ar)): # checking for all curly brackets
            if my_ar[i] == c_ar[0]:
                o_br = i
                for z in range(i, len(my_ar)):
                    if my_ar[z] == c_ar[1]:
                        c_br = z
                        print("Found {} match! positions:", o_br , c_br )
                        my_ar[i] = ""
                        my_ar[z] = ""
                        time.sleep(1)
                        print("String after elemination: ", ''.join(my_ar))
                        time.sleep(1)
                        break    
                else:
                        print("No matching closing \"}\"")
                        time.sleep(1)
                        print("Exiting...")
                        sys.exit()
  
    if s_ar[2] != 0:   
        for i in range(len(my_ar)): # checking for all square brackets
            if my_ar[i] == s_ar[0]:
                o_br = i
                for z in range(i, len(my_ar)):
                    if my_ar[z] == s_ar[1]:
                        c_br = z
                        print("Found [] match! positions:", o_br , c_br )
                        my_ar[i] = ""
                        my_ar[z] = ""
                        time.sleep(1)
                        print("String after elemination: ", ''.join(my_ar))
                        time.sleep(1)
                        break    
                else:
                        print("No matching closing \"]\"")
                        time.sleep(1)
                        print("Exiting...")
                        sys.exit()  

else:
    print("Opening and closing bracket number does not match!")