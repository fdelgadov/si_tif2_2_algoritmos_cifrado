import tkinter as tk
from cifrado_one_time_pad import *
from panel2 import *
from panel1 import *

def mostrar_panel1():
    panel1.pack()
    panel2.pack_forget()
    btn_cambio.config(text="One Time Pad", command=mostrar_panel2)

def mostrar_panel2():
    panel2.pack()
    panel1.pack_forget()
    btn_cambio.config(text="Permutacion por serie", command=mostrar_panel1)

raiz = tk.Tk()
raiz.title("Algoritmos de cifrado")
raiz.geometry("640x360")

btn_cambio = tk.Button(raiz, text="One Time Pad", command=mostrar_panel2)

btn_cambio.pack()

panel2 = panel2(raiz)
panel1 = panel1(raiz)

mostrar_panel1()

raiz.mainloop()