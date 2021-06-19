import numpy as np
from tabulate import tabulate
from sympy import *
from matplotlib import pyplot
from math import *

#Creamos la clase Un5
class Un5:
    #Definimos la funcion principal U5
    def U5(self=None):
        opc = int(input("\x1b[3;35m"+"Ingrese el numero de la opcion deseada\n1.Metodo de Euler\n2.Metodo de Taylor\n3.Metodo de Runge Kutta\n4.Metodo adaptativo\nOtro numero para salir\n"))

        while opc > 0 and opc < 5:
            if opc==2:
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
                x,y=symbols("x y")

                try:
                    fn=eval(input("Ingrese la funcion f(x,y): "))
                    print(fn)
                except:
                    print("La funcion tiene un problema en sus sintaxis\nPor favor ingrese de nuevo la funcion ")
                #Por definicion n=4
                x0=float(input("Ingrese el valor incial de x0: "))
                y0 = float(input("Ingrese el valor incial de y0: "))
                while True:
                    h=float(input("Ingrese el tamaño de paso h: "))
                    if h<=0:
                        print("El tamaño de paso no puede cer cero o negativo")
                    else:

                        break
                xn=float(input("Ingrese el valor a calcular y(xn): "))
                itc=round(((xn-x0)/h))
                vx=[]
                vy=[]
                print("--------- Tabla de valores ---------")
                for i in range(1,itc+1):
                    k1=fn.subs([(x,x0),(y,y0)])
                    k2=fn.subs([(x,x0+h/2),(y,y0+(h/2)*k1)])
                    k3=fn.subs([(x,x0+h/2),(y,y0+(h/2)*k2)])
                    k4=fn.subs([(x,x0+h),(y,y0+h*k3)])
                    yn=y0+h/6*(k1+2*k2+2*k3+k4)
                    x0=round(x0+h,5)
                    y0=yn
                    print('y(',x0,')=',yn)
                break
            else:
                break