#Importamos las clases de las unidades
from Unidad1 import Un1
from Unidad2 import Un2
from Unidad3 import Un3

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

#Pedimos al usuario el numero de cifras significativas
cifras = int(input("Cuantas cifras significativas desea "))
#Calculamos el error Es
tolerancia = 0.5 * (10 ** (2 - cifras))

#Saludamos el usuario e implementamos un menu para que el usuario elija
print("..:Bienvenido:..")
menu = int(input("Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))

#La opcion ingresada tiene que estar entre 1 y 5
while menu > 0 and menu < 6:
    #OPPCION 1
    if menu == 1:
        #Desplegamos un menu para que el usuario elija la funcion que desea resolver
        opcion = int(input("Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir "))

        while opcion > 0 and opcion < 13:
            # Creamos una nueva instancia de la clase unidad 1
            Unidad1 = Un1.U1(opcion, tolerancia)
            opcion = int(input("Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir "))

    #OPCION 2
    elif menu == 2:
        #Creamos una nueva instancia de la clase unidad 2
        Unidad2 = Un2.U2(tolerancia)

    #OPCION 3
    elif menu == 3:
        # Creamos una nueva instancia de la clase unidad 2
        Unidad3 = Un3.U3()

menu = int(input(
    "Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))