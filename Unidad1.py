#Importamos las librerias a utilizar
import math
import sys
import numpy as np
from tabulate import tabulate
from matplotlib import pyplot as plt

#Creamos la clase Un1
class Un1:
    #Creamos la funcion U1 y le pasamos los argumentos opcion y tol
    def U1(tol):
        # Funcion Ea
        def Ea(vp, va):
            return abs((vp - va) / vp) * 100

        # Funcion tabular
        def tabular(va, vp, it, toleran=tol):
            while Ea(va, vp) > toleran or next(oncemore):
                #Creamos una tabla y le mandamos los datos
                data.append([it + 1, va, vp, Ea(va, vp)])
                vp = va
                # aumentar en 1 la iteracion
                it += 1
                va += g(x, it)

            #Imprimimos la tabla
            print(tabulate(data, headers=["It", "Valor Actual", "Valor Pasado", "Error"], tablefmt="pretty"))

        # Desplegamos un menu para que el usuario elija la funcion que desea resolver
        opcion = int(input("\x1b[3;32m" + "Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir " + "\x1b[0;30m"))
        while opcion > 0 or opcion < 13:
            # Si la opcion elejida fue 1
            if opcion == 1:
                # opcion 1 Ln(e+x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def le(x):
                    e = np.exp(1)
                    return np.log(e + x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 3)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("Ln(e+x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=Ln(e+x)")
                # Graficamos nuestra funcion
                plt.plot(x, le(x))
                # Mostramos la grafica al usuario
                plt.show()

            # Si la opcion elejida fue 2
            elif opcion == 2:
                # opcion 2 e^(x^2)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def ex2(x):
                    return np.exp(x ** 2)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-1, 1)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("e*x^2")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=e*x^2")
                # Graficamos nuestra funcion
                plt.plot(x, ex2(x))
                # Mostramos la grafica al usuario
                plt.show()

            # Si la opcion elejida fue 3
            elif opcion == 3:
                # opcion 3 sen(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def sen(x):
                    return np.sin(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(0, 10)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.ylabel("Sen(x)")
                plt.xlabel("Eje x")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=sen(x)")
                # Graficamos nuestra funcion
                plt.plot(x, sen(x))
                # Mostramos la grafica al usuario
                plt.show()

                cifras = -1
                ea = 1000

                while (cifras < 0):
                    cifras = int(input("ingrese la cantidad de cifras significativas "))
                    if (cifras < 0):
                        print("el numero que ingreso no es valido")
                    else:
                        es = (0.5 * (10 ** (2 - cifras)))

                # Pedimos el valor de x para evaluar la funcion
                x = float(input("ingrese el valor de x "))
                value = math.sin(x)
                aprox = x
                n = 1

                while (ea > es):
                    ant = aprox
                    aprox = aprox + (((-1) ** n) * (x ** (2 * n + 1)) / math.factorial(2 * n + 1))
                    # Calculamos el Ea
                    ea = abs(((aprox - ant) / aprox) * 100)
                    print("iteracion ", n)
                    print("valor aproximado ", aprox)
                    print("error aproximado ", ea)
                    n = n + 1
                print(value)
                print("el valor es: ", aprox)
                print("el error es: ", ea)

            # Si la opcion elejida fue 4
            elif opcion == 4:
                # opcion 4 cos(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def cos(x):
                    return np.cos(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(0, 10)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("cos(x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=cos(x)")
                # Graficamos nuestra funcion
                plt.plot(x, cos(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario el valor de x
                x = float(input("¿Cual es el valor de x? \n"))

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

                # Pasamos los parametros a la funcion tabular
                tabular(vp, va, n)

            # Si la opcion elejida fue 5
            elif opcion == 5:
                # opcion 5 e^x
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def ex(x):
                    return np.exp(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 2)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("e^x")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=e^x")
                # Graficamos nuestra funcion
                plt.plot(x, ex(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario el valor de x
                x = float(input("Cual es el valor de x? \n"))

                # Se define la naturaleza de la funcion
                def g(x, it):
                    return (x ** it) / math.factorial(it)

                # iteracion: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                # Pasamos lo parametros a la funcion tabular
                tabular(va, vp, it)

            # Si la opcion elejida fue 6
            elif opcion == 6:
                # opcion 6 sh(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def sh(x):
                    return np.sinh(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 3)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("sinh(x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=sinh(x)")
                # Graficamos nuestra funcion
                plt.plot(x, sh(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario las cifras significativas y calculamos el error
                cifras = int(input("¿Cuantas cifras significativas desea? "))
                tolerancia = 0.5 * (10 ** (2 - cifras))

                # Pedimos al usuario el valor de x
                x = float(input("¿Cual es el valor de x? \n"))

                # se define la serie de la funcion
                def g(x, n):
                    return (1 / (math.factorial((2 * n) + 1))) * (x ** ((2 * n) + 1))

                # Se encuentra Ea
                def Ea(vp, va):
                    return abs((vp - va) / vp) * 100

                # iteracion
                n = 0

                # valor presente vp
                vp = g(x, n)

                # valor anterior va
                va = 0

                oncemore = iter([True, False])
                data = []

                while Ea(vp, va) > tolerancia or next(oncemore):
                    data.append([n + 1, vp, va, Ea(vp, va)])
                    va = vp
                    # aumentamos 1 a n
                    n += 1
                    vp += g(x, n)
                    # Imprimimos la tabla
                print(tabulate(data, headers=["It", "Valor presente", "Valor anterior", "Er"], tablefmt="orgtbl"))

            # Si la opcion elejida fue 7
            elif opcion == 7:
                # opcion 7 ch(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def ch(x):
                    return np.cosh(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 3)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("cosh(x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=cosh(x)")
                # Graficamos nuestra funcion
                plt.plot(x, ch(x))
                # Mostramos la grafica al usuario
                plt.show()

            # Si la opcion elejida fue 8
            elif opcion == 8:
                # opcion 8 arcsen(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def arcsen(x):
                    return np.arcsin(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-1, 1)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("arcsin(x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=arcsin(x)")
                # Graficamos nuestra funcion
                plt.plot(x, arcsen(x))
                # Mostramos la grafica al usuario
                plt.show()

                cifras = -1
                ea = 1000

                while (cifras < 0):
                    cifras = int(input("ingrese la cantidad de cifras significativas "))
                    if (cifras < 0):
                        print("el numero que ingreso no es valido")
                    else:
                        es = (0.5 * (10 ** (2 - cifras)))

                # Pedimos al usuario el valor de x
                x = float(input("ingrese el valor de x, intervalo[-1,1]"))
                while (x < -1 or x > 1):
                    # Si el numero no esta en el intervalo dado le devuelve el mensaje
                    print("ha ingresado un numero que no se encuentra en el intervalo")
                    # Pedimos al usuario el valor de x
                    x = float(input("ingrese el valor de x "))

                aprox = x + ((1 / 2) * (((x) ** 3) / 3))
                n = 2

                while (ea > es):
                    ant = aprox
                    aprox = aprox + (((math.factorial(2 * n)) / (((2 ** n) * math.factorial(n)) ** 2)) * (
                            (x ** ((2 * n) + 1)) / ((2 * n) + 1)))
                    ea = abs(((aprox - ant) / aprox) * 100)
                    print("iteracion ", n)
                    print("valor aproximado ", aprox)
                    print("error aproximado ", ea)
                    n = n + 1
                print("el valor es: ", aprox)
                print("el error es: ", ea)

            # Si la opcion elejida fue 9
            elif opcion == 9:
                # opcion 9 ln(1+x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def ln(x):
                    return np.log(1 + x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 5)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("Ln(1+x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=Ln(1+x)")
                # Graficamos nuestra funcion
                plt.plot(x, ln(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario el valor de x
                x = float(input("Cual es el valor de x? \n"))
                if not (-1 < x < 1):
                    # Si el numeor no se encuentra en el intervalo dado devuelve el mensaje
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()

                # Se define la naturaleza de la funcion
                def g(x, it):
                    return (((-1) ** (it)) / (it + 1)) * (x ** (it + 1))

                # iteracion: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                # Pasamos lo parametros a la funcion tabular para que se imprima la tabla
                tabular(va, vp, it)

            # Si la opcion elejida fue 10
            elif opcion == 10:
                # opcion 10 1/(1+x^2)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def cociente(x):
                    return 1 / (1 + x ** 2)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-3, 3)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("1/(1+x^2)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=1/(1+x^2)")
                # Graficamos nuestra funcion
                plt.plot(x, cociente(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario el valor de x
                x = float(input("Cual es el valor de x? \n"))
                if not (-1 < x < 1):
                    # Si el valor no esta en el intervalo dado devuelve el mensaje
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()

                # Se define la naturaleza de la funcion
                def g(x, it):
                    return ((-1) ** (it)) * (x ** (2 * it))

                # iteracion: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp
                vp = 0

                oncemore = iter([True, False])
                data = []
                # Pasa los parametros a la funcion tabular para crear nuestra tabla
                tabular(va, vp, it)

            # Si la opcion elejida fue 11
            elif opcion == 11:
                # opcion 11 arctg(x)
                # Creamos la funcion para poder evaluar los puntos y graficarla
                def arctg(x):
                    return np.arctan(x)

                # Desinamos un rango de datos para graficar la funcion
                x = np.linspace(-4, 4)
                # Creamos una cuadricula
                plt.grid()
                # Colocamos las etiquetas a los ejes
                plt.xlabel("Eje x")
                plt.ylabel("arctg(x)")
                # Repintamos los eje x e y
                plt.axhline(y=0, color="k")
                plt.axvline(x=0, color="k")
                # Colocamos un nombre al grafico
                plt.title("F(x)=arctg(x)")
                # Graficamos nuestra funcion
                plt.plot(x, arctg(x))
                # Mostramos la grafica al usuario
                plt.show()

                # Pedimos al usuario el valor de x
                x = float(input("Cual es el valor de x? \n"))
                if not (-1 < x < 1):
                    # Si el valor no es el esperado devulve el mensaje
                    print("El valor de \"x\" tiene que ser mayor a -1 y menor a 1")
                    exit()

                # Se define la naturaleza de la funcion
                def g(x, it):
                    return (((-1) ** (it)) * (x ** ((2 * it) + 1))) / ((2 * it) + 1)

                # iteracion: it
                it = 0
                # valor actual: va
                va = g(x, it)
                # valor pasado: vp}
                vp = 0

                oncemore = iter([True, False])
                data = []
                # Pasamos lo parametros a la funcion tabular para crear nuestra tabla
                tabular(va, vp, it)

            else:
                break;

            opcion = int(input("\x1b[3;32m" + "Ingrese el numero del ejercicio que desea ver la solucion\n1.Ln(e+x)\n2.e^(x^2)\n3.sen(x)\n4.cos(x)\n5.e^x\n6.sh(x)\n7.ch(x)\n8.arcsen(x)\n9.Ln(1+x)\n10.1/(1+x^2)\n11.arctg(x)\n12.Limpiar consola\nOtro numero para salir " + "\x1b[0;30m"))
