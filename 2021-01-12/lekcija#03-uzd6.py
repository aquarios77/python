a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b**2 - 4*a*c)

if(d>=0):
    x1 = (-b + d**0.5)/2*a
    x2 = (-b - d**0.5)/2*a
    if(x1!=x2):
        print("x1=",x1," x2=",x2)
    else:
        print("x=",x1)
else:
    print("D is negative!")