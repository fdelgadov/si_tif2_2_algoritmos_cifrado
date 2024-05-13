import tkinter as tk

# Funciones para mostrar y ocultar marcos
def mostrar_marco1():
    marco1.pack()
    marco2.pack_forget()

def mostrar_marco2():
    marco2.pack()
    marco1.pack_forget()

# Crear una instancia de la clase Tk, que representa la ventana principal
raiz = tk.Tk()
raiz.title("Paneles intercambiables")

# Crear marco para la ventana 1
marco1 = tk.Frame(raiz)
etiqueta_ventana1 = tk.Label(marco1, text="Esta es la ventana 1")
etiqueta_ventana1.pack()
boton_ventana1 = tk.Button(marco1, text="Mostrar ventana 2", command=mostrar_marco2)
boton_ventana1.pack()

# Crear marco para la ventana 2
marco2 = tk.Frame(raiz)
etiqueta_ventana2 = tk.Label(marco2, text="Esta es la ventana 2")
etiqueta_ventana2.pack()
boton_ventana2 = tk.Button(marco2, text="Mostrar ventana 1", command=mostrar_marco1)
boton_ventana2.pack()

# Mostrar el marco de la ventana 1 al iniciar
mostrar_marco1()

# Iniciar el bucle de eventos de la interfaz gráfica
raiz.mainloop()
