user = input("Enter username: ")
passw = input("Enter password: ")
cor_user = "user"
cor_passw = "password"
fail_count=0
fail_block=3

while user!=cor_user or passw!=cor_passw:
    fail_count+=1
    if fail_count==fail_block:
        print('Your account is blocked! Please contact the admnistrator!')
        break
    print('Username or password is incorrect! Fail count:',fail_count,' (tries left:',(fail_block-fail_count),')\nType "y" to try one more time or anything else to quit: ',end='',sep='')
    if(input()!='y'):
        print('Quitting now...')
        break
    user = input("Enter username: ")
    passw = input("Enter password: ")
else:
    print("User logged in successfully!")
