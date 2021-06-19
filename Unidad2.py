#Importamos las librerias necesarias
import numpy as np
from math import *
from numpy import sign
from tabulate import tabulate
from matplotlib import pyplot as plt

#Creamos la clase U2
class Un2:
    #Definimos la funcion U2 que recibe el argumento tolerancia
    def U2(tolerancia):
        #Solicitamos al usuario que ingresa la funcion exponencial
        fx = input("\x1b[1;33m"+"Introduce la funcion exponencial en terminos de x "+"\x1b[1;36m")
        #Validamos que en realidad se trate de una funcion exponencial
        if "**x" in fx or "exp(" in fx or "**-x" in fx:
            #Desplegamos un menu para que el usuario elija el metodo a utilizar
            metodo = int(input("\x1b[3;36m"+
                "Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n"
                "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Bairstow\n9.Müller\nOtro numero para salir\n"+"\x1b[0;30m"))

            while metodo > 0 and metodo < 10:

                #Si la opcion es 1 Grafico
                if metodo == 1:
                    #Definimos el rango de datos a evaluar la funcion
                    x = np.linspace(-3, 3)
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


                # Si la opcion es 2 Biseccion
                elif metodo == 2:
                    # Biseccion
                    #Solicitamos el primer valor
                    x = float(input("Ingrese el valor para x1 "))
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
                        print("Ingrese un intervalo valido")

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
                    print(tabulate(data, headers=["It", "x1", "x2", "xr", "F(x1)", "F(xr)", "F(x1)*F(xr)", "Ea"],
                                   tablefmt="github"))


                # Si la opcion es 6 Secante
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

                    xa = int(input("Ingrese el primer valor "))
                    xb = int(input("Ingrese el segundo valor "))
                    cifras = 3
                    error = 0.5 * (10 ** (2 - cifras))  # en porcentaje
                    if fx(xa) * fx(xb) < 0:
                        print("Converge")
                    else:
                        print("No converge")
                        exit()

                    # PROCEDIMIENTO
                    tabla = secante_tabla(fx, xa, xb)
                    n = len(tabla)

                    # SALIDA
                    print(tabulate(tabla, headers=['Xn-1', 'Xn', "f(Xn-1)", "f(Xn)",
                                                   "Xn+1", "|Ea|%"], tablefmt="pretty"))
                    print('raiz en: ', tabla[n - 1, 4])
                    print("Con error de: ", tabla[n - 1, 5])

                elif metodo==9:
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
                    print(
                        f"La raíz es: {data[-1][-2]}, \nCon un error de {data[-1][-1]}")
                    print(tabulate(data, headers=["X0", "X1", "X2", "h0", "h1", "&0", "&1", "a", "b", "c", "X3", "Ea"],
                                   tablefmt="pretty"))

                    print("Para que se mire toda la tabla en orden, es necesario hacer más pequeña la letra de la consola, esto es debido al gran número de variables")

                metodo = int(input("\x1b[3;36m"+"Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n"
                    "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Bairstow\n9.Müller\nOtro numero para salir "+"\x1b[0;30m"))

        #Si la funcion no es exponencial devolvemos al usuario el mensaje
        else:
            print("Debe ingresar una funcion exponencial")