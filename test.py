import sys
from cifrado_permutacion_serie import *
from cifrado_one_time_pad import *

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
    print(descrifrado_otp_diccionario(txt, clave))

def test3_preprocesamiento():
    txt = ""

    for i in range(0, 256):
        txt += chr(i)

    print(txt)

    txt = solo_minusculas_ñ(txt)

    print(txt)

_ = sys.argv
if _[1] == "test1":
    test1_permutacion_serie()
elif _[1] == "test2":
    test2_one_time_pad()
elif _[1] == "test3":
    test3_preprocesamiento()