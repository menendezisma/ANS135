import time
import sympy as sym
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
import os

#Creamos la clase Un3
class Un3:
    #Definimos la funcion U3
    def U3(self):
        #Desplegamos un menu
        metodo = int(input("\x1b[3;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
            "\n3.Diferencias Divididas\n4.pol de Hermite\nOtro numero para salir "+"\x1b[0;30m"))

        while metodo > 0 and metodo < 5:
            #Opcion 1 Interpolacion de Lagrange
            if metodo == 1:
                opc=int(input("Ingrese la opcion deseada\n1.Ingresar datos\n2.Ingresar funcion "))
                while opc > 0 and opc < 3:
                    if opc==1:
                        # Definimos nuestras variables
                        x = sym.Symbol('x')
                        #Creamos las listas vacias a utilizar
                        data = []
                        xi = []
                        fi = []
                        #Definimos las demas variables a utilizar
                        y = 0
                        num = 1
                        denom = 1
                        pol = 0
                        #Pedimos al usuario que ingrese los datos
                        n = int(input("Ingrese la cantidad de datos a ingresar "))
                        #creamos un bucle para ir pidiento los datos
                        for i in range(n):
                            #solicitamos al usuario que ingrese el primer dato
                            datoXi = float(input("Ingrese el dato x{}: ".format(i)))
                            #Guardamos nuestros datos en la lista correspondiente
                            xi.append(datoXi)
                            # solicitamos al usuario que ingrese el segundo dato
                            datoFi = float(input("Ingrese el dato y{}: ".format(i)))
                            fi.append(datoFi)
                            # Guardamos nuestros datos en la lista correspondiente
                            data.append([datoXi, datoFi])
                        os.system("cls")
                        print(tabulate(data, headers=["x", "y"], tablefmt="pretty"))

                        #Empezamos a calcular
                        for y in range(0, n, 1):
                            num = 1
                            denom = 1
                            for j in range(0, n, 1):
                                if y != j:
                                    num *= (x - xi[j])
                                    denom = denom * (xi[y] - xi[j])
                                term = (num / denom) * fi[y]
                            pol+= + term
                        polSimp = sym.expand(pol)
                        funcion = " ", polSimp
                        print("pol: \n", pol)
                        print("\npol Simple: \n", polSimp)

                        break
                    elif opc==2:
                        break
                    else:
                        break

            # Opcion 2 pol de newton
            elif metodo == 2:
                opc = int(input("Ingrese la opcion deseada\n1.Ingresar datos\n2.Ingresar funcion "))
                while opc > 0 and opc < 3:
                    #Opcion 1- Ingresa datos
                    if opc == 1:
                        #Definimos las variables
                        x = sym.Symbol('x')
                        #Declaramos las listas a utilizar
                        data = []
                        xi = []
                        fi = []
                        bn = []
                        pol = 0

                        #Solicitamos la cantidad de datos
                        nDatos = int(input("ingrese la cantidad de datos "))
                        #Implementamos un bucle para pedir los datos
                        for i in range(nDatos):
                            #Solicitamos el primer dato
                            datoXi = float(input("Ingrese el dato numero x{}: ".format(i)))
                            #Lo almacenamos en la lista correspondiente
                            xi.append(datoXi)
                            # Solicitamos el segundo dato
                            datoFi = float(input("Ingrese el dato numero y{}: ".format(i)))
                            # Lo almacenamos en la lista correspondiente
                            fi.append(datoFi)
                            #Pasamos los datos a la lista para luego mostrarlo
                            data.append([i, datoXi, datoFi])
                        #Despues de haber calculado los valores imprimos la tabla en pantalla
                        print(tabulate(data, headers=["iteracion", "x", "y"], tablefmt="pretty"))

                        # Tabla de Diferencias Divididas Avanzadas
                        n = len(xi)
                        #Creamos nuestra tabla de diferencias divididas inicialmente vacia
                        dfinita = np.zeros(shape=(n, n), dtype=float)
                        data = np.concatenate((data, dfinita), axis=1)
                        #Calculamos la tabla
                        [n, m] = np.shape(data)
                        diag = n - 1
                        j = 3
                        titulo = ["iteracion", "x", "y"]
                        while (j < m):
                            # cada fila de columna
                            i = 0
                            # paso = j-2 # inicia en 1
                            while (i < diag):
                                denom = (xi[i + (j - 2)] - xi[i])
                                num = data[i + 1, j - 1] - data[i, j - 1]
                                data[i, j] = num / denom
                                i = i + 1
                            diag = diag - 1
                            j = j + 1
                        #Una ves tenemos la tabla de diferencias divididas pasamos a calcular el pol
                        dDividida = data[0, 3:]
                        n = len(dfinita)

                        # expresión del pol con Sympy
                        x = sym.Symbol('x')
                        pol = fi[0]
                        for j in range(1, n, 1):
                            factor = dDividida[j - 1]
                            term = 1
                            for k in range(0, j, 1):
                                term = term * (x - xi[k])
                            pol = pol + term * factor

                        # simplifica multiplicando entre (x-xi)
                        polSimp = pol.expand()

                        # pol para evaluacion numérica
                        px = sym.lambdify(x, polSimp)

                        # Puntos para la gráfica
                        muestras = 101
                        a = np.min(xi)
                        b = np.max(xi)
                        pxi = np.linspace(a, b, muestras)
                        pfi = px(pxi)

                        # SALIDA
                        print('pol: ')
                        print(pol)
                        print('pol simplificado: ')
                        print(polSimp)

                    # Opcion 2- Ingresa Funcion
                    elif opc==2:
                        #Declaro la variable a utilizar
                        x = sym.Symbol('x')
                        #Creo las listas necesarias para almacenar los datos
                        data = []
                        xi = []
                        fi = []
                        y = 0
                        numerador = 1
                        denominador = 1
                        polinomio = 0

                        #Solicitamos al ususario que ingrese la funcion
                        funcion = input("Ingrese la funcion en terminos de x\nf(x): ")
                        lista = funcion.split()
                        for i in lista:
                            # Solicitando datos al usuario para la funcion
                            print("\n Ingrese el valor del intervalo a evaluar ")
                            x0 = float(input("Ingrese el valor x0:  \t"))
                            x1 = float(input("Ingrese el valor x1:  \t"))

                            # Creando la tabla de datos
                            xm = (x0 + x1) / 2
                            nDatos = int(input("Ingrese la cantidad de datos "))
                            for i in range(nDatos):
                                if i % 2 == 0:
                                    xm = (x0 + xm) / 2
                                    datoFi = sym.sympify(funcion).subs(x,xm)
                                    xi.append(xm)
                                    fi.append(datoFi)
                                    data.append([xm, datoFi])
                                else:
                                    xm = (x1 + xm) / 2
                                    datoFi = sym.sympify(funcion).subs(x,xm)
                                    xi.append(xm)
                                    fi.append(datoFi)
                                    data.append([xm, datoFi])
                            data.sort()
                            print(tabulate(data, headers=["x", "y"], tablefmt="pretty"))
                            # procedimiento del polinomio de newton
                            x = sym.Symbol('x')

                            # Tabla de Diferencias Divididas Avanzadas
                            n = len(xi)
                            # diferencias divididas vacia
                            dfinita = np.zeros(shape=(n, n), dtype=float)
                            data = np.concatenate((data, dfinita), axis=1)
                            # Calcula tabla, inicia en columna 3
                            [n, m] = np.shape(data)
                            diagonal = n - 1
                            j = 3
                            titulo = ["iteracion", "x", "y"]
                            while (j < m):
                                # cada fila de columna
                                i = 0
                                # paso = j-2 # inicia en 1
                                while (i < diagonal):
                                    denominador = (xi[i + (j - 2)] - xi[i])
                                    numerador = data[i + 1, j - 1] - data[i, j - 1]
                                    data[i, j] = numerador / denominador
                                    i = i + 1
                                    diagonal = diagonal - 1
                                    j = j + 1
                            # POLINOMIO con diferencias Divididas
                            # caso: puntos equidistantes en eje x
                            dDividida = data[0, 3:]
                            n = len(dfinita)

                            # expresión del polinomio con Sympy
                            x = sym.Symbol('x')
                            polinomio = fi[0]
                            for j in range(1, n, 1):
                                factor = dDividida[j - 1]
                                termino = 1
                                for k in range(0, j, 1):
                                    termino = termino * (x - xi[k])
                                polinomio = polinomio + termino * factor

                            # simplifica multiplicando entre (x-xi)
                            polisimple = polinomio.expand()

                            # polinomio para evaluacion numérica
                            px = sym.lambdify(x, polisimple)

                            # Puntos para la gráfica
                            muestras = 101
                            a = np.min(xi)
                            b = np.max(xi)
                            pxi = np.linspace(a, b, muestras)
                            pfi = px(pxi)

                            # SALIDA
                            print('polinomio: ')
                            print(polinomio)
                            print('polinomio simplificado: ')
                            print(polisimple)

                            opcion = input("****  ¿Desea evaluar algun punto en X?\n1. Si \n2. No")
                            if opcion == 1:
                                x = float(input("Ingrese el valor de x \t"))
                                px = eval(str(polisimple))
                                print("valor evaluado es: ", px)
                            if opcion == 2:
                                print("Fin del programa")
                    else:
                        break

            # Opcion 3 Diferencias divididas
            elif metodo == 3:
                # pol interpolación
                # Diferencias Divididas de Newton
                # INGRESO , Datos de prueba
                xi = np.array([5, 6, 7, 8, 9, 10])
                fi = np.array([3, 7, 6, 5, -2, 1])

                # PROCEDIMIENTO
                # Tabla de Diferencias Divididas Avanzadas
                titulo = ['i   ', 'xi  ', 'fi  ']
                n = len(xi)
                ki = np.arange(0, n, 1)
                tabla = np.concatenate(([ki], [xi], [fi]), axis=0)
                tabla = np.transpose(tabla)

                # diferencias divididas vacia
                dfinita = np.zeros(shape=(n, n), dtype=float)
                tabla = np.concatenate((tabla, dfinita), axis=1)

                # Calcula tabla, inicia en columna 3
                [n, m] = np.shape(tabla)
                diag = n - 1
                j = 3
                while (j < m):
                    # Añade título para cada columna
                    titulo.append('f[' + str(j - 2) + ']')

                    # cada fila de columna
                    i = 0
                    paso = j - 2  # inicia en 1
                    while (i < diag):
                        denom = (xi[i + paso] - xi[i])
                        num = tabla[i + 1, j - 1] - tabla[i, j - 1]
                        tabla[i, j] = num / denom
                        i = i + 1
                    diag = diag - 1
                    j = j + 1

                # pol con diferencias Divididas
                # caso: puntos equidistantes en eje x
                dDividida = tabla[0, 3:]
                n = len(dfinita)

                # expresión del pol con Sympy
                x = sym.Symbol('x')
                pol = fi[0]
                for j in range(1, n, 1):
                    factor = dDividida[j - 1]
                    term = 1
                    for k in range(0, j, 1):
                        term = term * (x - xi[k])
                    pol = pol + term * factor

                # simplifica multiplicando entre (x-xi)
                polSimp = pol.expand()

                # pol para evaluacion numérica
                px = sym.lambdify(x, polSimp)
                print("El valor del punto es", px(2.3))

                # Puntos para la gráfica
                muestras = 101
                a = np.min(xi)
                b = np.max(xi)
                pxi = np.linspace(a, b, muestras)
                pfi = px(pxi)

                # SALIDA
                np.set_printoptions(precision=4)
                print('Tabla Diferencia Dividida')
                # print([titulo])
                # print(tabla)
                print(tabulate(tabla, headers=titulo, tablefmt="pretty"))
                print('dDividida: ')
                print(dDividida)
                print('pol: ')
                print(pol)
                print('pol simplificado: ')
                print(polSimp)

                # Gráfica
                plt.plot(xi, fi, 'o', label='Puntos')
                ##for i in range(0,n,1):
                ##    plt.axvline(xi[i],ls='--', color='yellow')
                plt.plot(pxi, pfi, label='pol')
                plt.legend()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Diferencias Divididas - Newton')
                plt.show()

            # Opcion 4 Interpolacion de Hermite
            elif metodo == 4:
                #Solicitamos el usuario la funcion
                fn = input("Ingrese la funcion en terminos de x\nf(x): ")
                dfn=sym.diff(fn)

                #Imprimimos la funcion y su derivada
                print("f(x)= ", fn)
                print("f'(x)= ", dfn)
                #creamos dos listas vacias para guardar los datos
                X = []
                Fx = []
                #Pedimos que ingrese el grado del pol a calcular
                n = int(input("\x1b[0;31m" + "Ingrese el grado del pol "))
                #Recordamos al usuario que necesitamos n+1 puntos
                print("\x1b[1;33m"+"Recuerde que para un pol de grado n, necesitamos n+1 puntos ")
                #Esperamos un tiempo
                time.sleep(2)
                #Creamos una lista vacia
                data = []
                #Solicitamos los datos
                for i in range(n+1):
                    #Empezamos a pedir los datos de x
                    x = float(input("\x1b[1;32m" + "Ingrese los valores de x "))
                    #Almacenamos estos valores en la lista
                    X.append(x)
                    # Empezamos a pedir los datos de fx
                    y = float(input("\x1b[1;33m" + "Ingrese los valores de Fx "))
                    # Almacenamos estos valores en la lista
                    Fx.append(y)
                    #
                    data.append([x, y])

                # Tabla de Diferencias Divididas Avanzadas
                n = len(X)

                # diferencias divididas vacia
                dfinita = np.zeros(shape=(n, n), dtype=float)
                data = np.concatenate((data, dfinita), axis=1)
                indice=0
                while indice<n:
                    b0=Fx[0]
                    b1=(Fx[indice+1]-Fx[indice])/(X[indice+1]-X[indice])
                    print(b1)
                    indice+=1

                print("\x1b[1;34m")
                print(X)
                print("\x1b[1;36m",end='')
                print(Fx)
                print("\x1b[1;30m")
                print(tabulate(data, headers=["x", "f(x)",""], tablefmt="pretty"))
                break
            else:
                break

            metodo = int(input("\x1b[3;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
                "\n3.Diferencias Divididas\n4.pol de Hermite\nOtro numero para salir "+"\x1b[0;30m"))