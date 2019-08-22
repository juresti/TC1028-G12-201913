cal1 = int(input("Dime la calificación del parcial 1: "))
cal2 = int(input("Dime la calificación del parcial 2: "))
cal3 = int(input("Dime la calificación del parcial 3: "))

if ((cal1 >= 0) and (cal1 <= 100)):
    print("Calificacion válida")
else:
    print("Valor inválido de calificación 1")
    print("Resultados no serán confiables")

if ((cal2 >= 0) and (cal2 <= 100)):
    print("Calificacion válida")
else:
    print("Valor inválido de calificación 2")
    print("Resultados no serán confiables")

if ((cal3 >= 0) and (cal3 <= 100)):
    print("Calificacion válida")
else:
    print("Valor inválido de calificación 3")
    print("Resultados no serán confiables")


promedio = (cal1 + cal2 + cal3) / 3

print("Tu promedio es {0} en este periodo".format(promedio))
if (promedio > 95):
    print("¡Felicidades por tu promedio!")
    
print("Adios")
