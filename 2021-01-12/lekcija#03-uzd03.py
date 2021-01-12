a1 = int(input("Enter first number: "))
a2 = int(input("Enter second number: "))
a3 = int(input("Enter third number: "))

if(a1 == a2 == a3): print("3 matches")
elif(a1 == a2 or a1 == a3 or a2 == a3): print("2 matches")
else: print ("No matches :( ")