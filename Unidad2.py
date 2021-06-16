#Importamos las librerias necesarias
import numpy as np
from numpy import sign
from tabulate import tabulate
from matplotlib import pyplot as plt

#Creamos la clase U2
class Un2:
    #Definimos la funcion U2 que recibe el argumento tolerancia
    def U2(tolerancia):
        #Solicitamos al usuario que ingresa la funcion exponencial
        fx = input("Introduce la funcion exponencial en terminos de x ")
        #Validamos que en realidad se trate de una funcion exponencial
        if "**x" in fx or "exp(" in fx or "**-x" in fx:
            #Desplegamos un menu para que el usuario elija el metodo a utilizar
            metodo = int(input(
                "Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n"
                "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Bairstow\n9.Müller\nOtro numero para salir\n"))

            while metodo > 0 and metodo < 10:
                #Si la opcion es 1
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
                    break

                # Si la opcion es 2
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
                    break

                    if sign(fx1) != sign(fx2):
                        print("\nEl intervalo si contiene una raiz")
                    else:
                        print("Ingrese un intervalo valido")

                metodo = int(input(
                    "Ingrese el numero del metodo por el que desea resolver la funcion\n1.Ver grafico\n2.Biseccion\n3.Falsa Posicion\n"
                    "4.Punto fijo\n5.Newton Raphson\n6.Secante\n7.Bairstow\n9.Müller\nOtro numero para salir\n"))

        #Si la funcion no es exponencial devolvemos al usuario el mensaje
        else:
            print("Debe ingresar una funcion exponencial")