edad = int(input("Dime tu edad: "))

if (edad > 18):
    if(edad < 50):
        divertir = input("Tienes ganas de divertirte (Si/No)? ")
        if(divertir == "Si"):
            print("Puedes pasar")
        else:
            print("Debes de tener ganas de divertirte")
    else:                
        print("Estas muy ruco... no pasas")
else:
    print("Estas muy chavo... no pasas...")