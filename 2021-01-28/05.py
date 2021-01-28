import string
alphabet_string_u = string.ascii_uppercase
alphabet_string_l = string.ascii_lowercase
digits = string.digits
special_chars = string.punctuation

mypass = input("Enter a password for test: ")

if len(mypass)>8:
    print("Your password is long enough, +")
else:
    print("Your password is shorter than 8 symbols, -")
    
if (any(elem in mypass for elem in alphabet_string_u)):
    print("Your password contains uppercase letters, +")
else:
    print("No uppercase letters, try again")

if (any(elem in mypass for elem in alphabet_string_l)):
    print("Your password contains lowercase letters, +")
else:
    print("No lowercase letters, -")
    
if (any(elem in mypass for elem in digits)):
    print("Your password contains digits, +")
else:
    print("No digits, try again")
    
if (any(elem in mypass for elem in special_chars)):
    print("Your password contains special chars, +")
else:
    print("No special chars, -")

for i in range (len(mypass) - 2):
    el01 = ord(mypass[i])
    el02 = ord(mypass[i+1])
    el03 = ord(mypass[i+2])
    if (el01 + 1 == el02 and el02 + 1 == el03):
        print("Your password contains consecutive symbols, -")
    if i >= 1 and (el01 - 1 == el02 and el02 - 1 == el03 ):
        print("Your password contains backward consecutive symbols, try again")