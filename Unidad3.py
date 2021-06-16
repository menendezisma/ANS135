class Un3:
    def U3(self):
        metodo = int(input("\x1b[0;34m"+"Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
            "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir\n"))

        while metodo > 0 and metodo < 5:
            if metodo == 1:
                print("1")
            elif metodo == 2:
                print("2")
            elif metodo == 3:
                print("3")
            elif metodo == 4:
                Fn = int(input("\x1b[0;34m" + "Ingrese la funcion en terminos de x "))
                X = []
                Fx = []
                n = int(input("\x1b[0;31m" + "Ingrese el grado del polinomio "))
                for i in range(n):
                    x = float(input("\x1b[1;32m" + "Ingrese los valores de x "))
                    X.append(x)
                    y = float(input("\x1b[1;33m" + "Ingrese los valores de Fx "))
                    Fx.append(y)
                print(X)
                print(Fx)
                break
            else:
                break

            metodo = int(input("Ingrese el numero del metodo por el que desea aproximar la raiz\n1.Interpolación de Lagrange\n2.Interpolación del polinomio de Newton"
                "\n3.Diferencias Divididas\n4.Polinomio de Hermite\nOtro numero para salir\n"))