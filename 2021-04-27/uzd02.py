# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 19:36:04 2021

@author: antons.sincovs
"""

from PIL import Image
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
from random import shuffle


field_count = 0
correct_answers = 0 # pareizas max = 4 where game ends
answers = []
answers_dict = {}

def click_poga(btn , number):
    global field_count , correct_answers , answers , answers_dict
    global my_image_bg , images
    
    if btn['image'] == 'pyimage1' and field_count < 2:
        btn['image'] = images[number]
        field_count += 1
        answers.append(number)
        answers_dict[btn] = images[number]
    
    if len(answers) == 2:
        if images[answers[0]] == images[answers[1]]:
            # atteli ir vienadi
            for key in answers_dict:
                key['state'] = tk.DISABLED
            correct_answers += 1
            if correct_answers == 4:
                # game over
              messagebox.showerror("atminas spele" , "You win! Game Over!")
        else:
            messagebox.showerror("atminas spele" , "Wrong choice!")
            for key in answers_dict:
                key['image'] = 'pyimage1'
        field_count = 0
        answers = []
        answers_dict = {}
    

window = tk.Tk()
window.title("Atminas Spele")

my_image_bg = ImageTk.PhotoImage(Image.open("smiley.png").resize((200 , 200)))

images = []
shuffle(images)
images += images                 


for i in range (1 , 5):
    link = "attels_0" + str(i) + ".png"
    images.append(ImageTk.PhotoImage(Image.open(link).resize((200 , 200))))

pogas  = []
for i in range(8):
    pogas.append(tk.Button(width=200 , height = 200 , image = my_image_bg , command = lambda : click_poga(pogas[i] , i)))

for i in range(8):
    if i > 3:
        pogas[i].grid(row = 1 , column = i - 4)   
    else:
        pogas[i].grid(row = 0 , column = i)

window.mainloop()