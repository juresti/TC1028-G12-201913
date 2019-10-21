def pedirDatos():
    nombre = input("Dime el nombre: ")
    dire = input("Dime la dirección: ")
    email = input("Dime el email: ")
    cel = input("Dime el celular: ")
    return nombre,dire,email,cel

def creaDiccionario():
    agenda = {}
    otro = input("¿Quieres agregar persona? (si/no) ")
    while(otro.lower() == "si"):
        name,direc,correo,movil = pedirDatos()
        agenda[name] = [direc,correo,movil]
        otro = input("¿Quieres agregar otra persona? (si/no) ")
    return agenda

def creaLista(agenda):
    salida = []
    for persona in agenda:
        nombre = persona
        listaInfo = agenda[nombre]
        direc = listaInfo[0]
        correo = listaInfo[1]
        cel = listaInfo[2]
        strPersona = nombre + " " + direc + " " + correo + " " + cel + "\n"
        salida.append(strPersona)
    return salida

def guardaAgendaEnArchivo(agenda):
    listaInfo = creaLista(agenda)
    with open("agenda.txt","w") as archivo:
        archivo.writelines(listaInfo)
    print("Agenda guardada en disco")
    
import os
print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\Desktop")
print(os.getcwd())
