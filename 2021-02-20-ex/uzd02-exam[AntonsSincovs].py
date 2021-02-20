'''
Antons Sincovs, eksamenas uzdevums #2
'''

import string

low = string.ascii_lowercase
up = string.ascii_uppercase
all_let = low + up

'''
1. Definējiet funkciju, kurai ir viens parametrs – šifrēšanas solis, funkcija atgriež vārdnīcu ar
šifra atslēgām. 
'''

def code_dic(shift=0):
    shift = shift%len(low) # in case shift >= overall alphabet length
    my_dic = {}
    
    shifted_low = low[shift:] + low[:shift] 
    shifted_up = up[shift:] + up[:shift]
    all_shifted = shifted_low + shifted_up
    
    for i in range(len(all_shifted)):
        my_dic[all_let[i]] = all_shifted[i]
        
    return my_dic

'''
2. Definējiet arī funkciju, kas atgriež vārdnīcu ar atslēgām teksta dekodēšanai.
'''

def decode_dic(code_dic): # receives the coded dictionary and as Cesar's cypher is symmetrical - swaps keys and values
    values = list(code_dic.values())
    keys = list(code_dic.keys())
    my_dic = {}
    for i in range(len(code_dic)):
        my_dic[values[i]] = keys[i]
    return my_dic
'''
3. Definējiet funkciju, kurai ir divi parametri – teksts un vārdnīca ar šifra atslēgām.
Funkcija atgriež kodēto vai dekodēto tekstu atkarībā no tā, kura vārdnīca šai funkcijai tiek
iedota kā parametrs.
'''

def code_text(text, dic):
    my_text = []
    for i in range(len(text)):
        if text[i] in dic:
            my_text.append(dic[text[i]])
        else:
            my_text.append(text[i])
    return ''.join(my_text)
        
        
    

# just to check dictionary creation
'''
print(code_dic(13))
print("="*40)
print(decode_dic(code_dic(13)))
'''


text = "I Love Python 3.9 ?!"
dic = code_dic(13)# create a dictionary with shift of 13
print(code_text(text, dic))# display encoded text

co_text = code_text(text, dic)# take the encoded text

dec_dic = decode_dic(dic)# create a decoding dictionary (reverse to encoding)
print(code_text(co_text, dec_dic))# decode the encoded text using decoding dictionary
