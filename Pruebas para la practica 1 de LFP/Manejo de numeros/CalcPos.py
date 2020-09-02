var = ["Nombre",0]
arregloVariables = [var]
N=50
pila=[]
EP=[]
tope=-1

#Esto es si ponen variables
abcd=list('ABCDEFGHIJKLMNOPQRSTUVXYZ')
#Esto es si solo ponen numeros hasta 100000
udt=list('01')
for x in range(100000):
    udt.append(str(x+2))

class CalcularPosfijo:
    def __init__(self, arreglo):
        self.arreglo = arreglo
    def ejecutar(self):
        EP = self.arreglo
        for x in range(len(EP)):
            for y in range(len(arregloVariables)):
                aux = arregloVariables[y]
                if EP[x]==aux[0].upper():
                    EP[x]=aux[1]
        
        if len(EP) >= 3:
            pilaAuxiliar = []
            resultadoFinal = 0
            contador=0
            for posicion in EP:
                if posicion != "+" and posicion != "-" and posicion != "*" and posicion != "/" and posicion != "(" and posicion != ")":
                    pilaAuxiliar.append(posicion)
                    contador+=1
                else:
                    valor1 = pilaAuxiliar.pop()
                    valor2 = pilaAuxiliar.pop()
                    operador = posicion
                    contador+=1
                    if operador =="+":
                        valAux = int(valor2) + int(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="-":
                        valAux = int(valor2) - int(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="*":
                        valAux = int(valor2) * int(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="/":
                        valAux = int(valor2) / int(valor1)
                        pilaAuxiliar.append(valAux)
                if contador == len(EP):
                    resultadoFinal= pilaAuxiliar[0]
        else:
            if len(EP) == 1:
                resultadoFinal = EP[0]
            else:
                resultadoFinal = EP[1]+EP[0]
        return resultadoFinal