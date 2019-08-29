def algoSimple(num1,num2):
    """
>>> algoSimple(5,1)
'Mayor el primer numero'
>>> algoSimple(-7,1)
'Mayor el segundo numero"
    """
    if(num1 > num2):
        return "Mayor el primer numero"
    else:
        return "Mayor el segundo numero"
    
if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose = False)
