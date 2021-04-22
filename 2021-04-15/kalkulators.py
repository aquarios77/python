import tkinter as tk
mat_op = '' 


def click_vienads():
    global mat_op
    otrais_skaitlis = int(teksta_lauks.get())
    result = 0
    if mat_op == '+':
        result = pirmais_skaitlis + otrais_skaitlis
    elif mat_op == '-':
        result = pirmais_skaitlis - otrais_skaitlis
    elif mat_op == '*':
        result = pirmais_skaitlis * otrais_skaitlis
    elif mat_op == '/':
        result = pirmais_skaitlis / otrais_skaitlis
    else:
        result = 0
    teksta_lauks.delete(0,tk.END)
    teksta_lauks.insert(0, str(result))
    
    mat_op = '='
    #pass

def click_darbiba(command):
    global pirmais_skaitlis
    global mat_op
    mat_op = command
    pirmais_skaitlis = int(teksta_lauks.get())
    teksta_lauks.delete(0,tk.END)

def click_skaitli(number):
    global mat_op
    if mat_op == '=':
        teksta_lauks.delete(0,tk.END)
        mat_op = ''
    teksta_lauks.insert(tk.END,number)
    
def click_backsp():
    teksts = teksta_lauks.get()
    print(type(teksts))
    teksta_lauks.delete(len(teksts)-1,tk.END)
    
def click_clear():
    teksta_lauks.delete(0,tk.END)
    #pirmais_skaitlis = 0
    #mat_op = ""

window = tk.Tk()
window.title("Mans kalkulators")

teksta_lauks = tk.Entry(master=window, width=25, font=("Arial", 20), justify=tk.RIGHT)

poga_0 = tk.Button(master=window, text='0', padx=40, pady=20, command=lambda:click_skaitli(0))
poga_1 = tk.Button(master=window, text='1', padx=40, pady=20, command=lambda:click_skaitli(1))
poga_2 = tk.Button(master=window, text='2', padx=40, pady=20, command=lambda:click_skaitli(2))
poga_3 = tk.Button(master=window, text='3', padx=40, pady=20, command=lambda:click_skaitli(3))
poga_4 = tk.Button(master=window, text='4', padx=40, pady=20, command=lambda:click_skaitli(4))
poga_5 = tk.Button(master=window, text='5', padx=40, pady=20, command=lambda:click_skaitli(5))
poga_6 = tk.Button(master=window, text='6', padx=40, pady=20, command=lambda:click_skaitli(6))
poga_7 = tk.Button(master=window, text='7', padx=40, pady=20, command=lambda:click_skaitli(7))
poga_8 = tk.Button(master=window, text='8', padx=40, pady=20, command=lambda:click_skaitli(8))
poga_9 = tk.Button(master=window, text='9', padx=40, pady=20, command=lambda:click_skaitli(9))

poga_plus = tk.Button(master=window, text='+', padx=40, pady=20, command=lambda:click_darbiba('+'))
poga_minus = tk.Button(master=window, text='-', padx=40, pady=20, command=lambda:click_darbiba('-'))
poga_reiz = tk.Button(master=window, text='*', padx=40, pady=20, command=lambda:click_darbiba('*'))
poga_dalit = tk.Button(master=window, text='/', padx=40, pady=20, command=lambda:click_darbiba('/'))
poga_vienads = tk.Button(master=window, text='=', padx=40, pady=20, command=lambda:click_vienads())
poga_backsp = tk.Button(master=window, text='B', padx=40, pady=20, command=lambda:click_backsp())
poga_clear = tk.Button(master=window, text='C', padx=80, pady=20, command=lambda:click_clear())

teksta_lauks.grid(row=0, column=0, columnspan=4)
poga_7.grid(row=1, column=0)
poga_8.grid(row=1, column=1)
poga_9.grid(row=1, column=2)

poga_4.grid(row=2, column=0)
poga_5.grid(row=2, column=1)
poga_6.grid(row=2, column=2)

poga_1.grid(row=3, column=0)
poga_2.grid(row=3, column=1)
poga_3.grid(row=3, column=2)
poga_0.grid(row=4, column=1)

poga_reiz.grid(row=1, column=3)
poga_dalit.grid(row=2, column=3)
poga_plus.grid(row=3, column=3)
poga_minus.grid(row=4, column=3)

poga_backsp.grid(row=4, column=0)
poga_vienads.grid(row=4, column=2)
poga_clear.grid(row=5, column=0, columnspan=4)

window.mainloop()
