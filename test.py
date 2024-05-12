from cifrado_permutacion_serie import *
from descifrado_permutacion_serie import *
from descifrado_one_time_pad import *

def descifrado():
    nombre_archivo = "cifrado"
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        txt = archivo.read()

    serie = generar_serie(len(txt))

    print(descifrado_permutacion_serie(txt, serie))

def cifrado():
    nombre_archivo = "soneto"
    with open(nombre_archivo, 'r', encoding="utf-8") as archivo:
        txt = archivo.read()

    print(txt)
    txt = preprocesamiento(txt)
    print(txt)
    serie = generar_serie(len(txt))
    txt = codificar_por_serie(txt, serie)
    print(txt)

    with open("cifrado", "w", encoding="utf-8") as archivo:
        archivo.write(txt)

def test1_permutacion_serie():
    cifrado()
    print("")
    descifrado()

def test2_one_time_pad():
    with open("otp_cifrado", 'r', encoding="utf-8") as archivo:
        txt = archivo.read()

    with open("otp_clave", 'r', encoding="utf-8") as archivo:
        clave = archivo.read()

    print(txt)
    print(descifrado_one_time_pad(txt, clave))

test2_one_time_pad()