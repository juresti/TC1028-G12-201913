def crearMatriz(numRen,numCol,valorInicial):
    matriz = []
    #renglon = [valorInicial] * numCol
    renglon = []
    for elem in range(numCol):
        renglon.append(valorInicial)
        
    for valor in range(numRen):
        matriz.append(renglon)
    return matriz

def imprimirMatriz(matriz):
    salida = "" #string vacio
    for renglon in matriz:
        for valor in renglon:
            salida += str(valor) + " "
        salida += "\n"
    print(salida)
    
def esCuadrada(matriz):
    numRen = len(matriz)
    
    numCol = len(matriz[0])
    for renglon in matriz: #Obtener numero de columnas
        col = len(renglon)
        if(col != numCol): #verificar todos mismo tamaño
            return False
    
    if(numRen == numCol):
        return True
    else:
        return False
    
        