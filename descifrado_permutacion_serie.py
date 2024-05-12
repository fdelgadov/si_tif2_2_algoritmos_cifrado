from cifrado_permutacion_serie import generar_serie

def descifrado_permutacion_serie(texto, serie):
    serie_inversa = [0 for x in range(len(serie))]
    j = 1
    for i in serie:
        serie_inversa[i - 1] = j
        j += 1

    res = ""
    for i in range(len(texto)):
        res += texto[serie_inversa[i] - 1]

    return res