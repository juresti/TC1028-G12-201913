cal1 = int(input("Dime la calificación del parcial 1: "))
cal2 = int(input("Dime la calificación del parcial 2: "))
cal3 = int(input("Dime la calificación del parcial 3: "))

promedio = (cal1 + cal2 + cal3) / 3

print("Tu promedio es {0} en este periodo".format(promedio))
if (promedio > 95):
    print("¡Felicidades por tu promedio!")
    
print("Adios")
