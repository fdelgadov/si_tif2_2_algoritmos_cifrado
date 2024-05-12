import tkinter as tk
from cifrado_permutacion_serie import *
from descifrado_one_time_pad import *
from descifrado_permutacion_serie import *

def btn_cifrado_permutacion_serie():
    txt = txt_original.get("1.0", "end-1c")
    txt = preprocesamiento(txt)
    serie = generar_serie(len(txt))
    txt = codificar_por_serie(txt, serie)
    txt_cifrado.delete("1.0", "end")
    txt_cifrado.insert("1.0", txt)

def btn_descifrado_permutacion_serie():
    txt = txt_cifrado.get("1.0", "end-1c")
    serie = generar_serie(len(txt))
    txt = descifrado_permutacion_serie(txt, serie)
    txt_original.delete("1.0", "end")
    txt_original.insert("1.0", txt)

ventana = tk.Tk()
ventana.geometry("640x360")

lbl_original = tk.Label(ventana, text="Texto original", anchor='w')
lbl_aux = tk.Label(ventana)
lbl_cifrado = tk.Label(ventana, text="Texto cifrado", anchor='w')
txt_original = tk.Text(ventana, height=5)
txt_cifrado = tk.Text(ventana, height=5)
btn_cifrar = tk.Button(ventana, text="Cifrar", command=btn_cifrado_permutacion_serie)
btn_descifrar = tk.Button(ventana, text="Descifrar", command=btn_descifrado_permutacion_serie)

lbl_original.pack(fill='x')
txt_original.pack(fill='x')
lbl_aux.pack()
txt_cifrado.pack(fill='x')
btn_cifrar.pack()
btn_descifrar.pack()

ventana.mainloop()