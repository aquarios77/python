# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 17:54:42 2021

@author: antons.sincovs
"""

import tkinter as tk

window = tk.Tk()
image = tk.PhotoImage(file="python_image.png")
label = tk.Label(window, image = image)
label.pack()

window.mainloop()