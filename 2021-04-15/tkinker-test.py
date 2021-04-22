# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 18:49:01 2021

@author: antons.sincovs
"""

import tkinter as tk

def button_note1():
    print("Hi!")
    
def button_note2(name):
    print("Button " + name + "is pressed!" )

window = tk.Tk()

# height and width is take for OS font size
hello = tk.Label(text="Hello from Python!" , width=30 , height=10 ,
                 foreground="blue" , background="orange"
                 )

hello.pack()

button = tk.Button(text="Push me!" , width=30 , height=10 ,
                 foreground="red" , background="lime" , command=lambda:button_note2("my precious!")
                 )

button.pack()

# in the very end of the script
window.mainloop()