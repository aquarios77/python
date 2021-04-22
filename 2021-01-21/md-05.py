'''
Antons Sincovs

random number guessing game

'''


import random
start = int(input("Enter start integer: "))
end = int(input("Enter end integer: "))
number = random.randint(start, end)

print("I have picked a number between",start,'and',end,'. Guess the number! ',sep=' ')
guess = int(input(":"))

try_count = 1

while guess!=number:
    if guess>number:
        print("My number is smaller",sep='',end='')
    else:
      print("My number is larger",sep='',end='')
    try_count+=1
    print(" Guess again! ")
    guess = int(input(":"))

else:
    print ("You win! Try count: ",try_count,' ')