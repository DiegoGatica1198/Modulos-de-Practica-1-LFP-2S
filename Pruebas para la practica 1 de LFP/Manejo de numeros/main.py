import os 
os.system('cls')
from PS import ValuarPosfijo
from pos import Posfijo
from CalcPos import CalcularPosfijo
from FormatoDeOpareciones import Formato
from CalcPre import ValuarPrefijo


arreglo = ["36","*","2"]
valuar = ValuarPosfijo(arreglo)
print(valuar.ejecutar())

arreglo = ["3","+","2"]
valuar2 = Posfijo(arreglo)
print(valuar2.ejecutar())

arreglo = ["3","2","+"]
valuar3 = CalcularPosfijo(arreglo)
print(valuar3.ejecutar())

problema ="(9.2+21)*pow[10,3]*sqrt[4]+fact[9]-pow[5,2]"
listaWeona = list(problema.upper())
#print(listaWeona)

Formato1 = Formato(listaWeona)
nigga=Formato1.ejecutar()
print(nigga)

problema ="- + 4 * - 3 / - 5 3 10 3 1"
problema = problema.upper()
listaWeona2 = problema.split(" ")
Formato2 = Formato(listaWeona2)
a= Formato2.PalabrasReservadas(listaWeona2)
print(a)

preorder = ValuarPrefijo()
resultado =preorder.ejecutar(a)
print(resultado)