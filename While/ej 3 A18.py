def esPerfecto(valor):
    cont = valor - 1
    suma = 0
    while(cont > 0):
        res = valor % cont
        if(res == 0): #sí es divisor
            suma += cont
            print("El {0} es divisor de {1}".format(cont,valor))
        cont -= 1
    if(valor == suma):
        return "Perfecto"
    else:
        return "Imperfecto"
    
def main():
    num = int(input("Dime numero para ver si es perfecto: "))
    que_fue = esPerfecto(num)
    print("El número {0} resulto {1}".format(num,que_fue))