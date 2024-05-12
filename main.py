import tkinter as tk
from cifrado_permutacion_serie import *
from descifrado_one_time_pad import *

ventana = tk.Tk()
ventana.geometry("640x360")

lbl_original = tk.Label(ventana, text="Texto original", anchor='w')
lbl_aux = tk.Label(ventana)
lbl_cifrado = tk.Label(ventana, text="Texto cifrado", anchor='w')
txt_original = tk.Text(ventana, height=5)
txt_cifrado = tk.Text(ventana, height=5)
btn_cifrar = tk.Button(ventana, text="Cifrar", command="")
btn_descifrar = tk.Button(ventana, text="Descifrar", command="")

lbl_original.pack(fill='x')
txt_original.pack(fill='x')
lbl_aux.pack()
txt_cifrado.pack(fill='x')
btn_cifrar.pack()
btn_descifrar.pack()

ventana.mainloop()