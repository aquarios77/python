# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 20:07:13 2021

@author: antons.sincovs
"""

import tkinter as tk

window = tk.Tk()

ramis_00 = tk.Frame(master=window)
ramis_00.grid(row=0 , column=0 , padx=5 , pady=5)
uzraksts_00 = tk.Label(master=ramis_00 , text='(0,0)')
uzraksts_00.pack()

window.mainloop()