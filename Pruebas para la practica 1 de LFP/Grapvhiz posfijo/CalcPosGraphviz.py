from graphviz import Digraph

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

class CalcularPosfijoGraphviz:
    def __init__(self, arreglo):
        self.arreglo = arreglo
    def ejecutar(self):
        f = Digraph(format='png', name='grafico')
        f.attr(rankdir='TB', size='8')
        f.attr('node', shape='plaintext')
        EP = self.arreglo
        NumeroDeNodo=1
        for x in range(len(EP)):
            for y in range(len(arregloVariables)):
                aux = arregloVariables[y]
                if EP[x]==aux[0].upper():
                    EP[x]=aux[1]
        
        if len(EP) >= 3:
            
            pilaAuxiliar = []
            resultadoFinal = 0
            contador=0
            xd = 0
            cadena = "<<table>"
            while xd < len(EP):
                cadena = cadena + "<tr><td>   </td></tr>"
                xd = xd+1
            cadenaFinal = "</table>>"
            f.node('0', cadena + cadenaFinal)
            
            for posicion in EP:
                oper=""
                pilaGraph=[]
                for x in pilaAuxiliar:
                    pilaGraph.append(x)
                
                if posicion != "+" and posicion != "-" and posicion != "*" and posicion != "/" and posicion != "(" and posicion != ")":
                    pilaAuxiliar.append(posicion)
                    contador+=1
                else:
                    valor1 = pilaAuxiliar.pop()
                    valor2 = pilaAuxiliar.pop()
                    operador = posicion
                    oper=posicion
                    contador+=1
                    if operador =="+":
                        valAux = float(valor2) + float(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="-":
                        valAux = float(valor2) - float(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="*":
                        valAux = float(valor2) * float(valor1)
                        pilaAuxiliar.append(valAux)
                    elif operador =="/":
                        valAux = float(valor2) / float(valor1)
                        pilaAuxiliar.append(valAux)
                if contador == len(EP):
                    resultadoFinal= pilaAuxiliar[0]

                if oper != "":
                    pilaGraph.append(oper)
                
                if len(pilaGraph)>len(pilaAuxiliar):
                    largo = len(EP)
                    largo2 = largo-len(pilaGraph)
                    cadena = "<<table>"
                    cadenaFinal = "</table>>"
                    x=0
                    while x < largo2:
                        cadena = cadena + "<tr><td>   </td></tr>"
                        x=x+1
                    x=len(pilaGraph)
                    y=0
                    while y<x:
                        cadena = cadena + "<tr><td>"+str(pilaGraph[x-y-1])+"</td></tr>"
                        y=y+1
                    f.node(str(NumeroDeNodo), cadena + cadenaFinal)
                    NumeroDeNodo = NumeroDeNodo +1
                    print("----------")                    
                    print(pilaGraph)
                
                print(pilaAuxiliar)
                largo = len(EP)
                largo2 = largo-len(pilaAuxiliar)
                cadena = "<<table>"
                cadenaFinal = "</table>>"
                x=0
                while x < largo2:
                    cadena = cadena + "<tr><td>   </td></tr>"
                    x=x+1
                x=len(pilaAuxiliar)
                y=0
                while y<x:
                    cadena = cadena + "<tr><td>"+str(pilaAuxiliar[x-y-1])+"</td></tr>"
                    y=y+1
                f.node(str(NumeroDeNodo), cadena + cadenaFinal)
                NumeroDeNodo = NumeroDeNodo +1
        else:
            if len(EP) == 1:
                resultadoFinal = EP[0]
            else:
                resultadoFinal = EP[1]+EP[0]
        f.view()
        return resultadoFinal