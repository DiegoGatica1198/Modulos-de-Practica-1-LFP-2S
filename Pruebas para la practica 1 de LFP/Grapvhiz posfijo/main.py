import os 
os.system('cls')
from CalcPosGraphviz import CalcularPosfijoGraphviz



arreglo = ["4","4","*","4.4","3.6","+","/"]
valuar6 = CalcularPosfijoGraphviz(arreglo)
print(valuar6.ejecutar())