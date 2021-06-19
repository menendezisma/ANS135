#Importamos las clases de las unidades
from Unidad1 import Un1
from Unidad2 import Un2
from Unidad3 import Un3
from Unidad5 import Un5
from Integracion_Numerica import Integracion
from Diferenciacion_Numerica import Diferenciacion

#Creamos un try/catch para evitar que el usuario corra el codigo sin haber instalado las librerias
try:
    import math
    import sys
    import numpy as np
    from numpy import sign
    from tabulate import tabulate
    from matplotlib import pyplot as plt

except:
    #Devolvemos al usuario los respectivos mensajes para solucionar la excepcion
    print("Para que el programa funcione bien, tiene que importar el modulo math")
    print("instalar el modulo tabulate,el modulo matplotlib y el modulo numpy\n")
    print("Para instalar tabulate por favor corra\npip install tabulate\npara instalarlo, o \npip3 install tabulate\n")
    print("Para instalar matplotlib por favor corra\npip install matplotlib\npara instalarlo, o \npip3 instal\n")
    print("Para instalar numpy, por favor ejecute\npip install numpy")
    exit()

#try:
# Saludamos el usuario e implementamos un menu para que el usuario elija
print("\x1b[1;34m" + "..............................:Bienvenido:.............................."+"\x1b[0;31m")
print("\x1b[3;31m"+"--------------- Recomendaciones para el uso del programa---------------\n"+"\x1b[3;31m")
print("Los terminos de las expresiones deben ir con un * entre ellas\npara usar la raiz cuadrada use sqrt()")
print("para las funciones trogonometricas use: sin(), cos(), tan()\npara usar la funcion exponencial use exp()\nsi solo desea elevar a una potencia use **")
print("------------------------------------------------------------------------"+"\x1b[1;34m")

try:
     #Pedimos al usuario el numero de cifras significativas
     cifras = int(input("Cuantas cifras significativas desea "))
     # Calculamos el error Es
     tolerancia = 0.5 * (10 ** (2 - cifras))
except:
    print("\x1b[1;31m"+"Ingrese un numero valido")
    exit()

menu = int(input("\x1b[1;34m"+"Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))

# La opcion ingresada tiene que estar entre 1 y 5
while menu > 0 or menu < 6:
    # OPCION 1
    if menu == 1:
        # Creamos una nueva instancia de la clase unidad 1
        Unidad1 = Un1.U1(tolerancia)

    # OPCION 2
    elif menu == 2:
        # Creamos una nueva instancia de la clase unidad 2
        Unidad2 = Un2.U2(tolerancia)

    # OPCION 3
    elif menu == 3:
        # Creamos una nueva instancia de la clase unidad 3
        Unidad3 = Un3.U3(self=None)

    #OPCION 4
    elif menu == 4:
        #Creamos una instancia nueva de la unidad 4
        integracion=int(input("\x1b[3;32m" + "Ingrese el numero de la opcion deseada\n1.Derivacion numerica\n2.Integracion numerica\nOtro numero para salir " + "\x1b[0;30m"))
        while integracion > 0 and integracion < 5:
            if integracion==1:
                DifNum=Diferenciacion()
            if integracion==2:
                IntNum = Integracion()
            else:
                break
        integracion=int(input("\x1b[3;32m" + "Ingrese el numero de la opcion deseada\n1.Derivacion numerica\n2.Integracion numerica\nOtro numero para salir " + "\x1b[0;30m"))

    elif menu==5:
        Unidad5=Un5.U5()
    else:
        break

    menu = int(input("\x1b[1;34m"+"Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))
'''except:
    print("\x1b[1;31m"+"Ingrese un numero valido")
    exit()'''