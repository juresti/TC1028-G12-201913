def cuentaLetras(palabra):
    dicLetras = {}
    for letra in palabra:
        if letra in dicLetras:
            dicLetras[letra] += 1
        else:
            dicLetras[letra] = 1
    return dicLetras

def cuentaLetrasSinDic(palabra):
    letras = []
    cont = []
    for letra in palabra:
        if letra in letras:
            cont[letras.index(letra)] += 1
        else:
            letras.append(letra)
            cont.append(1)
    
    salida = []
    for indice in range(len(letras)):
        salida.append([letras[indice],cont[indice]])
    return salida