import tkinter as tk
from cifrado_permutacion_serie import *

class panel1(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.txt_original = 0
        self.txt_cifrado = 0
        self.raiz = raiz
        self.contruir_panel()

    def btn_cifrado_permutacion_serie(self):
        txt = self.txt_original.get("1.0", "end-1c")
        txt = solo_minusculas_ñ(txt)
        serie = generar_serie(len(txt))
        txt = codificar_por_serie(txt, serie)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_permutacion_serie(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")
        serie = generar_serie(len(txt))
        txt = descifrado_permutacion_serie(txt, serie)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)

    def contruir_panel(self):
        lbl_titulo = tk.Label(self, text="Permutacion por serie")
        lbl_original = tk.Label(self, text="Texto original", anchor='w')
        lbl_aux = tk.Label(self)
        lbl_cifrado = tk.Label(self, text="Texto cifrado", anchor='w')
        self.txt_original = tk.Text(self, height=5)
        self.txt_cifrado = tk.Text(self, height=5)
        btn_cifrar = tk.Button(self, text="Cifrar", command=self.btn_cifrado_permutacion_serie)
        btn_descifrar = tk.Button(self, text="Descifrar", command=self.btn_descifrado_permutacion_serie)

        lbl_titulo.pack()
        lbl_original.pack(fill='x')
        self.txt_original.pack(fill='x')
        lbl_aux.pack()
        lbl_cifrado.pack(fill='x')
        self.txt_cifrado.pack(fill='x')
        btn_cifrar.pack()
        btn_descifrar.pack()