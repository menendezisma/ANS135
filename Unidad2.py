#Importamos las librerias necesarias
import numpy as np
import sympy as sp
from math import *
from numpy import sign
from tabulate import tabulate
from matplotlib import pyplot as plt

#Creamos la clase U2
class Un2:
    #Definimos la funcion U2 que recibe el argumento tolerancia
    def U2(tolerancia):
        #Solicitamos al usuario que ingresa la funcion exponencial
        f = input("\x1b[1;33m"+"Introduce la funcion exponencial en terminos de x "+"\x1b[1;36m")
        if "exp(x)" in f:
            fx=f.replace('exp(x)','e**x')
        elif "exp(-x)" in f:
            fx = f.replace('exp(-x)', 'e**-x')
        #Le mostramos la funcion al usuario para verificar que es correcta
        print(fx)
        #Validamos que en realidad se trate de una funcion exponencial
        if "**x" in fx or "exp(x" in fx or "exp(-x" in fx or "**-x" in fx:
            #Desplegamos un menu para que el usuario elija el metodo a utilizar
            metodo = int(input("\x1b[3;36m"+"Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n"
                "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Müller\nOtro numero para salir\n"+"\x1b[1;36m"))

            while metodo > 0 and metodo < 8:
                #Opcion 1 Grafico
                if metodo == 1:
                    # Le colocamos un estilo
                    plt.style.use('classic')
                    #Definimos el rango de datos a evaluar la funcion
                    x = np.linspace(-2, 4)
                    #creamos la variable ejey que almacenara los valores de la funcion evaluada en x
                    ejey = eval(fx)
                    #creamos una cuadricula en nuestra grafica
                    plt.grid()
                    #Le ponemos titulo a nuestra grafica
                    plt.title(fx)
                    #Colocamos nombres a nuestros ejes
                    plt.xlabel("Eje x")
                    plt.ylabel("F(x)=" + fx)
                    #Repintanmos los ejes x e y
                    plt.axhline(y=0, color="k")
                    plt.axvline(x=0, color="k")
                    #Graficamos nuestra funcion
                    plt.plot(x, ejey)
                    #Mostramos nuestra grafica
                    plt.show()

                #Opcion 2 Biseccion
                elif metodo == 2:
                    #Solicitamos el primer valor
                    x = float(input("\x1b[0;30m"+"Ingrese el valor para x1 "))
                    #Almacenamos el valor x en otra variable
                    x1 = x
                    #Evaluamos nuestro valor x1 en la funcion fx
                    fx1 = eval(fx)
                    # Solicitamos el segundo valor
                    x = float(input("Ingrese el valor para x2 "))
                    # Almacenamos el valor x en otra variable
                    x2 = x
                    # Evaluamos nuestro valor x2 en la funcion fx
                    fx2 = eval(fx)

                    if sign(fx1) != sign(fx2):
                        print("\nEl intervalo si contiene una raiz")
                    else:
                        print("\x1b[1;31m"+"Ingrese un intervalo valido"+"\x1b[0;30m")

                    it = 0
                    #Encontramos el punto medio inicial
                    xri = (x1 + x2) / 2
                    xrf = 100
                    #creamos una tabla vacia
                    data = []
                    oncemore = iter([True, False])
                    E = 100
                    #calculamos la raiz hasta que el Ea sea Es
                    while E > tolerancia:
                        # Se encuentra xr
                        #Obtenemos lo segundos valores
                        x = x1
                        #evaluamos los segundos valores en la funcion fx
                        fx1 = eval(fx)
                        #almacenamos los valores iniciales en otras variables para ser reutilizados
                        x11 = x1
                        x22 = x2
                        #encontramos el nuevo punto medio
                        xr = (x11 + x22) / 2
                        x = xr
                        #Evaluamos la funcion en el punto medio
                        fxr = eval(fx)

                        E = abs((xrf - xr) / xrf) * 100
                        #Evaluamos los criterios para las demas iteraciones
                        if fx1 * fxr < 0:
                            x2 = xr
                        elif fx1 * fxr > 0:
                            x1 = xr
                        else:
                            #Si el eror Ea es menor que Es devolemos la raiz al usuario con el mensaje
                            print("A econtrado la raiz es: " + str(xri))
                        producto = fx1 * fxr
                        data.append([it + 1, x11, x22, xr, fx1, fxr, producto, E])
                        xrf = xr
                        it += 1

                        #Imprimimos la tabla
                    print(tabulate(data, headers=["It", "x1", "x2", "xr", "F(x1)", "F(xr)", "F(x1)*F(xr)", "Ea"], tablefmt="github"))

                #Opcion 3 falsa posicion
                elif metodo==3:
                    oncemore = iter([True, False])
                    data = []

                    # Defino la función a trabajar
                    def f(x):
                        y = 2.718281828 ** (-x) - x
                        return (y)

                    # Obteniendo los datos
                    x1 = float(input("\x1b[0;30m"+"¿Cual es el valor de X1?\n"))
                    x2 = float(input("¿Cual es el valor de X2?\n"))
                    if f(x1) * f(x2) <= 0:
                        # inicializo las variables
                        xr = 0
                        i = 0
                        E = 100
                        # mientras sea mayor a tolerancia seguir iterando
                        while (E > tolerancia):
                            i += 1
                            # Guardo en otras variables la funcion evaluada con esos parametros
                            fx1 = f(x1)
                            fx2 = f(x2)
                            fxr = f(xr)
                            # Resguardo mi valor para la siguiente iteración
                            xr_anterior = xr
                            # Calculo la aproximación
                            xr = (x1 - ((fx1 * (x1 - x2)) / (fx1 - fx2)))
                            # Inicializo en 0 para que en la siguiente iteracion me guarde el E en ella misma.
                            E = 0
                            E = (abs((xr - xr_anterior) / xr)) * 100
                            # Imprimo los valores en la tabla creada
                            data.append([i, x1, x2, f(x1), f(x2), xr, f(xr), f(x1) * f(x2), E])
                            if fx1 * fx2 < 0:
                                x2 = xr
                                xr_anterior = x2
                            else:
                                x1 = xr
                                xr_anterior = x1
                        # Genero el encabezado de la tabla,ademas de imprimir los valores obtenidos
                        print(tabulate(data,
                                       headers=["Iteración", "X1", "X2", "f(X1)", "f(X2)", "Xr", "f(Xr)", "f(X1)f(Xr)",
                                                "Ea"], tablefmt="orgtbl"))
                        print("\nEn iteracion :  " + str(i))
                        print("Se obtuvo como resultado de xr=  " + str(xr))
                        print("Con un error de Ea=" + str(E) + "\n")
                    else:
                        print("\x1b[1;31m"+"No existe solucion en dicho intervalo"+"\x1b[0;30m")

                #Opcion 4 punto fijo
                elif metodo==4:
                    x = sp.Symbol('x')
                    oncemore = iter([True, False])
                    data = []

                    # Obtengo función g(x) proporcionado por el usuario
                    gx=input("\x1b[0;30m"+"Por favor ingrese g(x):")
                    print(gx)

                    # Obtengo el punto inicial
                    x0 = float(input("¿Cual es el valor de X0?\n"))

                    # Evaluo en el punto con la g'(x)
                    evaluando = sp.diff(gx).subs(x, x0)
                    print(evaluando)

                    # Compruebo si existe convergencia
                    if (evaluando < 1):  # converge
                        i = 0
                        xr = 0
                        E = 100
                        while E > tolerancia:
                            i += 1
                            # Resguardo mi valor para la siguiente iteración
                            xr_anterior = x0
                            # Calculo la aproximacion
                            xr = sp.sympify(gx).subs(x,x0)
                            # ahora calculamos el error
                            E = 0
                            E = abs((xr - xr_anterior) / xr) * 100
                            # Imprimo los valores en la tabla creada
                            data.append([i, xr_anterior, xr, E])
                            x0 = xr
                        # Genero el encabezado de la tabla,ademas de imprimir los valores obtenidos
                        print(tabulate(data, headers=["Iteración", "X", "g(x)", "Ea"], tablefmt="orgtbl"))
                        print("\nEn iteracion :  " + str(i))
                        print("Se obtuvo como resultado de xr=  " + str(xr))
                        print("Con un error de Ea=" + str(E) + "\n")
                    else:
                        print("\x1b[1;31m"+"No posee convergencia en el punto proporcionado"+"\x1b[0;30m")

                #Opcion 5 Newton raphson
                elif metodo==5:
                    cifras = -1
                    ea = 1000
                    Xn = 0

                    # se declara a "x" como simbolo en las funciones que ingrese el usuario
                    x = sp.Symbol('x')
                    # se le pide al usuario que ingrese la funcion
                    fx = f
                    # se calcula la primer derivada
                    dfx = sp.diff(fx)
                    # se muestra la derivada de la funcion
                    print("\x1b[0;30m","f'(x)= ", dfx)
                    # el metodo de newton exige un valor incial, aca se pide este valor incial
                    Xn = float(input("digite el valor inicial "))
                    # i=1, esto es quivalente a iteracion
                    i = 1
                    # en este metodo while se lleva acabo el proceso para calcular la raiz
                    while (ea > tolerancia):
                        print("iteracion ", i)
                        print("Xn, ", Xn)
                        # se calcula la evaluacion de Xn en la funcion fx
                        fXn = sp.sympify(fx).subs(x, Xn)
                        print("fXn ", fXn)
                        # se calcula ñla evaluacion de Xn en la derivada de la funcion
                        dfXn = sp.sympify(dfx).subs(x, Xn)
                        print("f'(Xn)= ", dfXn)
                        # ecuacion para obtener la aproximacion de la raiz a traves del metodo de newton
                        aprox = Xn - ((fXn) / (dfXn))
                        print("Xn+1 ", aprox)
                        # calculamos el error
                        ea = abs(((aprox - Xn) / aprox) * 100)
                        print("ea= ", ea)
                        # ahora Xn=aprox
                        Xn = aprox
                        # incrementamos el valor de i
                        i = i + 1

                #Opcion 6 Secante
                elif metodo==6:
                    # Error
                    def errorAbs(va, vp):
                        return abs((va - vp) / va) * 100

                    def secante_tabla(fx, xa, xb):
                        tabla = []
                        while True:
                            fa = fx(xa)
                            fb = fx(xb)
                            xc = xa - fa * (xb - xa) / (fb - fa)
                            errorAb = errorAbs(xc, xb)
                            tabla.append([xa, xb, fa, fb, xc, errorAb])
                            xa = xb
                            xb = xc
                            if errorAb <= error:
                                break

                        tabla = np.array(tabla)
                        return (tabla)

                    # INGRESO
                    def fx(x):
                        return sin(x/2)-5*exp(-x)

                    xa = int(input("\x1b[0;30m"+"Ingrese el primer valor "))
                    xb = int(input("Ingrese el segundo valor "))
                    cifras = 3
                    error = 0.5 * (10 ** (2 - cifras))  # en porcentaje
                    if fx(xa) * fx(xb) < 0:
                        print("Converge")
                    else:
                        print("\x1b[1;31m"+"No converge"+"\x1b[0;30m")
                        exit()

                    # PROCEDIMIENTO
                    tabla = secante_tabla(fx, xa, xb)
                    n = len(tabla)

                    # SALIDA
                    print(tabulate(tabla, headers=['Xn-1', 'Xn', "f(Xn-1)", "f(Xn)",
                                                   "Xn+1", "|Ea|%"], tablefmt="pretty"))
                    print('raiz en: ', tabla[n - 1, 4])
                    print("Con error de: ", tabla[n - 1, 5])

                #Opcion 7 Müller
                elif metodo==7:
                    # Funcion del Ejercicio
                    def f(x, funcion):
                        return eval(funcion.replace("x", str(x)))

                    # Recibe tres valores iniciales y la cadena de la funcion
                    def muller(x0, x1, x2, Es, funcion):
                        """
                        Parametros:
                         x0 -- primer valor inicial
                         x1 -- Segundo valor
                         x2 -- tercer valor
                         Es -- error especifico
                         funcion -- la cadena de la funcion
                        """
                        Ea = 100
                        data = []
                        while Ea > Es:
                            h0 = x1 - x0
                            h1 = x2 - x1
                            delta0 = (f(x1, funcion) - f(x0, funcion)) / h0
                            delta1 = (f(x2, funcion) - f(x1, funcion)) / h1
                            a = (delta1 - delta0) / (h1 + h0)
                            b = a * h1 + delta1
                            c = f(x2, funcion)
                            if b > 0:
                                if (b * b - 4 * a * c) > 0:
                                    xr = x2 + (-2 * c) / (b + sqrt(b * b - 4 * a * c))
                                else:
                                    xr = x2 + (-2 * c) / (complex(b, sqrt(b * b - 4 * a * c)))
                            else:
                                if (b * b - 4 * a * c) > 0:
                                    xr = x2 + (-2 * c) / (b - sqrt(b * b - 4 * a * c))
                                else:
                                    xr = x2 + (-2 * c) / (complex(b, -sqrt(b * b - 4 * a * c)))
                            Ea = abs((xr - x2) / xr) * 100
                            data.append([x0, x1, x2, h0, h1, delta0, delta1, a, b, c, xr, Ea])
                            x0 = x1
                            x1 = x2
                            x2 = xr
                        return data

                    funcion = "2*(x**4)+(x**3)-8*(x**2)-x+6"
                    # funcion = "6*(x**3)+7*(x**2)-9*x+2"
                    x0 = 0
                    x1 = 0.5
                    x2 = 0.7
                    # cifras = int(input("Cuantas cifras significativas desea?\n"))
                    cifras = 3
                    Es = 0.5 * (10 ** (2 - cifras))  # en porcentaje

                    data = muller(x0, x1, x2, Es, funcion)
                    print("\x1b[0;30m",end="")
                    print(
                        f"La raíz es: {data[-1][-2]}, \nCon un error de {data[-1][-1]}")
                    print(tabulate(data, headers=["X0", "X1", "X2", "h0", "h1", "&0", "&1", "a", "b", "c", "X3", "Ea"],
                                   tablefmt="pretty"))

                    print("Para que se mire toda la tabla en orden, es necesario hacer más pequeña la letra de la consola, esto es debido al gran número de variables")

                metodo = int(input("\x1b[3;36m" +"Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n" "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Müller\nOtro numero para salir\n" + "\x1b[1;36m"))

        #Si la funcion no es exponencial devolvemos al usuario el mensaje
        else:
            print("\x1b[1;31m"+"Debe ingresar una funcion exponencial"+"\x1b[3;36m")
