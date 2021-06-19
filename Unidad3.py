import time
import sympy as sym
import numpy as np
from tabulate import tabulate
import matplotlib.pyplot as plt
from math import *

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
                print("1")
            # Opcion 2 Polinomio de newton
            elif metodo == 2:
                print("2")
            # Opcion 3 Diferencias divididas
            elif metodo == 3:
                # Polinomio interpolación
                # Diferencias Divididas de Newton
                # INGRESO , Datos de prueba
                xi = np.array([5, 6, 7, 8, 9, 10])
                fi = np.array([3, 7, 6, 5, -2, 1])

                ####################### Por si se da la funcion #################
                # fi=[]
                # def poli(x):
                #     return (sin(x))*(log(x))

                # for y in xi:
                #     fi.append(poli(y))

                # fi = np.array(fi)
                #################################################################

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
                diagonal = n - 1
                j = 3
                while (j < m):
                    # Añade título para cada columna
                    titulo.append('F[' + str(j - 2) + ']')

                    # cada fila de columna
                    i = 0
                    paso = j - 2  # inicia en 1
                    while (i < diagonal):
                        denominador = (xi[i + paso] - xi[i])
                        numerador = tabla[i + 1, j - 1] - tabla[i, j - 1]
                        tabla[i, j] = numerador / denominador
                        i = i + 1
                    diagonal = diagonal - 1
                    j = j + 1

                # POLINOMIO con diferencias Divididas
                # caso: puntos equidistantes en eje x
                dDividida = tabla[0, 3:]
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
                print('polinomio: ')
                print(polinomio)
                print('polinomio simplificado: ')
                print(polisimple)

                # Gráfica
                plt.plot(xi, fi, 'o', label='Puntos')
                ##for i in range(0,n,1):
                ##    plt.axvline(xi[i],ls='--', color='yellow')
                plt.plot(pxi, pfi, label='Polinomio')
                plt.legend()
                plt.xlabel('X')
                plt.ylabel('Y')
                plt.title('Diferencias Divididas - Newton')
                plt.show()

            # Opcion 4 Interpolacion de Hermite
            elif metodo == 4:
                #Solicitamos el usuario la funcion
                fn = input("\x1b[1;30m" + "Ingrese la funcion en terminos de x ")
                dfn=sym.diff(fn)

                #Imprimimos la funcion y su derivada
                print("f(x)= ", fn)
                print("f'(x)= ", dfn)
                #creamos dos listas vacias para guardar los datos
                X = []
                Fx = []
                #Pedimos que ingrese el grado del polinomio a calcular
                n = int(input("\x1b[0;31m" + "Ingrese el grado del polinomio "))
                print("\x1b[1;33m"+"Recuerde que para un polinomio de grado n, necesitamos n+1 puntos ")
                time.sleep(2)
                data = []
                #Solicitamos los datos
                for i in range(n+1):
                    x = float(input("\x1b[1;32m" + "Ingrese los valores de x "))
                    X.append(x)
                    y = float(input("\x1b[1;33m" + "Ingrese los valores de Fx "))
                    Fx.append(y)
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
                "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir "+"\x1b[0;30m"))