EP=[]

class ValuarPrefijo:
    def __init__(self):
        placeholder=1
    def ejecutar(self,arreglo):
        if len(arreglo)==3:
            print("esta esta paja")
            if arreglo[0]=="+":
                x=float(arreglo[1])+float(arreglo[2])
                return x
            elif arreglo[0]=="-":
                x=float(arreglo[1])-float(arreglo[2])
                return x
            elif arreglo[0]=="*":
                x=float(arreglo[1])*float(arreglo[2])
                return x
            elif arreglo[0]=="/":
                x=float(arreglo[1])/float(arreglo[2])
                return x
        else:
            print("esta pisada hommie")
            Largo = len(arreglo)
            contador = 0
            valorDeRemplazo=0
            arregloAux=[]
            while contador<Largo:
                if arreglo[contador] =="+" or arreglo[contador] =="*" or arreglo[contador] =="-" or arreglo[contador] =="/":
                    if arreglo[contador+1] !="+" and arreglo[contador+1] !="*" and arreglo[contador+1] !="-" and arreglo[contador+1] !="/":
                        if arreglo[contador+2] !="+" and arreglo[contador+2] !="*" and arreglo[contador+2] !="-" and arreglo[contador+2] !="/":
                            if arreglo[contador]=="+":
                                x=float(arreglo[contador+1])+float(arreglo[contador+2])
                                valorDeRemplazo=x
                                arregloAux.append(str(valorDeRemplazo))
                                contador = contador+3
                                break
                            elif arreglo[contador]=="-":
                                x=float(arreglo[contador+1])-float(arreglo[contador+2])
                                valorDeRemplazo=x
                                arregloAux.append(str(valorDeRemplazo))
                                contador = contador+3
                                break
                            elif arreglo[contador]=="*":
                                x=float(arreglo[contador+1])*float(arreglo[contador+2])
                                valorDeRemplazo=x
                                arregloAux.append(str(valorDeRemplazo))
                                contador = contador+3
                                break
                            elif arreglo[contador]=="/":
                                x=float(arreglo[contador+1])/float(arreglo[contador+2])
                                valorDeRemplazo=x
                                arregloAux.append(str(valorDeRemplazo))
                                contador = contador+3
                                break
                arregloAux.append(arreglo[contador])
                contador = contador+1
            while contador<Largo:
                arregloAux.append(arreglo[contador])
                contador = contador+1
            print(arregloAux)
            return self.ejecutar(arregloAux)
