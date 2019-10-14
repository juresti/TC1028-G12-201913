import os
print(os.getcwd())

def leeArchivo():
    file = open("clase.txt","r")
    string = file.read(7)
    linea = file.readline()
    lista = file.readlines()
    
    print("Con read lei: " + string)
    print("Con readline lei: " + linea)
    print("Con readlines lei: " + str(lista))
    
    file.close()
    
def escribeArchivo(nombreArchivo):
    archivo = open(nombreArchivo + ".txt","w")
    archivo.write("Hola ")
    archivo.write("Mundo\n")
    archivo.write("No se sabe otra?\n")
    archivo.writelines(["Mesa\n","Silla\n","Sí me sé otra\n", "pero me da flojera\n"])
    archivo.close()
    print("Archivo escrito a disco")
    
def agregaInfoArchivo(nombreArchivo):
    arch = open(nombreArchivo + ".txt","a")
    arch.write("A partir de aqui estoy agregando info\n")
    arch.writelines(["Esto ","es ","texto nuevo\n","Bye\n"])
    arch.close()
    print("Archivo actualizado")
    
    
