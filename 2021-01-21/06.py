int_start = int(input("Enter interval start: "))
int_end = int(input("Enter interval end: "))

if(int_start > int_end):
    int_start,int_end = int_end,int_start

guess_point = round(abs(int_start + int_end)//2)
guess = False

while guess == False:
    print('Is it ',guess_point, '? Print "g" if your number is greated or "s" if your number is smaller or "y" if I guessed correctly')
    answer = input("=>")
    if answer== "y":
        guess = True
        continue
    elif answer == "g":
        int_start = guess_point
        guess_point = round(abs(int_start + int_end)//2)
        continue
    elif answer == "s":
        int_end = guess_point    
        guess_point = round(abs(int_start + int_end)//2)
        continue
    else:
        print("The answer you entered is incorrect!")
        continue
else:
    print("Got you!")
