def descifrado_one_time_pad(txt, clave):
    res = ""

    for i in range(len(txt)):
        ct = txt[i]
        cc = clave[i % len(clave)]

        res += f"{chr(ord(cc) ^ ord(ct))}"

    return res