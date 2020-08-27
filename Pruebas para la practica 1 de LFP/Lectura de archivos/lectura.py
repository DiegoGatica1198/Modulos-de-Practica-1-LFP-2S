import os 
os.system('cls')
nombre = input(">>Nombre del archivo: ")
formato = nombre.split(".")
#print(formato[1])
if(formato[1]=="lfp"):
    f = open(nombre, "r")
    print(f.read())
else:
    print("El formato es incorrecto!")
#entrada.lfp
#C:\Users\diego\OneDrive\Desktop\Pruebas para la practica 1 de LFP\Lectura de archivos\entrada.lfp