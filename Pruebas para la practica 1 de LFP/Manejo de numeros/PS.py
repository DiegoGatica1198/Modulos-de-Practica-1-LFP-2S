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

class ValuarPosfijo:
    def __init__(self, arreglo):
        self.arreglo = arreglo
    def ejecutar(self):        
        def llena():
            if(tope==(N-1)):
                print('STACKOVERFLOW')
                return True
            return False

        def vacia():
            if(tope==-1):
                'STACKUNDERFLOW'
                return True
            return False

        def push(dato):
            if(llena()!=True):
                global tope
                tope=tope+1
                pila.insert(tope,dato)
        def pop():
            if(vacia()!=True):
                global tope
                aux=pila[tope]
                del pila[tope]
                tope=tope-1
                return aux
            else:
                return -9999

        def infijo(i, EI):
            if(EI[i]=='^'):
                prioridadop=4
                return prioridadop
            elif(EI[i]=='*'):
                prioridadop=2
                return prioridadop
            elif(EI[i]=='/'):
                prioridadop=2
                return prioridadop
            elif(EI[i]=='+'):
                prioridadop=1
                return prioridadop
            elif(EI[i]=='-'):
                prioridadop=1
                return prioridadop
            elif(EI[i]=='('):
                prioridadop=5
                return prioridadop

        def pripila(pila):
            if(pila[tope]=='^'):
                prioridadpi=3
                return prioridadpi
            elif(pila[tope]=='*'):
                prioridadpi=2
                return prioridadpi
            elif(pila[tope]=='/'):
                prioridadpi=2
                return prioridadpi
            elif(pila[tope]=='+'):
                prioridadpi=1
                return prioridadpi
            elif(pila[tope]=='-'):
                prioridadpi=1
                return prioridadpi
            elif(pila[tope]=='('):
                prioridadpi=0
                return prioridadpi


        eistring= self.arreglo
        texto = eistring#.upper()
        textoSeparado = list(texto)
        NuevaCadena = []
        cadenaDeNumeros = ""

        for numero in range(len(textoSeparado)):
            if textoSeparado[numero] != "+" and textoSeparado[numero] != "-" and textoSeparado[numero] != "*" and textoSeparado[numero] != "/" and textoSeparado[numero] != "(" and textoSeparado[numero] != ")":
                cadenaDeNumeros += textoSeparado[numero]
            else:
                if cadenaDeNumeros != "":
                    NuevaCadena.append(cadenaDeNumeros)
                cadenaDeNumeros = ""
                NuevaCadena.append(textoSeparado[numero])
            if numero+1 == len(textoSeparado):
                if cadenaDeNumeros != "":
                    NuevaCadena.append(cadenaDeNumeros)
        #print(NuevaCadena)
        #EI=list(NuevaCadena.upper())
        EI=list(NuevaCadena)


        for i in range(len(EI)):
            if(EI[i] in abcd or EI[i] in udt):      #EI es operando
                EP.append(EI[i])
            elif(EI[i]!=')'):                       #EI es diferente a ')'
                if (tope==-1):                      #Pila no esta vacia
                    push(EI[i])
                else:
                    if(infijo(i,EI)<=pripila(pila)):#operador de EI es <= a operador de pila
                        EP.append(pop())                
                        push(EI[i])
                    elif(infijo(i,EI)>pripila(pila)):#operador de EI es > a operador de pila
                        push(EI[i])
            elif(EI[i]==')'):                       #EI es igual a ')'
                while (pila[tope]!='('):            #Pila es diferente a '('
                    EP.append(pop())
                if(pila[tope]=='('):                #Pila es igual a '('
                    pop()
                elif(tope!=-1):                     #Pila no esta vacia
                    EP.append(pop())

        while (tope>-1):                
            EP.append(pop())

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