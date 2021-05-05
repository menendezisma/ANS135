#FUNCIONES
#Funcion Ea
def Ea(vp, va):
    return abs((vp - va) / vp) * 100

#Funcion tabular
def tabular(va,vp,it):
    while Ea(va, vp) > tolerancia or next(oncemore):
        data.append([it + 1, va, vp, Ea(va, vp)])
        vp = va
        # aumentar en 1 la iteración
        it += 1
        va += g(x, it)

    print(tabulate(data, headers=["It", "Valor Actual", "Valor Pasado", "Error"], tablefmt="pretty"))

try:
    import math
    import sys
    import numpy as np
    from tabulate import tabulate
    from matplotlib import pyplot as plt

except:
    print("Para que el programa funcione bien, tiene que importar el modulo math")
    print("instalar el modulo tabulate,el modulo matplotlib y el modulo numpy\n")
    print("Para instalar tabulate por favor corra\npip install tabulate\npara instalarlo, o \npip3 install tabulate\n")
    print("Para instalar matplotlib por favor corra\npip install matplotlib\npara instalarlo, o \npip3 instal\n")
    print("Para instalar numpy, por favor ejecute\npip install numpy")
    exit()

cifras = int(input("Cuantas cifras significativas desea "))
tolerancia = 0.5 * (10 ** (2 - cifras))

print("..:Bienvenido:..")
menu = int(input("Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))

while menu > 0 and menu < 6:
    if menu == 1:
        opcion = int(
            input("Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)"
                  "\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir "))

        while opcion > 0 and opcion < 13:

            if opcion == 1:
                # opcion 1 Ln(e+x)
                def le(x):
                    e=np.exp(1)
                    return np.log(e+x)
                x=np.linspace(-3,3)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("Ln(e+x)")
                plt.title("F(x)=Ln(e+x)")
                plt.plot(x,le(x))
                plt.show()

            elif opcion == 2:
                # opcion 2 e^(x^2)
                def ex2(x):
                    return np.exp(x**2)
                x=np.linspace(-1,1)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("e*x^2")
                plt.title("F(x)=e*x^2")
                plt.plot(x,ex2(x))
                plt.show()

            elif opcion == 3:
                # opcion 3 sen(x)
                def sen(x):
                    return np.sin(x)

                x=np.linspace(0,10)
                plt.grid()
                plt.title("F(x)=sen(x)")
                plt.ylabel("Sen(x)")
                plt.xlabel("Eje x")
                plt.plot(x,sen(x))
                plt.show()

            elif opcion == 4:
                # opcion 4 cos(x)

                def cos(x):
                    return np.cos(x)
                x=np.linspace(0,10)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("cos(x)")
                plt.title("F(x)=cos(x)")
                plt.plot(x,cos(x))
                plt.show()

                x = float(input("¿Cual es el valor de x?\n"))


                # se define la serie de la funcion
                def g(x, n):
                    return (((-1) ** n) / (math.factorial(2 * n))) * (x ** (2 * n))


                # iteracion
                n = 0
                # valor presente vp
                vp = g(x, n)
                # valor anterior va
                va = 0
                oncemore = iter([True, False])
                data = []

                tabular(vp, va, n)

            elif opcion == 5:
                # opcion 5 e^x

                def ex(x):
                    return np.exp(x)
                x=np.linspace(-3,2)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("e^x")
                plt.title("F(x)=e^x")
                plt.plot(x,ex(x))
                plt.show()

                x = float(input("Cual es el valor de x?\n"))


                # Se define la naturaleza de la función
                def g(x, it):
                    return (x ** it) / math.factorial(it)


                # iteración: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                tabular(va, vp, it)

            elif opcion == 6:
                # opcion 6 sh(x)
                def sh(x):
                    return np.sinh(x)
                x = np.linspace(-3, 3)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("sinh(x)")
                plt.title("F(x)=sinh(x)")
                plt.plot(x,sh(x))
                plt.show()


            elif opcion == 7:
                # opcion 7 ch(x)
                def ch(x):
                    return np.cosh(x)
                x = np.linspace(-3, 3)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("cosh(x)")
                plt.title("F(x)=cosh(x)")
                plt.plot(x, ch(x))
                plt.show()


            elif opcion == 8:
                # opcion 8 arcsen(x)
                def arcsen(x):
                    return np.arcsin(x)
                x = np.linspace(-1, 1)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("arcsin(x)")
                plt.title("F(x)=arcsin(x)")
                plt.plot(x, arcsen(x))
                plt.show()


            elif opcion == 9:
                # opcion 9 ln(1+x)

                def ln(x):
                    return np.log(1+x)
                x=np.linspace(-3,5)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("Ln(1+x)")
                plt.title("F(x)=Ln(1+x)")
                plt.plot(x,ln(x))
                plt.show()

                x = float(input("Cual es el valor de x?\n"))
                if not (-1 < x < 1):
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()


                # Se define la naturaleza de la función
                def g(x, it):
                    return (((-1) ** (it)) / (it + 1)) * (x ** (it + 1))


                # iteración: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                tabular(va, vp, it)

            elif opcion == 10:
                # opcion 10 1/(1+x^2)

                def cociente(x):
                    return 1/(1+x**2)
                x=np.linspace(-3,3)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("1/(1+x^2)")
                plt.title("F(x)=1/(1+x^2)")
                plt.plot(x,cociente(x))
                plt.show()

                x = float(input("Cual es el valor de x?\n"))
                if not (-1 < x < 1):
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()


                # Se define la naturaleza de la función
                def g(x, it):
                    return ((-1) ** (it)) * (x ** (2 * it))


                # iteración: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                tabular(va, vp, it)

            elif opcion == 11:
                # opcion 11 arctg(x)

                def arctg(x):
                    return np.arctan(x)
                x=np.linspace(-4,4)
                plt.grid()
                plt.xlabel("Eje x")
                plt.ylabel("arctg(x)")
                plt.title("F(x)=arctg(x)")
                plt.plot(x,arctg(x))
                plt.show()

                x = float(input("Cual es el valor de x?\n"))
                if not (-1 < x < 1):
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()


                # Se define la naturaleza de la función
                def g(x, it):
                    return (((-1) ** (it)) * (x ** ((2 * it) + 1))) / ((2 * it) + 1)


                # iteración: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                tabular(va, vp, it)

            elif opcion==12:
                sys.stdout.flush()

            else:
                seguir = 1

            opcion = int(input("Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)"
                      "\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir "))

    menu = int(input("Ingrese el numero de la opcion deseada\n1.Unidad 1\n2.Unidad 2\n3.Unidad 3\n4.Unidad 4\n5.Unidad 5\nOtro numero para salir "))
