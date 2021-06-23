#Importamos las librerias necesarias
import sympy
import numpy as np
from tabulate import tabulate

#Creamos el metodo Diferenciacion
def Diferenciacion():
    #Definimos las variables a utilizar
    x = sympy.symbols('x')
    opc = int(input("\x1b[1;33m"+"Ingrese el numero de la opcion deseada\n1.Diferencias finitas \n2.Extrapolacion de Richardson\nOtro numero para salir "+"\x1b[1;35m"))

    while opc > 0 and opc < 3:
        if opc == 1:
            #Diferencias finitas
            opc2 = int(input("\x1b[1;35m"+"Que metodo desea realizar\n1.Diferencia finita hacia adelante \n2.Diferencia finita hacia atras \n3.Diferencia finita centrada"
                "\n4.Formula de los tres puntos \n5.Formula de los cinco puntos\n6.Diferencias de orden superior\n7.Cualquier numero para Salir "+"\x1b[1;30m"))
            while opc2 > 0 and opc2 < 7:
                #Diferencia finita hacia adelante
                if opc2 == 1:
                    #Pedimos la funcion al usuario
                    fx = input("\x1b[1;30m""Ingrese la funcion en terminos de x\nf(x): ")
                    #Validamos que la funcion ingresada sea algebraica
                    if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                        print("\x1b[1;31m"+"Asegurese de ingresar una funcion algebraica")
                    else:
                        # Solicitamos el valor de x
                        X = float(input("\x1b[0;30m" + "digite el valor de X "))
                        # Pedimos que ingrese el valor de h
                        h = float(input("digite el valor de h "))

                        # aca se calculara la diferencia finita hacia adelante primera diferencia
                        Efx = sympy.sympify(fx).subs(x, X)
                        fxh = X + h
                        Efxh = sympy.sympify(fx).subs(x, fxh)
                        dfx = (Efxh - Efx) / h
                        print("primera diferencia finita hacia adelante")
                        print("f(", X, ") = ", dfx)
                        # ahora calculamos el error

                        # aca se calculara la diferencia finita hacia adelante segunda diferencia
                        X2h = X + 2 * h
                        EX2h = sympy.sympify(fx).subs(x, X2h)
                        dfx2 = (-EX2h + (4 * Efxh) - (3 * Efx)) / (2 * h)
                        print("segunda diferencia finita hacia adelante")
                        print("f'(", X, ") = ", dfx2)

                elif opc2 == 2:
                    # Pedimos la funcion al usuario
                    fx = input("\x1b[1;30m""Ingrese la funcion en terminos de x\nf(x): ")
                    # Validamos que la funcion ingresada sea algebraica
                    if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                        print("\x1b[1;31m"+"Asegurese de ingresar una funcion algebraica")
                    else:
                        # Solicitamos el valor de x
                        X = float(input("\x1b[0;30m" + "digite el valor de X "))
                        # Pedimos que ingrese el valor de h
                        h = float(input("digite el valor de h "))
                        # aca se calcula la primera diferencia hacia atras
                        Efx = sympy.sympify(fx).subs(x, X)
                        fxh = X - h
                        Efxh = sympy.sympify(fx).subs(x, fxh)
                        dfx = (Efx - Efxh) / h
                        print("primera diferencia finita hacia atras")
                        print("f'(", X, ") = ", dfx)
                        # aca se calcula la diferencia finita hacia atras-segunda diferencia
                        X2h = X - 2 * h
                        EX2h = sympy.sympify(fx).subs(x, X2h)
                        dfx2 = ((3 * Efx) - 4 * (fxh) + EX2h) / (2 * h)
                        print("segunda diferencia finita hacia adelante")
                        print("f'(", X, ") = ", dfx2)

                elif opc2 == 3:
                    # para diferencia finita centrada, haremos uso solo de la orden cuatro
                    # Pedimos la funcion al usuario
                    fx = input("\x1b[1;30m""Ingrese la funcion en terminos de x\nf(x): ")
                    # Validamos que la funcion ingresada sea algebraica
                    if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                        print("\x1b[1;31m" + "Asegurese de ingresar una funcion algebraica")
                    else:
                        # Solicitamos el valor de x
                        X = float(input("\x1b[0;30m" + "digite el valor de X "))
                        # Pedimos que ingrese el valor de h
                        h = float(input("digite el valor de h "))
                        X2h = X + 2 * h
                        EX2h = sympy.sympify(fx).subs(x, X2h)
                        Xh = X + h
                        EXh = sympy.sympify(fx).subs(x, Xh)
                        rXh = X - h
                        ErXh = sympy.sympify(fx).subs(x, rXh)
                        rX2h = X - 2 * h
                        ErX2h = sympy.sympify(fx).subs(x, rX2h)
                        dfx = (-EX2h + (8 * EXh) - (8 * ErXh) + ErX2h) / (12 * h)
                        print("diferencia centrada, orden 4")
                        print("f'(", X, ") = ", dfx)

                elif opc2 == 4:
                    # formula de los 3 puntos
                    # Pedimos la funcion al usuario
                    fx = input("\x1b[1;30m""Ingrese la funcion en terminos de x\nf(x): ")
                    # Validamos que la funcion ingresada sea algebraica
                    if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                        print("\x1b[1;31m" + "Asegurese de ingresar una funcion algebraica")
                    else:
                        # Solicitamos el valor de x
                        X = float(input("\x1b[0;30m" + "digite el valor de X "))
                        # Pedimos que ingrese el valor de h
                        h = float(input("digite el valor de h "))
                        Efx = sympy.sympify(fx).subs(x, fx)
                        X2h = X + 2 * h
                        EX2h = sympy.sympify(fx).subs(x, X2h)
                        Xh = X + h
                        EXh = sympy.sympify(fx).subs(x, Xh)
                        dfx = ((-3 * Efx) + 4 * (fxh) - EX2h) / (2 * h)
                        print("formula de los tres puntos")
                        print("f'(", X, ") = ", dfx)

                elif opc2 == 5:
                    # formula de los 5 puntos
                    # la formula que se usara es la que genera mayor exactitud
                    # Pedimos la funcion al usuario
                    fx = input("\x1b[1;30m""Ingrese la funcion en terminos de x\nf(x): ")
                    # Validamos que la funcion ingresada sea algebraica
                    if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                        print("\x1b[1;31m" + "Asegurese de ingresar una funcion algebraica")
                    else:
                        # Solicitamos el valor de x
                        X = float(input("\x1b[0;30m" + "digite el valor de X "))
                        # Pedimos que ingrese el valor de h
                        h = float(input("digite el valor de h "))
                        X2h = X + (2 * h)
                        EX2h = sympy.sympify(fx).subs(x, X2h)
                        Xh = X + h
                        EXh = sympy.sympify(fx).subs(x, Xh)
                        rXh = X - h
                        ErXh = sympy.sympify(fx).subs(x, rXh)
                        rX2h = X - (2 * h)
                        ErX2h = sympy.sympify(fx).subs(x, rX2h)
                        dfx = (1 / 12 * h) * (rX2h + 8 * EXh - 8 * ErXh - EX2h)
                        print("formula de los cinco puntos")
                        print("f'(", X, ") = ", dfx)

                elif opc2==6:
                    #Diferencias de orden superior
                    x = sympy.symbols('x')
                    oncemore = iter([True, False])
                    data = []

                    # mantengo en el menu al usuario mientras el desee
                    continuar = 1
                    while (continuar == 1):

                        # Obtengo la función
                        funsion = input("\x1b[1;30m""Ingrese la funcion\nf(x)= ")
                        # Validamos que la funcion ingresada sea algebraica
                        if "sin(" in funsion or "cos(" in funsion or "tan(" in funsion or "cos(" in funsion or "asin(" in funsion or "acos(" in funsion or "atan(" in funsion or "e**" in funsion or "exp(" in funsion or "log(" in funsion or "ln(" in funsion or "e*" in funsion:
                            print("\x1b[1;31m" + "Asegurese de ingresar una funcion algebraica")
                        else:
                            # defino la funcion
                            def f(valor):
                                y = sympy.sympify(funsion).subs(x, valor)
                                return (y)

                            # El usuario ingresara el valor de x
                            xi = float(input("\x1b[0;33m" + "Ingrese el valor de x\n"))

                            # Obtengo las derivada evaluadas en el punto que seran el valor verdadero
                            der2 = sympy.diff(funsion, x, 2).subs(x, xi)
                            der3 = sympy.diff(funsion, x, 3).subs(x, xi)
                            der4 = sympy.diff(funsion, x, 4).subs(x, xi)
                            print(der2)
                            print(der3)
                            print(der4)

                            # obtengo el valor de h
                            h = float(input("Ingrese el valor de h\n"))
                            opcion = int(input(
                                "Ingrese el tipo de diferenciacion que desea:\n1.Hacia adelante.\n2.Hacia atras.\n3.Central\n"))

                            # Hacia Adelante
                            if (opcion == 1):
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                                while diferencia < 1 or diferencia > 2:
                                    print("Diferecnia seleccionada no valida")
                                    diferencia = int(
                                        input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))

                                # Primer diferencia
                                if (diferencia == 1):
                                    segunda = (f(xi + 2 * h) - 2 * f(xi + h) + f(xi)) / (h ** 2)
                                    tercera = (f(xi) - 3 * f(xi - h) + 3 * f(xi - 2 * h) - f(xi - 3 * h)) / (h ** 3)
                                    cuarta = (f(xi) - 4 * f(xi - h) + 6 * f(xi - 2 * h) - 4 * f(xi - 3 * h) + f(
                                        xi - 4 * h)) / (h ** 4)
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para primer diferencia hacia adelante con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                                # segunda diferencia
                                if (diferencia == 2):
                                    segunda = (-1 * f(xi + 3 * h) + 4 * f(xi + 2 * h) - 5 * f(xi + h) + 2 * f(xi)) / (
                                            h ** 2)
                                    tercera = (-3 * f(xi + 4 * h) + 14 * f(xi + 3 * h) - 24 * f(xi + 2 * h) + 18 * f(
                                        xi + h) - 5 * f(xi)) / (2 * (h ** 3))
                                    cuarta = (-2 * f(xi + 5 * h) + 11 * f(xi + 4 * h) - 24 * f(xi + 3 * h) + 26 * f(
                                        xi + h) + 3 * f(xi)) / (h ** 4)
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para segunda diferencia hacia adelante con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                            # hacia atras
                            if (opcion == 2):
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                                while diferencia < 1 or diferencia > 2:
                                    print("Diferecnia seleccionada no valida")
                                    diferencia = int(
                                        input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                                # Primer diferencia
                                if (diferencia == 1):
                                    segunda = (f(xi) - 2 * f(xi - h) + f(xi - 2 * h)) / (h ** 2)
                                    tercera = (f(xi) - 3 * f(xi - h) + 3 * f(xi - 2 * h) - f(xi - 3 * h)) / (h ** 3)
                                    cuarta = (f(xi) - 4 * f(xi - h) + 6 * f(xi - 2 * h) - 4 * f(xi - 3 * h) + f(
                                        xi - 4 * h)) / (h ** 4)
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para primer diferencia hacia atrás con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                                # segunda diferencia
                                if (diferencia == 2):
                                    segunda = (2 * f(xi) - 5 * f(xi - h) + 4 * f(xi - 2 * h) - f(xi - 3 * h)) / (h ** 2)
                                    tercera = (5 * f(xi) - 18 * f(xi - h) + 24 * f(xi - 2 * h) - 14 * f(
                                        xi - 3 * h) + 3 * f(
                                        xi - 4 * h)) / (2 * (h ** 3))
                                    cuarta = (3 * f(xi) - 14 * f(xi - h) + 26 * f(xi - 2 * h) - 24 * f(
                                        xi - 3 * h) + 11 * f(
                                        xi - 4 * h) - 2 * f(xi - 5 * h)) / (h ** 4)
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para segunda diferencia hacia atrás con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                            # central
                            if (opcion == 3):
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                                while diferencia < 1 or diferencia > 2:
                                    print("Diferecnia seleccionada no valida")
                                    diferencia = int(
                                        input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                                if (diferencia < 1 or diferencia > 2):
                                    print("Opcion ingresada no valida")
                                # Primer diferencia
                                if (diferencia == 1):
                                    segunda = (f(xi + h) - 2 * f(xi) + f(xi - h)) / (h ** 2)
                                    tercera = (f(xi + 2 * h) - 2 * f(xi + h) + 2 * f(xi - h) - f(xi - 2 * h)) / (
                                            2 * (h ** 3))
                                    cuarta = (f(xi + 2 * h) - 4 * f(xi + h) + 6 * f(xi) - 4 * f(xi - h) + f(
                                        xi - 2 * h)) / (
                                                     h ** 4)
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para primer diferencia central con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                                # segunda diferencia
                                if (diferencia == 2):
                                    segunda = (-1 * f(xi + 2 * h) + 16 * f(xi + h) - 30 * f(xi) + 16 * f(xi - h) - f(
                                        xi - 2 * h)) / (12 * (h ** 2))
                                    tercera = (-1 * f(xi + 3 * h) + 8 * f(xi + 2 * h) - 12 * f(xi + h) + 12 * f(
                                        xi - h) - 8 * f(xi - 2 * h) + f(xi - 3 * h)) / (8 * (h ** 3))
                                    cuarta = (-1 * f(xi + 3 * h) + 12 * f(xi + 2 * h) - 39 * f(xi + h) + 56 * f(
                                        xi) - 39 * f(xi - h) + 12 * f(xi - 2 * h) - f(xi - 3 * h)) / ((6 * (h ** 4)))
                                    # Calculor el error de cada aproximacion
                                    eSegunda = abs((der2 - segunda) / der2) * 100
                                    eTercera = abs((der3 - tercera) / der3) * 100
                                    eCuarta = abs((der4 - cuarta) / der4) * 100
                                    print("Para segunda diferencia central con: x=" + str(xi) + " y h=" + str(
                                        h) + " se obtuvo:")
                                    # Imprimo los valores en la tabla creada
                                    data.append(["Segunda", segunda, eSegunda])
                                    data.append(["Tercera", tercera, eTercera])
                                    data.append(["Cuarta", cuarta, eCuarta])

                            # Genero el encabezado de la tabla,ademas de imprimir los valores obtenidos
                            print(tabulate(data, headers=["Derivada", "f(x)", "E"], tablefmt="orgtbl"))
                            # controlo el error de la opcion
                            if (opcion < 1 or opcion > 3):
                                print("Opcion ingresada no valida")
                            continuar = int(input("¿Desea seguir?\n1.si\nCualquier otro numero para salir\n"))

                        print("**EJECUCION FINALIZADA**")

                opc2 = int(input(
                    "\x1b[1;35m" + "Que metodo desea realizar\n1.Diferencia finita hacia adelante \n2.Diferencia finita hacia atras \n3.Diferencia finita centrada"
                                   "\n4.Formula de los tres puntos \n5.Formula de los cinco puntos\n6.Diferencias de orden superior\n7.Cualquier numero para Salir " + "\x1b[1;30m"))


        elif opc==2:
            #Extrapolacion de Richardson
            # declaramos x como variable independiente
            x = sympy.symbols("x")
            # pedimos la funcion que se quiere derivar asi como x, h y m que sera la cantidad de niveles a utilizar
            fx = input("\x1b[1;30m"+"ingrese la funcion a utilizar: ")
            # Validamos que la funcion ingresada sea algebraica
            if "sin(" in fx or "cos(" in fx or "tan(" in fx or "cos(" in fx or "asin(" in fx or "acos(" in fx or "atan(" in fx or "e**" in fx or "exp(" in fx or "log(" in fx or "ln(" in fx or "e*" in fx:
                print("\x1b[1;31m" + "Asegurese de ingresar una funcion algebraica")
            else:
                X0 = float(input("\x1b[0;30m"+"digite el valor de X: "))
                h = float(input("digite el valor de h: "))
                m = int(input("digite la cantidad de niveles a utilizar: "))

                # funcion en la cual se calcula diferencia de tres puntos
                # A esta funcion de python se le esta pasando como parametro fx que es la funcion que ingresa el usuario
                # X que es el valo que ingresa el usuario y h de igual manera que lo ingresa el usuario
                def tres_puntos(fx, X, h):
                    # se declara a "x" como una variable independiente
                    x = sympy.symbols("x")
                    # con sympy.sympify se evalua determinado valor en la funcion original, en este caso se evalua "X", que es el valor ingresado por el usuario
                    Efx = sympy.sympify(fx).subs(x, X)
                    X2h = X + 2 * h
                    EX2h = sympy.sympify(fx).subs(x, X2h)
                    Xh = X + h
                    EXh = sympy.sympify(fx).subs(x, Xh)
                    # dfx es la aproximacion de la derivada con el metodo de los tres puntos
                    dfx = (((-3 * Efx) + (4 * (EXh)) - EX2h) / (2 * h))
                    # la funcion tres_punto retornara el valor que se obtenga del calculo de la derivada a traves del metodo de los tres puntos
                    return dfx

                # la funcion extra_richardson espera fx que es la funcion ingresada por el usuario
                # ademas espera el X,h que son valores ingresados por el usuario
                # y espera el valor de m que es el nivel hasta el cual el usuario desea llegar
                def extra_richardson(fx, X, h, m):
                    # se declara a "x" como variable independiente
                    x = sympy.symbols("x")
                    # inicializamos un array con la libreria numpy, al principio con valores de cero, y ademas de indicarle que sean float los valores a utilizar.
                    N = np.zeros((m, m), dtype="float")
                    # se crea el bucle for que va de 0 hasta el nivel ingresado por el usuario
                    for i in range(0, m):
                        # en este punto se hace el llamado a la funcion tres_puntos a la que se le indica como parametro fx que es la funcion ingresada por el usuario, asi como x y h
                        N[i, 0] = tres_puntos(fx, X, h)
                        for j in range(1, i + 1):
                            # ecuacion para calcular la derivada apartir del nivel 2
                            N[i, j] = N[i, j - 1] + (N[i, j - 1] - N[i - 1, j - 1]) / (4 ** j - 1)
                        # h se divide siempre entre 2
                        h = h / 2
                        # se retorna los array con los valores resultantes en cada iteracion
                    return N

                # llamada a la funcion extra_richardson y ademas se le pasan los parametros que se necesitan para que esta funcione
                richardson = extra_richardson(fx, X0, h, m)
                # se imprimer los resultados
                print(richardson)

        opc = int(input("\x1b[1;33m" + "Ingrese el numero de la opcion deseada\n1.Diferencias finitas \n2.Extrapolacion de Richardson\nOtro numero para salir " + "\x1b[1;35m"))
