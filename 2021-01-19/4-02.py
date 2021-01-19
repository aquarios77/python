i = 2
number = int(input("Enter a number: "))
while i<=(number/2):
    if number%i==0:
        print("Not a primary")
        break
    i+=1
else:
    print("Primary")