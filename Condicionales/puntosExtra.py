calif = int(input("Dime tu calificación: "))
extra = 0

if (calif >= 95):
    print("5 puntos extra")
    extra = 5
elif (calif >= 90):
    print("4 puntos extra")
    extra = 4
elif (calif >= 85):
    print("3 puntos extra")
    extra = 3
elif (calif >= 80):
    print("2 puntos extra")
    extra = 2

if ((calif < 0) or (calif > 100)):
    print("Calificación no válida")
else:    
    nueva_calif = calif + extra
    print(nueva_calif)
    

