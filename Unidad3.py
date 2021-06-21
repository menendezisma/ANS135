import sympy as sym
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt

#Creamos la clase Un3
class Un3:
    #Definimos la funcion U3
    def U3(self):
        #Desplegamos un menu
        metodo = int(input("\x1b[3;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
            "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir "+"\x1b[0;30m"))

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
                        #Declaro las listas necesarias
                        data = []
                        xi = []
                        fi = []
                        #Declaro la variable a utilizar
                        x = sym.Symbol('x')
                        y = 0
                        num = 1
                        denom = 1
                        polinomio = 0

                        #Solicito al usuario que ingrese la funcion
                        funcion = input("Ingrese la funcion en terms de x\nf(x): ")
                        lista = funcion.split()
                        for i in lista:
                            # Solicitando datos al usuario para la funcion
                            print("Ingrese el valor del intervalo a evaluar ")
                            x0 = float(input("Ingrese el valor x0: "))
                            x1 = float(input("Ingrese el valor x1: "))

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

                            # procedimiento de Langrage
                            for y in range(0, nDatos, 1):
                                num = 1
                                denom = 1
                                for j in range(0, nDatos, 1):
                                    if y != j:
                                        num = num * (x - xi[j])
                                        denom = denom * (xi[y] - xi[j])
                                    term = (num / denom) * fi[y]
                                polinomio = polinomio + term
                            polSim = sym.expand(polinomio)
                            funcion = " ", polSim
                            print("polinomio: \n", polinomio)
                            print("\npolinomio Simple: \n", polSim)
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
                        num = 1
                        denom = 1
                        polinomio = 0

                        #Solicitamos al ususario que ingrese la funcion
                        funcion = input("Ingrese la funcion en terms de x\nf(x): ")
                        lista = funcion.split()
                        for i in lista:
                            # Solicitando datos al usuario para la funcion
                            print("Ingrese el valor del intervalo a evaluar ")
                            x0 = float(input("Ingrese el valor x0: "))
                            x1 = float(input("Ingrese el valor x1: "))

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
                                    denom = (xi[i + (j - 2)] - xi[i])
                                    num = data[i + 1, j - 1] - data[i, j - 1]
                                    data[i, j] = num / denom
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
                                term = 1
                                for k in range(0, j, 1):
                                    term = term * (x - xi[k])
                                polinomio = polinomio + term * factor

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
                                x = float(input("Ingrese el valor de x "))
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
                #Calculamos el polinomio de hermite por medio de las derivadas por posicion
                #Creamos las listas que vamos a utilizar
                data = []
                xi = []
                fi = []
                fk = []
                lx = []
                derivada = []
                evaluado = []
                expresionElevada = []
                Hn = []
                Kn = []
                #Creamos un lista con los nombres de los titulos
                titulo = ["k", "Xk", "f(Xk)", "f'(k)"]
                #Declaramos la variable a utilizar
                x = sym.Symbol('x')
                y = 0
                num = 1
                denom = 1
                polinomio = 0
                #Pedimos al usuario que ingrese la cantidad de datos
                nDatos = int(input("Ingrese la cantidad de datos "))
                #Solicitamos que ingrese la cantidad de derivadas
                nDerivada = int(input("Ingrese la cantidad de derivada "))
                for i in range(nDatos):
                    #Pedimos al usuario que ingrese los datos y los almacenamos en las listas
                    datoXi = float(input("Ingrese el dato numero x{}: ".format(i)))
                    xi.append(datoXi)
                    datoFi = float(input("Ingrese el dato numero y{}: ".format(i)))
                    fi.append(datoFi)
                    datoFk = float(input("Ingrese el dato numero f'{}: ".format(i)))
                    fk.append(datoFk)
                    data.append([i, datoXi, datoFi, datoFk])
                print(tabulate(data, headers=titulo, tablefmt="pretty"))
                # Utilizando el metodo de lagrange
                for y in range(0, nDatos, 1):
                    num = 1
                    denom = 1
                    for j in range(0, nDatos, 1):
                        if y != j:
                            num = num * (x - xi[j])
                            denom = denom * (xi[y] - xi[j])
                        term = (num / denom)
                    lx.append(term)
                    polinomio = polinomio + term

                # Imprimiendo los datos de L + calculando su derivada
                print("\n------ Encontrado el valor de L(n,j) ------")
                for z in range(len(lx)):
                    #Imprimimoso el valor de L al usuario
                    print("L{}: ".format(z), lx[z])
                    y = lx[z]
                    deri = y.diff(x)
                    derivada.append(deri)
                    print("L'{}: ".format(z), derivada[z])

                print("\n------ Evaluando los valores de x en derivada ------")
                # Evaluando los valores de x en derivada
                for t in range(len(lx)):
                    exp = derivada[t]
                    x = xi[t]
                    evaluacion = eval(str(exp))
                    evaluado.append(evaluacion)
                    #imprimimos el valor de L
                    print("L'{}(".format(z), x, "): ", evaluacion)
                # Encontramos los valores de L
                print("\n------ El valor de ln ------")
                for u in range(len(lx)):
                    lCuadrado = (lx[u]) ** 2
                    elevado = lCuadrado.expand()
                    expresionElevada.append(elevado)

                    print("(L{})^2:".format(u), expresionElevada[u])
                # Encontramos los valor de H
                print("\n------ Los valores H(n,j) ------")
                for q in range(len(lx)):
                    #definimos nuestra variable
                    x = sym.Symbol('x')
                    lCuadrado = expresionElevada[q]
                    lEvaluado = evaluado[q]
                    formu = (1 - 2 * (lEvaluado) * (x - xi[q]))
                    poly = (lCuadrado * formu)
                    expre = poly.expand()
                    Hn.append(expre)
                    #imprimimos los valores de H(n,j)
                    print("H{}(x)=".format(q), Hn[q])

                # Encontramos los valores de K
                print("\n------ Encontrado los valores Kn ------")
                for r in range(len(lx)):
                    x = sym.Symbol('x')
                    lCuadrado = expresionElevada[r]
                    formu = ((x - xi[r]))
                    poly = (lCuadrado * formu)
                    expre = poly.expand()
                    Kn.append(expre)
                    #Imprimimos los valores de K
                    print("K{}(x)=".format(r), Kn[r])

                #Una ves teniendo todos los valores
                print("\n------ Calculando el polinomio ------")
                termino = 1
                pol = 0
                for g in range(len(lx)):
                    primerTermino = (fi[g] * Hn[g])
                    segundoTermino = (fk[g] * Kn[g])
                    print(primerTermino)
                    print(segundoTermino)
                    formu = primerTermino + segundoTermino
                    print("formula: ", formu)
                    termino = termino + formu
                pol = pol + termino
                poliSim = sym.expand(pol)
                funcion = " ", poliSim
                print("polinomio: \n", polinomio)
                print("\npolinomio Simple: \n", poliSim)

                opcion = input("****  ¿Desea evaluar algun punto en X?\n1. Si \n2. No\n")
                if opcion == '1':
                    x = float(input("Ingrese el valor de x \t"))
                    px = eval(str(polSim))
                    print("valor evaluado es: ", px)
                if opcion == 2:
                    print("Programa finalizado")
                    break
            else:
                break

            metodo = int(input("\x1b[3;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
                "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir "+"\x1b[0;30m"))