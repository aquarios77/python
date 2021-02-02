import string
alphabet_string_u = string.ascii_uppercase
alphabet_string_l = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

pass_is_good = False
check = [False]*7

while not pass_is_good:
    
    mypass = input("Enter a password for test: ")
    
    if len(mypass) > 8:
        print("Your password is long enough, +")
        check[0] = True
    else:
        print("Your password is shorter than 8 symbols, -")
    
    if (any(elem in mypass for elem in alphabet_string_u)):
        print("Your password contains uppercase letters, +")
        check[1] = True
    else:
        print("Your password does not contain uppercase letters, -")
    
    if (any(elem in mypass for elem in alphabet_string_l)):
        print("Your password contains lowercase letters, +")
        check[2] = True
    else:
        print("Your password does not contain lowercase letters, -")
    
    if (any(elem in mypass for elem in digits)):
        print("Your password contains digits, +")
        check[3] = True
    else:
        print("Your password does not contain digits, -")
    
    if (any(elem in mypass for elem in special_chars)):
        print("Your password contains special chars, +")
        check[4] = True
    else:
        print("Your password does not contain special chars, -")
    
    for i in range(len(mypass) - 2):
        el01 = ord(mypass[i])
        el02 = ord(mypass[i+1])
        el03 = ord(mypass[i+2])
        if (el01 + 1 == el02 and el02 + 1 == el03):
            print("Your password contains consecutive symbols, -")
        else:
            check[5] = True
        if i >= 1 and (el01 - 1 == el02 and el02 - 1 == el03):
            print("Your password contains backward consecutive symbols, -")
        else:
            check[6] = True
   
    if check[5]:
        print("Your password does not contain consecutive symbols, +")
    if check[6]:
        print("Your password does not contain backward consecutive symbols, +")    
    
    if all(check): 
        print("\nYour password is good enough!")
        pass_is_good = True
    else:
        print("\nYour password does not match one of the criterias above, try again!")
     
 
