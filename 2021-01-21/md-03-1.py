user = input("Enter username: ")
passw = input("Enter password: ")
cor_user = "user"
cor_passw = "password"

while user!=cor_user or passw!=cor_passw:
    print("Username or password is incorrect! Try one more time!")
    user = input("Enter username: ")
    passw = input("Enter password: ")
else:
    print("User logged in successfully!")