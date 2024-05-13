import tkinter as tk
from cifrado_one_time_pad import *
from preprocesamiento import *

class panel2(tk.Frame):
    def __init__(self, raiz):
        super().__init__(raiz)
        self.raiz = raiz
        self.construir_panel()

    def btn_cifrado_OTP(self):
        txt = self.txt_original.get("1.0", "end-1c")
        txt = solo_minusculas_ñ(txt)
        print(f"{txt}\n")

        clave = self.txt_clave.get("1.0", "end-1c")
        clave = solo_minusculas_ñ(clave)
        print(f"{clave}\n")

        txt = cifrado_otp_diccionario(txt, clave)
        self.txt_cifrado.delete("1.0", "end")
        self.txt_cifrado.insert("1.0", txt)

    def btn_descifrado_OTP(self):
        txt = self.txt_cifrado.get("1.0", "end-1c")

        clave = self.txt_clave.get("1.0", "end-1c")
        clave = solo_minusculas_ñ(clave)

        txt = descrifrado_otp_diccionario(txt, clave)
        self.txt_original.delete("1.0", "end")
        self.txt_original.insert("1.0", txt)

    def construir_panel(self):
        lbl_titulo = tk.Label(self, text="One Time Pad")
        lbl_original = tk.Label(self, text="Texto original", anchor='w')
        lbl_aux = tk.Label(self)
        lbl_cifrado = tk.Label(self, text="Texto cifrado", anchor='w')
        lbl_clave = tk.Label(self, text="Clave", anchor='w')
        self.txt_original = tk.Text(self, height=5)
        self.txt_cifrado = tk.Text(self, height=5)
        self.txt_clave = tk.Text(self, height=1)
        btn_cifrar = tk.Button(self, text="Cifrar", command=self.btn_cifrado_OTP)
        btn_descifrar = tk.Button(self, text="Descifrar", command=self.btn_descifrado_OTP)

        lbl_titulo.pack()
        lbl_clave.pack(fill='x')
        self.txt_clave.pack(fill='x')
        lbl_aux.pack()
        lbl_original.pack(fill='x')
        self.txt_original.pack(fill='x')
        lbl_aux.pack()
        lbl_cifrado.pack(fill='x')
        self.txt_cifrado.pack(fill='x')
        btn_cifrar.pack()
        btn_descifrar.pack()