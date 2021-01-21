user = input("Enter username: ")
passw = input("Enter password: ")
cor_user = "user"
cor_passw = "password"

while user!=cor_user or passw!=cor_passw:
    print('Username or password is incorrect! Type "n" to quit or "y" to try one more time: ',end='')
    if(input()!='y'):
        print('Quitting now...')
        break
    user = input("Enter username: ")
    passw = input("Enter password: ")
else:
    print("User logged in successfully!")
