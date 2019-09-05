def imprimePares(a,b):
    if(a < b):
        cont = a
        while (cont <= b):
            res2 = cont % 2 #es par?
            if(res2 == 0): #es par
                print(cont)
            cont += 1
    else:
        print("{0} no es menor {1}".format(a,b))

def main():
    val1 = int(input("Dime el primer valor: "))
    val2 = int(input("Dime el segundo valor: "))
    imprimePares(val1,val2)
    print("Fin del programa")