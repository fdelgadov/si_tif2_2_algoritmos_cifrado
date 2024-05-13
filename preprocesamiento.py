caracter_sustituto = {
    'a': 'u',
    'h': 't',
    'ñ': 'e',
    'k': 'l',
    'v': 'f',
    'w': 'b',
    'z': 'y',
    'r': 'p'
}

tildes_vocales = {
    'á': 'a',
    'é': 'e',
    'í': 'i',
    'ó': 'o',
    'ú': 'u',
    'Á': 'A',
    'É': 'E',
    'Í': 'I',
    'Ó': 'O',
    'Ú': 'U',
    'ü': 'u',
    'Ü': 'u'
}

signos = [' ', ',', '.', ';', '\n']

def sustituciones(txt):
    aux = txt
    for k, v in caracter_sustituto.items():
        aux = aux.replace(k, v)
        aux = aux.replace(chr(ord(k) - 32), chr(ord(v) - 32))

    return aux

def eliminar_tildes(txt):
    aux = txt
    for k, v in tildes_vocales.items():
        aux = aux.replace(k, v)
    return aux

def a_mayuscula(txt):
    aux = txt

    for x in range(97, 123):
        aux = aux.replace(chr(x), chr(x - 32))
    
    aux = aux.replace('ñ', 'Ñ')

    return aux

def a_minuscula(txt):
    aux = txt

    for x in range(65, 91):
        aux = aux.replace(chr(x), chr(x  + 32))

    aux = aux.replace('Ñ', 'ñ')

    return aux

def eliminar_signos(txt):
    aux = txt

    for c in signos:
        aux = aux.replace(c, '')

    return aux

def solo_minusculas_ñ(txt):
    aux = ""
    validos = "abcdefghijklmnñopqrstuvwxyz"

    txt = a_minuscula(txt)
    txt = eliminar_tildes(txt)
    for c in txt:
        if c in validos:
            aux += c

    return aux

def preprocesamiento(texto):
    res = texto
    #res = sustituciones(res)
    res = eliminar_tildes(res)
    res = a_mayuscula(res)
    res = eliminar_signos(res)

    return res