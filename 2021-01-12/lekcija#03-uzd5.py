a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter third side: "))

p = (a+b+c)/2
s = (p(p-a)(p-b)(p-c))**0.5

if( (a+b)>c and (a+c)>b and (b+c)>a): print("Triangle exists!")
else: print("No triangle!")