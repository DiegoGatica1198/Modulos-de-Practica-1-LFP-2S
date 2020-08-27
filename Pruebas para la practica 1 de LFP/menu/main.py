import os 
os.system('cls')

control = True
while(control):
    os.system('cls')
    print("--------------------------------------------------------------")
    print("------------------------Practica 1----------------------------")
    print("Nombre: Diego Andres Gatica Contreras")
    print("Carnet: 201801405")
    print("Curso: Lenguajes formales y de programacion")
    print("Seccion: ")
    print("--------------------------------------------------------------")
    print("")
    print("-----------------------------Menu-----------------------------")
    print("| Este es el menu de la practica 1 de lenguajes formales y   |")
    print("| de programacion, a continuacion puede elegir entre los     |")
    print("| diferentes modulos del programa, ingrese la opcion que     |")
    print("| desea ejecutar:                                            |")
    print("--------------------------------------------------------------")
    print("1. Cargar Archivo")
    print("2. Graficar Operacion")
    print("3. Salir")
    opcion = input(">>Ingrese una opcion: ")
    if(opcion =="1"):
        os.system('cls')
        print("Ha seleccionado la opcion 1 (Cargar archivo)")
        pausa = input()
    elif(opcion =="2"):
        os.system('cls')
        print("Ha seleccionado la opcion 2 (Graficar Operacion)")
        pausa = input()
    elif(opcion =="3"):
        os.system('cls')
        print("Ha seleccionado la opcion 3 (Salir)")
        print("Adios! :)")
        pausa = input()
        control=False
    else:
        os.system('cls')
        print("Usted no selecciono una opcion valida \nPor favor vuelva a intentarlo")
        pausa = input()