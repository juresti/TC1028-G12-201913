def sumaHasta1000():
    cont = 0
    suma = 0
    while(suma <= 1000):
        num = int(input("Dime un numero: "))
        suma += num
        cont += 1
    return suma, cont
    
def main():
    suma, num_veces = sumaHasta1000()
    print("Los {0} numeros que me diste suman {1}".format(num_veces,suma))
    