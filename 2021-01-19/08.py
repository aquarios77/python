i = 1
mini, maxi = 0, 0
print("Enter a number: ")
while i<=10:
    number = int(input("==> "))
    if number == 0:
        break
    if i == 1:
        mini, maxi = number, number
        continue
    if maxi<number:
        maxi = number
    if mini>number:
        mini = number   
    i +=1
    
    
print("Max: ",maxi," Min: ", mini)