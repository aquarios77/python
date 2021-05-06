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
import time

class TimerError(Exception):
    """A custom exception used to report errors in use of Timer class"""

class Timer:
    def __init__(self):
        self._start_time = None

    def start(self):
        """Start a new timer"""
        if self._start_time is not None:
            raise TimerError("Timer is running. Use stop() to stop it")

        self._start_time = time.perf_counter()

    def stop(self):
        """Stop the timer, and report the elapsed time"""
        if self._start_time is None:
            raise TimerError("Timer is not running. Use start() to start it")

        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        return (f"Elapsed time: {elapsed_time:0.4f} seconds")
    
# number of different images - number of images in line with 2 rows, set from 3 to 8 (add more images to set >8)
num = 8 # essentially number of columns

# setting initial values
field_count = 0
correct_answers = 0 # pareizas max = 4 where game ends
answers = []
answers_dict = {}
timer_is_started = False # timer is not started
game_timer = Timer() # creating a timer instance

# method to manage button clicks
def click_poga(btn , number):
    global field_count , correct_answers , answers , answers_dict , num , timer_is_started, game_timer
    global my_image_bg , images
    
    # starting the timer after the first button click
    if timer_is_started == False:
        game_timer.start()
        timer_is_started = True
    
    if btn['image'] == 'pyimage1' and field_count < 2:
        btn['image'] = images[number]
        field_count += 1
        answers.append(number)
        answers_dict[btn] = images[number]
    
    if len(answers) == 2:
        if images[answers[0]] == images[answers[1]]:
            # atteli ir vienadi
            for key in answers_dict:
                key['state'] = tk.DISABLED # fixing buttons with correct answers
            correct_answers += 1
            if correct_answers == num: # game over - all images matched
                message = "You win! Game Over! " + game_timer.stop()  #  stopping the time upon game over
                messagebox.showerror("Memory Game" , message)
        else:
            messagebox.showerror("Memory Game" , "Wrong choice!")
            for key in answers_dict:
                key['image'] = 'pyimage1'
        field_count = 0
        answers = []
        answers_dict = {}

# resetting game state to initial state
def reset():
    global answers , answers_dict , correct_answers , images , my_bg_image , pogas , game_timer, timer_is_started
    for key in answers_dict:
        key['state'] = tk.NORMAL
        key['image'] = my_bg_image
     
    # recreate game timer and reset its state if user starts a new game without exiting from the program
    game_timer = Timer()
    timer_is_started = False
    
    answers = []
    answers_dict = {}
    correct_answers = 0
    pogas = []
    shuffle(images) # shuffling the images, so the order would be different from the previous games
    draw_buttons()
    
# drawing all the buttons needed
def draw_buttons():
    global pogas , num
    # forming a list of buttons with images with a cycle
    for j in range(num * 2):
        pogas.append(tk.Button(width = 200 , height = 200 , image = my_image_bg , command = lambda i=j: click_poga(pogas[i] , i)))
    # forming a grid of buttons with a cycle
    for i in range(num * 2):
        if i > num - 1:
            pogas[i].grid(row = 1 , column = i % num)
        else:
            pogas[i].grid(row = 0 , column = i)
        
# addiing some info about the game
def info():
    new_window = tk.Toplevel()
    new_window.title("About")
    new_window.geometry("300x300")
    about = tk.Label(new_window, text = "This is a tricky mind game! \n Beware player it is highly addictive! \n Whatever you try - do not cheat :)")
    about.grid(row = 0 , column = 0)
    
window = tk.Tk()
window.title("Memory Game")
window.iconbitmap("brain.ico") # nice icon for the game

# adding menus and submenus
main_menu = tk.Menu(window)
window.config(menu=main_menu)
options = tk.Menu(main_menu, tearoff=False)
main_menu.add_cascade(label="Options" , menu=options)
main_menu.add_command(label="About" , command=info)
options.add_command(label="New Game" , command=reset)
options.add_command(label="Exit" , command=window.destroy)


# initial image
my_image_bg = ImageTk.PhotoImage(Image.open("smiley.png").resize((200 , 200)))

images = []
# reading game images from the directory
for i in range (1 , num + 1):
    link = "attels_0" + str(i) + ".png"
    images.append(ImageTk.PhotoImage(Image.open(link).resize((200 , 200))))

images *= 2 # two rows with images
shuffle(images) # suffling images read from the directory
pogas  = []

draw_buttons()

window.mainloop()