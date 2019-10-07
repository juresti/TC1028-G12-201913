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
    
def tamanoMatriz(matriz):
    numRen = len(matriz)
    if esCuadrada(matriz):
        return (numRen,numRen)
    else:
        numCol = len(matriz[0])
        for renglon in matriz:
            col = len(renglon)
            if (numCol != col):
                return (-1,-1) #código error
        
        return (numRen,numCol)
    
def mismoTamano(matriz1,matriz2) :
    renM1,colM1 = tamanoMatriz(matriz1)
    renM2,colM2 = tamanoMatriz(matriz2)
    
    if (renM1 == renM2):
        if(colM1 == colM2):
            return True
        else:
            print("Numero de columnas diferente")
            return False
    else:
        print("Matriz 1 tiene {0} renglones y la 2 tiene {1}".format(renM1,renM2))
        return False
    
    
    