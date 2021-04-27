# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:34:22 2021

@author: antons.sincovs
"""
import os
from PIL import Image
import glob
import tkinter as tk
from PIL import ImageTk


        
def click_forward(image_number):
    global my_label , btn_forward , btn_back
    global current_image
    
    if current_image == len(image_list) - 2:
        btn_forward.configure(state=tk.DISABLED)
    else:
        btn_forward.configure(state=tk.ACTIVE)
        btn_back.configure(state=tk.ACTIVE)
    
    current_image += 1
    my_label.configure(image = image_list[current_image])
    pass

def click_back(image_number):
    global my_label , btn_forward , btn_back
    global current_image
    
    if current_image == 1:
        btn_back.configure(state=tk.DISABLED)
    else:
        btn_back.configure(state=tk.ACTIVE)
    
    current_image -= 1
    my_label.configure(image = image_list[current_image])
    pass

window = tk.Tk()
window.title("attelu galerija")

files = glob.glob("*.jpg")
files += glob.glob("*.png")
files += glob.glob("*.gif")
files.sort(key=os.path.getmtime, reverse=True)

#my_image = ImageTk.PhotoImage(Image.open(files[0]))
#my_label = tk.Label(image = my_image)
#my_label.grid(row = 0 , column = 0 , columnspan = 3)

image_list = [ImageTk.PhotoImage(Image.open(f)) for f in files]

current_image = 0
my_label = tk.Label(image = image_list[0])
my_label.grid(row = 0 , column = 0 , columnspan = 3)
#print(my_label['image'])

#print(image_list)

btn_back = tk.Button(window , text = "<<" , state = tk.DISABLED, command = lambda:click_back(current_image))
btn_forward = tk.Button(window , text = ">>" , command = lambda:click_forward(current_image))
btn_quit = tk.Button(window , text = "exit" , command = window.destroy)

btn_back.grid(row = 1, column = 0)
btn_quit.grid(row = 1, column = 1)
btn_forward.grid(row = 1, column = 2)

window.mainloop()