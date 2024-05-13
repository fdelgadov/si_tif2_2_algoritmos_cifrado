diccionario = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8,
    'j': 9,
    'k': 10,
    'l': 11,
    'm': 12,
    'n': 13,
    'ñ': 14,
    'o': 15,
    'p': 16,
    'q': 17,
    'r': 18,
    's': 19,
    't': 20,
    'u': 21,
    'v': 22,
    'w': 23,
    'x': 24,
    'y': 25,
    'z': 26
    }

diccionario_inverso = {}

for k, v in diccionario.items():
    diccionario_inverso[v] = k


def descrifrado_otp_diccionario(txt, clave):
    res = ""

    for i in range(len(txt)):
        ct = txt[i]
        id_ct = diccionario[ct]
        cc = clave[i % len(clave)]
        id_cc = diccionario[cc]

        id_cifrado = (id_ct - id_cc) % 27
        res += f"{diccionario_inverso[id_cifrado]}"
    
        print(f"{ct} {id_ct} {id_cc} {id_cifrado}")


    return res

def descifrado_one_time_pad(txt, clave):
    res = ""

    for i in range(len(txt)):
        ct = txt[i]
        cc = clave[i % len(clave)]

        res += f"{chr(ord(ct) ^ ord(cc))}"

    return res

def cifrado_otp_diccionario(txt, clave):
    res = ""

    for i in range(len(txt)):
        ct = txt[i]
        id_ct = diccionario[ct]
        cc = clave[i % len(clave)]
        id_cc = diccionario[cc]

        id_cifrado = (id_ct + id_cc) % 27
        res += f"{diccionario_inverso[id_cifrado]}"
    
        print(f"{ct} {id_ct} {id_cc} {id_cifrado}")

    return res