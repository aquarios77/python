# optimized almost all repeatative button generations and corresponding tasks

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

speletajs = True  # True == X, False = O
skaits = 0
winX = 0
winO = 0
draws = 0


def click_poga(num):
    global speletajs , skaits , pogas
    if pogas[num]['text'] == ' ' and speletajs:
        pogas[num]['text'] = 'X'
        speletajs = False
        skaits += 1
        parbaudit_uzvaru()
    elif pogas[num]['text'] == ' ' and not speletajs:
        pogas[num]['text'] = 'O'
        speletajs = True
        skaits += 1
        parbaudit_uzvaru()
    else:
        messagebox.showerror('TicTacToe', 'Si rutina ir aiznemta')


def uzvara(s):
   
    if (pogas[0]['text'] == s and pogas[1]['text'] == s and pogas[2]['text'] == s or
        pogas[3]['text'] == s and pogas[4]['text'] == s and pogas[5]['text'] == s or
        pogas[6]['text'] == s and pogas[7]['text'] == s and pogas[8]['text'] == s or
        pogas[0]['text'] == s and pogas[3]['text'] == s and pogas[6]['text'] == s or
        pogas[1]['text'] == s and pogas[4]['text'] == s and pogas[7]['text'] == s or
        pogas[2]['text'] == s and pogas[5]['text'] == s and pogas[8]['text'] == s or
        pogas[0]['text'] == s and pogas[4]['text'] == s and pogas[8]['text'] == s or
        pogas[2]['text'] == s and pogas[4]['text'] == s and pogas[6]['text'] == s):
    
        label = ttk.Label(mans_logs, text = stats() , font=("Helvetica" , 18))
        label.grid(column = 4, row = 0 , rowspan=4 )
        return True
    else:
        return False
    

def parbaudit_uzvaru():
    
    global uzvaretajs, winX, winO, draws
    uzvaretajs = False
    if uzvara('X'):  # uzvareja X
        messagebox.showinfo('TicTacToe', 'Player "X" has won!')
        uzvaretajs = True
        winX += 1
    elif uzvara('O'):  # uzvareja O
        messagebox.showinfo('TicTacToe', 'Player "O" has won!')
        uzvaretajs = True
        winO += 1
    elif skaits == 9 and not uzvaretajs:  # neizskirts
        draws += 1
        messagebox.showinfo('TicTacToe', 'It\'s a Draw!')
        izslegt_pogu()


def izslegt_pogu():
    
    for i in range(9):
        pogas[i].config(state=tk.DISABLED)
    
def atiestatit():
    
    for i in range(9):
        pogas[i].config(state=tk.NORMAL)
        pogas[i]['text'] = ' '
    
    global uzvaretajs , skaits , speletajs
    uzvaretajs = False
    speletajs = False
    skaits = 0
   
def stats():
    global winX , winO , draws
    message = "-===GAME STATS===- \n Player X: " + str(winX) + " wins , " + str(winO) + " losses \n Player O: " + str(winO) + " wins , " + str(winX) + " losses" 
    return message

def info():
    jauns_logs = tk.Toplevel()
    jauns_logs.title("About")
    jauns_logs.geometry("300x300")
    apraksts = tk.Label(jauns_logs, text = "Tic-Tac-Toe \n Good Old Game :)")
    apraksts.grid(row = 0 , column = 0)
    
mans_logs = tk.Tk()
mans_logs.title('Tic Tac Toe')
mans_logs.iconbitmap("gift_box.ico")
galvena_izvelne = tk.Menu(mans_logs)
mans_logs.config(menu=galvena_izvelne)
iespejas = tk.Menu(galvena_izvelne, tearoff=False)
galvena_izvelne.add_cascade(label="Iespejas" , menu=iespejas)
galvena_izvelne.add_command(label="par programmu" , command=info)
iespejas.add_command(label="Jauna spele" , command=atiestatit)
iespejas.add_command(label="Iziet" , command=mans_logs.destroy)

# array for all buttons
pogas = []

# j = i because without it lambda function glitches in array, collecting buttons into array with click() lambda function assigned
for i in range(0 , 9):
    pogas.append( tk.Button(mans_logs, text=" ", width=6, height=3, font=(
    "Helvetica", 24), command=lambda j = i: click_poga(j)))
# cyclical generation of button grid
for i in range(9):
    pogas[i].grid(row = int(i / 3) , column = i % 3)

stats()
    

mans_logs.mainloop()
