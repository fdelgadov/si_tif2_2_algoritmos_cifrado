# https://web.archive.org/web/20160927095624/http://www.criptored.upm.es/crypt4you/temas/criptografiaclasica/leccion7.html

from preprocesamiento import *

def generar_serie(tam):
    primos = [2]
    pares = [x for x in range(4, tam + 1, 2)]
    otros = [1]

    for i in range(3, tam + 1, 2):
        primo = True
        for j in primos:
            if i % j == 0:
                primo = False
                otros.append(i)
                break
                
        if primo:
            primos.append(i)

    return primos + pares + otros

def codificar_por_serie(texto, serie):
    res = ""
    for i in range(len(texto)):
        res += texto[serie[i] - 1]

    return res

