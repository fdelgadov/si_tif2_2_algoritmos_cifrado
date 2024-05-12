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

def descrifrado_otp_diccionario(txt, clave):
    res = ""
    diccionario_inverso = {}

    for k, v in diccionario.items():
        diccionario_inverso[v] = k

    for i in range(len(txt)):
        ct = txt[i]
        cc = clave[i]
        res += f"{diccionario_inverso[(ord(cc) ^ ord(ct)) % 27]}"

    return res

def descifrado_one_time_pad(txt, clave):
    res = ""

    for i in range(len(txt)):
        ct = txt[i]
        cc = clave[i % len(clave)]

        res += f"{chr(ord(cc) ^ ord(ct))}"

    return res