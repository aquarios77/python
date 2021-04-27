# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 18:13:05 2021

@author: antons.sincovs
"""

import tkinter as tk
from PIL import Image , ImageTk


window = tk.Tk()
window.geometry('200x200')

image = Image.open("python_image.png")
image = image.resize((20,20))
image = ImageTk.PhotoImage(image)

button = tk.Button(width=100 , height = 20 , image = image)

window.mainloop()