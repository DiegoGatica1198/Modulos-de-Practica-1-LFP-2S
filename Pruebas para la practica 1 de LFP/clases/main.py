from resta import *
from multiplicacion import *
from division import *
from suma import *

import os 
os.system('cls')

div1 = divObj()
sum1 = sumaObj()
mult1 = multiObj()
rest1 = restaObj()

print(rest1.operacion(2,3))

control=True
while(control):
    os.system('cls')
    print("-----------------------------------------------------------------------------------------")
    print("hi! this is a test of a very basic calculator")
    print("now, you can choose an option")
    print("dependig of which option you want introduce a number corespondig to what you want to do")
    print("1-sum 2-substraction 3-multiplication 4-division")
    print("input anything else if you want to exit")
    opcion = input(">>")
    if(opcion=="1"):
        print("you chose to sum")
        x=input("number 1 >>")
        x=int(x)
        y=input("number 2 >>")
        y=int(y)
        print("answer: "+str(sum1.operacion(x,y)))
        pas = input()
        print("---------------------------------------------------------------------------------------------------")
    elif(opcion=="2"):
        print("you chose to substraction")
        x=input("number 1 >>")
        y=input("number 2 >>")
        x=int(x)
        y=int(y)
        print("answer: "+str(rest1.operacion(x,y)))
        pas = input()
        print("---------------------------------------------------------------------------------------------------")
    elif(opcion=="3"):
        print("you chose to multiplication")
        x=input("number 1 >>")
        y=input("number 2 >>")
        x=int(x)
        y=int(y)
        print("answer: "+str(mult1.operacion(x,y)))
        pas = input()
        print("---------------------------------------------------------------------------------------------------")
    elif(opcion=="4"):
        print("you chose to division")
        x=input("number 1 >>")
        y=input("number 2 >>")
        x=int(x)
        y=int(y)
        print("answer: "+str(div1.operacion(x,y)))
        pas = input()
        print("---------------------------------------------------------------------------------------------------")
    else:
        print("good bye")
        control=False
