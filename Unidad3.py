import time
import sympy

#Creamos la clase Un3
class Un3:
    #Definimos la funcion U3
    def U3(self):
        #Desplegamos un menu
        metodo = int(input("\x1b[1;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
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
                print("3")

            # Opcion 4 Interpolacion de Hermite
            elif metodo == 4:
                #Solicitamos el usuario la funcion
                fn = input("\x1b[1;30m" + "Ingrese la funcion en terminos de x ")
                dfn=sympy.diff(fn)
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
                #Solicitamos los datos
                for i in range(n+1):
                    x = float(input("\x1b[1;32m" + "Ingrese los valores de x "))
                    X.append(x)
                    y = float(input("\x1b[1;33m" + "Ingrese los valores de Fx "))
                    Fx.append(y)
                print("\x1b[1;34m")
                print(X)
                print("\x1b[1;36m",end='')
                print(Fx)
                print("\x1b[1;35m")
                break
            else:
                break

            metodo = int(input("\x1b[0;35m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
                "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir "+"\x1b[0;30m"))