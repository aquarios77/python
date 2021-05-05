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

# number of different images
num = 8

field_count = 0
correct_answers = 0 # pareizas max = 4 where game ends
answers = []
answers_dict = {}

# method to manage button clicks
def click_poga(btn , number):
    global field_count , correct_answers , answers , answers_dict , num
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
            if correct_answers == num:
                # game over
              messagebox.showerror("atminas spele" , "You win! Game Over!")
        else:
            messagebox.showerror("atminas spele" , "Wrong choice!")
            for key in answers_dict:
                key['image'] = 'pyimage1'
        field_count = 0
        answers = []
        answers_dict = {}


def reset():
    global answers , answers_dict , correct_answers , images , my_bg_image , pogas
    for key in answers_dict:
        key['state'] = tk.ENABLED
        key['image'] = my_bg_image
        
    answers = []
    answers_dict = {}
    correct_answers = 0
    pogas = []
    shuffle(images)
    draw_buttons()
    

def draw_buttons():
    global pogas , num
    
    for j in range(num * 2):
        pogas.append(tk.Button(width=200 , height = 200 , image = my_image_bg , command = lambda i=j: click_poga(pogas[i] , i)))
    
    for i in range(num * 2):
        if i > num - 1:
            pogas[i].grid(row = 1 , column = i % num)
        else:
            pogas[i].grid(row = 0 , column = i)
        

def info():
    new_window = tk.Toplevel()
    new_window.title("About program")
    new_window.geometry("300x300")
    about = tk.Label(new_window, text = "This is a tricky mind game! \n Beware player it is highly addictive! \n Whatever you try - do not cheat :)")
    about.grid(row = 0 , column = 0)
    
window = tk.Tk()
window.title("Memory Game")
window.iconbitmap("brain.ico")

main_menu = tk.Menu(window)
window.config(menu=main_menu)
options = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Options" , menu=options)
main_menu.add_command(label="About program" , command=info)
options.add_command(label="New Game" , command=reset)
options.add_command(label="Exit" , command=window.destroy)



my_image_bg = ImageTk.PhotoImage(Image.open("smiley.png").resize((200 , 200)))

images = []
for i in range (1 , num + 1):
    link = "attels_0" + str(i) + ".png"
    images.append(ImageTk.PhotoImage(Image.open(link).resize((200 , 200))))

# two rows with images
images *= 2
shuffle(images)

#sprint(images)

pogas  = []
draw_buttons()

window.mainloop()