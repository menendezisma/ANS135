import numpy as np
from tabulate import tabulate
from sympy import *

#Creamos la clase Un5
class Un5:
    #Definimos la funcion principal U5
    def U5(self=None):
        opc = int(input("\x1b[3;35m"+"Ingrese el numero de la opcion deseada\n1.Metodo de Euler\n2.Metodo de Taylor\n3.Metodo de Runge Kutta\n4.Metodo multipaso\nOtro numero para salir\n"))

        while opc > 0 and opc < 5:
            if opc==1:
                euler=int(input("\x1b[1;33m"+"1.Euler hacia adelante\n2.Euler hacia atras\n3.Euler centrado\n4.Euler modificado\nOtro numero para salir "+"\x1b[1;30m"))
                while euler > 0 and euler < 5:
                    if euler==1:
                        # Metodo Euler hacia adelante
                        #Declarammos nuestras variables
                        x, y = symbols("x y")
                        #Creamos un try/except para controlar cualquier error
                        try:
                            #SOlicitamos al usuario que ingrese la funcion
                            fn = eval(input("\x1b[1;30m" + "Ingrese la funcion f(x,y): "+"\x1b[0;30m" ))
                            # Mostramos la funcion al usuario para que el verifique si es correcta
                            print(fn)
                            # Solicitamos los valores iniciales para x e y
                            x0 = float(input("Ingrese el valor incial de x0: "))
                            y0 = float(input("Ingrese el valor incial de y0: "))

                            # Creamos un bucle para pedir le al usuario el valor de h y que sea valido
                            while True:
                                # Solicitamos que ingrese el tamaño del paso
                                h = float(input("Ingrese el tamaño de paso h: "))
                                # Verificamos que h no sea 0 ni negativo
                                if h <= 0:
                                    # De no ser correcto el valor le mandamos un mensaje al usuario
                                    print("El tamaño de paso no puede cer cero o negativo")
                                else:
                                    # Si el valor es correcto cerramos el bucle y cntinuamos con el codigo
                                    break
                            # Solicitamos al usuario que ingrese el valor de y a calcular
                            xn = float(input("Ingrese el valor a calcular y(xn): "))
                            # Calculamos las iteraciones a dar
                            itc = round(((xn - x0) / h))
                            # Indicamos al usuario que imprimiremos los valores
                            print("--------- Tabla de valores ---------")
                            # Creamos un bucle para ir calculando los valores
                            for i in range(1, itc + 1):
                                # Evaluamos la funcion en los puntos iniciales
                                f = fn.subs([(x, x0), (y, y0)])
                                # Calculamos el valor de la aprocimacion
                                yn = y0 + h * f
                                # Aumentamos el valor de x
                                x0 = round(x0 + h, 5)
                                y0 = yn
                                # Vamos imprimiendo los valores
                                print("\x1b[1;35m" + 'y(', x0, ')=', yn)
                            # Cuando finalizamos indicamos al usuario cual es la respuesta
                            print("\nValor aproximado: ", yn)
                            
                        except:
                            #De haber un error le avisamos al usuario
                            print("\x1b[1;31m" + "La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion " + "\x1b[1;35m")

                    elif euler==2:
                        # Metodo Euler hacia atras
                        #Declaramos nuestras variables
                        x, y = symbols("x y")
                        #creamsos un try/except para manejar los errores que puedan surjir
                        try:
                            #Solicitamos al usuario que ingrese la funcion
                            fn = eval(input("\x1b[1;30m" + "Ingrese la funcion f(x,y): "+"\x1b[0;30m" ))
                            # imprimimos para que el usuario vea si es correcta
                            print(fn)
                            # solicitamos los valores iniciales de x e y
                            x0 = float(input("Ingrese el valor incial de x0: "))
                            y0 = float(input("Ingrese el valor incial de y0: "))
                            # Creamos un bucle para pedir le al usuario el valor de h y que sea valido
                            while True:
                                # Pedimos el valor de h
                                h = float(input("Ingrese el tamaño de paso h: "))
                                # Evaluamos si el valor es correcto
                                if h <= 0:
                                    # De no serlo le mandamos un mensaje al usuario
                                    print("El tamaño de paso no puede cer cero o negativo")
                                else:
                                    # Si es correcto cerramos el bucle y continuamos con el desarrollo
                                    break
                            # Solicitamos el valor a calcular en la funcion
                            xn = float(input("Ingrese el valor a calcular y(xn): "))
                            # calculamos la cantidad de iteraciones a dar
                            itc = round(((xn - x0) / h))
                            # Indicamos al usuario que imprimiremos los valores
                            print("--------- Tabla de valores ---------")
                            # creamos un bucle para ir calculando los valores
                            for i in range(1, itc + 1):
                                # Evaluamos los valores iniciales
                                f1 = fn.subs([(x, x0), (y, y0)])
                                # Creamos la variable U para calcular el valor de Yi*
                                u = y0 + h * f1
                                # Evaluamos X0+h y u en la funcion para encontrar Yi
                                f2 = fn.subs([(x, x0 + h), (y, u)])
                                yn = y0 + h * f2
                                # Calculamos el valor de la aprocimacion
                                x0 = round(x0 + h, 5)
                                y0 = yn
                                # Imprimimos todos los valores al usuario
                                print("\x1b[1;35m" + 'y(', x0, ')=', yn)
                            # Cuando finalizamos indicamos al usuario cual es la respuesta
                            print("\x1b[1;34m" + "\nValor aproximado: ", yn, "\x1b[3;35m")
                                
                        except:
                            # De haber un error le avisamos al usuario
                            print(
                                "\x1b[1;31m" + "La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion " + "\x1b[1;35m")

                    elif euler==3:
                        #Metodo de Euler centrado
                        x, y = symbols('x y')
                        # Le solicito la funcion al usuario
                        fn = eval(input("\x1b[1;30m" + "Ingrese la funcion f(x,y): "+"\x1b[0;30m" ))
                        oncemore = iter([True, False])
                        data = []

                        def funcion(x0, y0):
                            ec = sympify(fn).subs([(x, x0), (y, y0)])
                            return (ec)

                        # Pedimos los datos iniciales
                        x0 = float(input("Ingrese el valor incial de x0: "))
                        y0 = float(input("Ingrese el valor incial de y0: "))

                        # mientras prueba es 1 significa que el valor de n es no valido.
                        prueba = 1
                        while (prueba == 1):
                            n = int(input("Ingrese el numero de espacios\nn= "))
                            # validamos el valor de n para las partes iguales
                            if n >= 0:
                                # Obtenemos el valor aproximar de la función
                                x1 = float(input("Ingrese el valor aproximar: "))
                                # calculamos el valor de h que representa el espaciado
                                h = abs((x0 - x1) / n)
                                # generamos las iteraciones hasta que llegue a n+1 iteraciones
                                for i in range(n + 1):
                                    # Capturo los datos en tabla en cada iteración
                                    data.append([i, x0, y0])
                                    # para xi sumamos en cada iteracion h al valor que pasara hacer inicial
                                    xi = x0 + h
                                    # Evaluo los valores iniciales y creamos Yi
                                    yi = y0 + h * funcion(x0, y0)
                                    # hacemos cambio de variable para la siguiente iteración
                                    x0 = xi
                                    y0 = yi
                                # Genero el encabezado de la tabla,ademas de imprimir los valores obtenidos
                                print(tabulate(data, headers=["n", "X(n)", "Y(n)"], tablefmt="orgtbl"))
                                prueba = 0
                            else:
                                prueba = 1

                    elif euler==4:
                        # Metodo Euler mejorado
                        #Creamos nuestras variables
                        x, y = symbols("x y")
                        #Hacemos uso de un try/except para manejar posibles errores
                        try:
                            #Solicitamos al usuario que ingrese la funcion
                            fn = eval(input("\x1b[1;30m" + "Ingrese la funcion f(x,y): "+"\x1b[0;30m" ))
                            # Se la mostramos al usuario para que verifique si es correcta
                            print(fn)
                            # Solcitamos los valores iniciales de x e y
                            x0 = float(input("Ingrese el valor incial de x0: "))
                            y0 = float(input("Ingrese el valor incial de y0: "))
                            # Creamos un bucle para pedir le al usuario el valor de h y que sea valido
                            while True:
                                # Pedimos que ingrese el valor de h
                                h = float(input("Ingrese el tamaño de paso h: "))
                                # verificamos que el valor sea correcto
                                if h <= 0:
                                    # De no serlo devolvemos el siguiente mensaje
                                    print("El tamaño de paso no puede cer cero o negativo")
                                else:
                                    # si el valor es correcto cerramos el bucle y seguimos con el desarrollo
                                    break
                            # Solicitamos que ingrese el valor a calcular en la funcion
                            xn = float(input("Ingrese el valor a calcular y(xn): "))
                            # calculamos la cantidad de iteraciones
                            itc = round(((xn - x0) / h))
                            # Indicamos que vamos a imprimir los valores
                            print("--------- Tabla de valores ---------")
                            # creamos un ciclo for para calcular los valores
                            for i in range(1, itc + 1):
                                # Evaluamos los valores iniciales de x e y
                                f1 = fn.subs([(x, x0), (y, y0)])
                                # utilizamos la variable u para calcular yi*
                                u = y0 + h * f1
                                # Evaluamos los valores de x0+h y u en la funcion para encontrar yi
                                f2 = fn.subs([(x, x0 + h), (y, u)])
                                # Calculamos el valor de la aprocimacion
                                yn = y0 + h * ((f1 + f2) / 2)
                                # calculamos el valor redondeaddo de x para la siguiente iteracion
                                x0 = round(x0 + h, 5)
                                y0 = yn
                                # Imprimimos todos los valores al usuario
                                print("\x1b[1;35m" + 'y(', x0, ')=', yn)
                            # Cuando finalizamos indicamos al usuario cual es la respuesta
                            print("\nValor aproximado: ", yn)

                        except:
                            # De haber un error le avisamos al usuario
                            print("\x1b[1;31m" + "La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion " + "\x1b[1;31m")

                        else:
                            break
                    euler=int(input("\x1b[1;33m"+"1.Euler hacia adelante\n2.Euler hacia atras\n3.Euler centrado\n4.Euler modificado\nOtro numero para salir "+"\x1b[1;30m"))
                break
            elif opc==2:
                def edo_taylor3t(d1y, d2y, x0, y0, h, muestras):
                    tamano = muestras + 1
                    estimado = np.zeros(shape=(tamano, 4), dtype=float)
                    # incluye el punto [x0,y0]
                    estimado[0] = [x0, y0, 0, 0]
                    x = x0
                    y = y0
                    for i in range(1, tamano, 1):
                        estimado[i - 1, 2:] = [d1y(x, y), d2y(x, y)]
                        y = y + h * d1y(x, y) + ((h ** 2) / 2) * d2y(x, y)
                        x = x + h
                        estimado[i, 0:2] = [x, y]
                    return (estimado)

                # y'-y-x+(x**2)-1 =0, y(0)=1

                # INGRESO.
                # d1y = y', d2y = y''
                d1y = lambda x, y: y - x ** 2 + x + 1
                d2y = lambda x, y: y - x ** 2 - x + 2
                x0 = 0
                y0 = 1
                h = 0.1
                muestras = 5

                # PROCEDIMIENTO
                puntos = edo_taylor3t(d1y, d2y, x0, y0, h, muestras)
                xi = puntos[:, 0]
                yi = puntos[:, 1]
                # print(xi,yi)
                print(tabulate(puntos, headers=["xi", "yi", "d1yi", "d2yi"], tablefmt="pretty"))

                # ERROR vs solución conocida
                y_sol = lambda x: ((np.e) ** x) + x + x ** 2

                yi_psol = y_sol(xi)
                errores = yi_psol - yi
                errormax = np.max(np.abs(errores))

                # SALIDA
                print('Error relativo máximo estimado: ', errormax)
                print('entre puntos: ')
                print(errores)

                # GRAFICA [a,b+2*h]
                a = x0
                b = h * muestras + 2 * h
                muestreo = 10 * muestras + 2
                xis = np.linspace(a, b, muestreo)
                yis = y_sol(xis)

                # Gráfica
                import matplotlib.pyplot as plt
                plt.plot(xis, yis, label='y conocida')
                plt.plot(xi[0], yi[0], 'o', color='r', label='[x0,y0]')
                plt.plot(xi[1:], yi[1:], 'o', color='g', label='y estimada')
                plt.title('EDO: Solución con Taylor 3 términos')
                plt.xlabel('x')
                plt.ylabel('y')
                plt.legend()
                plt.grid()
                plt.show()
                break

            elif opc==3:
                #Metodo de Runge Kutta para orden 4
                #Definimos nuestras variables
                x,y=symbols("x y")
                #Mediante un try/except tratamos cualquier error
                try:
                    #Solicitamos al usuario que ingrese la funcion
                    fn = eval(input("\x1b[1;30m"+"Ingrese la funcion f(x,y): " + "\x1b[0;30m"))
                    # Mostramos para verificar que es correcta
                    print(fn)
                    # Solicitamos los valores iniciales de x e y
                    x0 = float(input("Ingrese el valor incial de x0: "))
                    y0 = float(input("Ingrese el valor incial de y0: "))
                    # creamos un ciclo while para que el usuario ingrese el valor de h
                    while True:
                        # Solicitamos el valor de h
                        h = float(input("Ingrese el tamaño de paso h: "))
                        # Verificamos que el valor sea correcto
                        if h <= 0:
                            # si el valor no es correcto devolvemos el siguiente mensaje
                            print("El tamaño de paso no puede cer cero o negativo")
                        else:
                            # de lo contrario cerramos nuestro ciclo y seguimos con los calculos
                            break
                    # Pedimos el valor a calcular
                    xn = float(input("Ingrese el valor a calcular y(xn): "))
                    # calculamos el numero de iteraciones
                    itc = round(((xn - x0) / h))
                    # Indicamos al usuario que imprimiremos lo valores
                    print("--------- Tabla de valores ---------")
                    # Creamos un bucle for para calcular los valores
                    for i in range(1, itc + 1):
                        # Calculamos los valores de ki
                        k1 = fn.subs([(x, x0), (y, y0)])
                        k2 = fn.subs([(x, x0 + h / 2), (y, y0 + (h / 2) * k1)])
                        k3 = fn.subs([(x, x0 + h / 2), (y, y0 + (h / 2) * k2)])
                        k4 = fn.subs([(x, x0 + h), (y, y0 + h * k3)])
                        # Despues de haber calculado los valores de ki calculamos el valor de la aproximacion
                        yn = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                        # calculamos el valor de x para las demas iteraciones
                        x0 = round(x0 + h, 5)
                        y0 = yn
                        # Imprimimos todos los valores al usuario
                        print("\x1b[1;35m" + 'y(', x0, ')=', yn)
                    # Cuando finalizamos indicamos al usuario cual es la respuesta
                    print("\nValor aproximado: ", yn)
                    break

                except:
                    # De haber un error le avisamos al usuario
                    print("\x1b[1;31m"+"La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion "+"\x1b[1;31m")
                break
            elif opc==4:
                # Multipaso Adam Bashfort y Moulton
                # Metodo Predictor orden 4-corrector de orden 3
                # Definimos nuestras variables
                x, y = symbols("x y")
                # Mediante un try/except tratamos cualquier error
                try:
                    # Solicitamos al usuario que ingrese la funcion
                    #print("\x1b[1;30m", end="")
                    fn = eval(input("\x1b[1;30m"+"Ingrese la funcion f(x,y): " + "\x1b[0;30m"))
                    # Mostramos para verificar que es correcta
                    print(fn)
                    # Solicitamos los valores iniciales de x e y
                    x0 = float(input("Ingrese el valor incial de x0: "))
                    xi = x0
                    y0 = float(input("Ingrese el valor incial de y0: "))
                    yi = y0
                    # creamos un ciclo while para que el usuario ingrese el valor de h
                    while True:
                        # Solicitamos el valor de h
                        h = float(input("Ingrese el tamaño de paso h: "))
                        # Verificamos que el valor sea correcto
                        if h <= 0:
                            # si el valor no es correcto devolvemos el siguiente mensaje
                            print("El tamaño de paso no puede cer cero o negativo")
                        else:
                            # de lo contrario cerramos nuestro ciclo y seguimos con los calculos
                            break
                    # Pedimos el valor a calcular
                    xn = float(input("Ingrese el valor a calcular y(xn): "))
                    # calculamos el numero de iteraciones
                    itc = round(((xn - x0) / h))
                    # Creamos un bucle for para calcular los valores
                    for i in range(1, itc + 1):
                        # Calculamos los valores de ki
                        k1 = fn.subs([(x, x0), (y, y0)])
                        k2 = fn.subs([(x, x0 + h / 2), (y, y0 + (h / 2) * k1)])
                        k3 = fn.subs([(x, x0 + h / 2), (y, y0 + (h / 2) * k2)])
                        k4 = fn.subs([(x, x0 + h), (y, y0 + h * k3)])
                        # Despues de haber calculado los valores de ki calculamos el valor de la aproximacion
                        yn = y0 + h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
                        if i == 1:
                            y1 = yn
                        elif i == 2:
                            y2 = yn
                        elif i == 3:
                            y3 = yn
                        # calculamos el valor de x para las demas iteraciones
                        x0 = round(x0 + h, 5)
                        y0 = yn
                    # Una ves calculado los valores de Runge kutta evaluamos la funcion en estos valores
                    fx0y0 = fn.subs([(x, xi), (y, yi)])
                    fx1y1 = fn.subs([(x, xi + h), (y, y1)])
                    fx2y2 = fn.subs([(x, xi + 2 * h), (y, y2)])
                    fx3y3 = fn.subs([(x, xi + 3 * h), (y, y3)])
                    # Una ves teniendo todos los datos procedemos a calcular el Predictor
                    u4 = y3 + (h / 24) * ((55 * fx3y3) - (59 * fx2y2) + (37 * fx1y1) - (9 * fx0y0))

                    y4 = fn.subs([(x, xn), (y, u4)])

                    # Por ultimo aplicamos la correccion de Adams-Moulton 3 pasos
                    Ry4 = y3 + (h / 24) * ((9 * y4) + (19 * fx3y3) - (5 * fx2y2) + fx1y1)
                    # Devolvemos la respuesta al usuario
                    print("\x1b[1;34m" + "\nLa respuesta a traves del metodo de multipasos es: ", Ry4)
                    print("\x1b[3;35m")

                except:
                    # De haber un error le avisamos al usuario
                    print(
                        "\x1b[1;31m" + "La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion " + "\x1b[1;31m")
            else:
                break
            opc = int(input("\x1b[3;35m" + "Ingrese el numero de la opcion deseada\n1.Metodo de Euler\n2.Metodo de Taylor\n3.Metodo de Runge Kutta\n4.Metodo multipaso\nOtro numero para salir\n"))