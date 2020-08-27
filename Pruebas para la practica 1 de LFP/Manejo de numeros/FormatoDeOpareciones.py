arreglo=[]
arregloAux=[]
arregloDePR=[]
arregloAux2=[]
import re
import math

class Formato:
    def __init__(self, operacion):
        self.operacion = operacion
    def PalabrasReservadas(self,arreglo1):
        arregloAux2 = []
        arregloDePR = arreglo1
        patron1 = r"POW"
        patron2 = r"FACT"
        patron3 = r"SQRT"
        for x in arregloDePR:
            if re.match(patron1,x):
                temp = x.replace("POW[","")
                temp = temp.replace("]","")
                temp = temp.split(",")
                NumTemp = int(temp[0])**int(temp[1])
                arregloAux2.append(str(NumTemp))
            elif re.match(patron2,x):
                temp = x.replace("FACT[","")
                temp = temp.replace("]","")
                NumTemp = math.factorial(int(temp))
                arregloAux2.append(str(NumTemp))
            elif re.match(patron3,x):
                temp = x.replace("SQRT[","")
                temp = temp.replace("]","")
                NumTemp = math.sqrt(int(temp))
                arregloAux2.append(str(NumTemp))
            else:
                arregloAux2.append(x)
        #print(arregloAux2)
        Aux2 = arregloAux2
        return Aux2
    def ejecutar(self):
        Vari=""
        arreglo = self.operacion
        for x in arreglo:
            if x == "(" or x == ")" or x == "+" or x == "-" or x == "*" or x == "/":
                if Vari != "":
                    arregloAux.append(Vari)
                arregloAux.append(x)
                Vari =""
            else:
                Vari = Vari+x
        if Vari != "":
             arregloAux.append(Vari)
        return self.PalabrasReservadas(arregloAux)   
    #def ejecutar2(self,array):
     #   A = self.array
      #  return self.PalabrasReservadas(A)