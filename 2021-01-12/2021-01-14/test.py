#---1--------------
a_smile = (input())
b_smile = (input())

if (a_smile == 'True' and b_smile == 'True') or (a_smile == 'False' and b_smile == 'False') : print(True)
else: print(False)

#---2--------------
a = int(input())
b = int(input())

if (a == 10 and b != 10) or (a!=10 and b==10) or (a+b)==10: print(True)
else: print(False)

#----1------------
a = int(input())
b = int(input())

if(a!=b): print(a+b)
else: print(2*(a+b))