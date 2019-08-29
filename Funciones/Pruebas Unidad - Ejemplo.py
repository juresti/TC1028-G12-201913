def SumaDos(a, b):

    '''Calcula la suma de dos números.

    Parámetros:
    a -- Primer número
    b -- Segundo número

    Ejemplos de uso:

    >>> SumaDos(1, 2)
    3

    >>> SumaDos(2, 2)
    4

    >>> SumaDos(5.0, 2)
    7.0

    >>> SumaDos(2.5, 1.5)
    4.0

    '''
    return a + b


def acceso(edad, divertirse):
    """ Dada una edad, indica si puede pasar a la fiesta.
    
    Ejemplos de uso:
    >>> acceso(33,"Si")
    Puedes entrar a la fiesta
    >>> acceso(17,"No")
    Todavía estás muy chavo
    >>> acceso(74,"Si")
    Ya está muy ruco
    """
    if edad > 18:
        if edad < 50:
            if divertirse == "Si":
                print ("Puedes entrar a la fiesta")
            else:
                print ("Debes de tener ganas de divertirte")
        else:
            print ("Ya está muy ruco")
    else:
        print ("Todavía estás muy chavo")

def main():
    print("Ejercicio 1: acceso a fiesta")
    acceso(15,"No")
    
    print("\nEjercicio 2: suma de dos numeros")
    res = SumaDos(3,8)
    print("SumaDos me regreso: ",res)

if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)
    
