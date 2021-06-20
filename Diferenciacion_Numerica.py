import sympy
from tabulate import tabulate

def Diferenciacion():
    x = sympy.symbols('x')
    print("..:Bienvenido:..")
    print("..Derivacion numerica..")
    opc = int(input("Ingrese el numero de la opcion deseada\n1.Diferencia finita \n2.Extrapolacion de Richardson\nOtro numero para salir "))

    while opc > 0 and opc < 3:
        if opc == 1:
            opc2 = int(input(
                "que metodo desea realizar\n1.Diferencia finita hacia adelante \n2.Diferencia finita hacia atras \n3.diferencia finita centrada"
                "\n4.Formula de los tres puntos \n5.Formula de los cinco puntos\n6.Diferencias de orden superior\n7.Cualquier numero para Salir "))
            while opc2 > 0 and opc2 < 7:
                if opc2 == 1:

                    fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    X = float(input("digite el valor de X "))
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
                    fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    X = float(input("digite el valor de X "))
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
                    fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    X = float(input("digite el valor de X "))
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
                    fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    X = float(input("digite el valor de X "))
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
                    fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    X = float(input("digite el valor de X "))
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
                    # Creo una tabla para pegar en ella los datos obtenidos
                    oncemore = iter([True, False])
                    data = []

                    # mantengo en el menu al usuario mientras el desee
                    continuar = 1
                    while (continuar == 1):

                        # Defino la funcion
                        def f(x):
                            # y=fx
                            y = x ** 4 + 2 * x ** 3
                            return (y)

                        # El usuario ingresara el valor de x
                        xi = float(input("Ingrese el valor de x\n"))

                        # Obtengo las derivada evaluadas en el punto que seran el valor verdadero

                        der2 = sympy.diff(x ** 4 + 2 * x ** 3, x, 2).subs(x, xi)
                        der3 = sympy.diff(x ** 4 + 2 * x ** 3, x, 3).subs(x, xi)
                        der4 = sympy.diff(x ** 4 + 2 * x ** 3, x, 4).subs(x, xi)

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
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))

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
                                print("Para primer diferencia hacia adelante con: x=" + str(xi) + " y h=" + str(
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
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
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
                                print("Para primer diferencia hacia adelante con: x=" + str(xi) + " y h=" + str(
                                    h) + " se obtuvo:")
                                # Imprimo los valores en la tabla creada
                                data.append(["Segunda", segunda, eSegunda])
                                data.append(["Tercera", tercera, eTercera])
                                data.append(["Cuarta", cuarta, eCuarta])

                            # segunda diferencia
                            if (diferencia == 2):
                                segunda = (2 * f(xi) - 5 * f(xi - h) + 4 * f(xi - 2 * h) - f(xi - 3 * h)) / (h ** 2)
                                tercera = (5 * f(xi) - 18 * f(xi - h) + 24 * f(xi - 2 * h) - 14 * f(xi - 3 * h) + 3 * f(
                                    xi - 4 * h)) / (2 * (h ** 3))
                                cuarta = (3 * f(xi) - 14 * f(xi - h) + 26 * f(xi - 2 * h) - 24 * f(xi - 3 * h) + 11 * f(
                                    xi - 4 * h) - 2 * f(xi - 5 * h)) / (h ** 4)
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

                        # central
                        if (opcion == 3):
                            diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                            while diferencia < 1 or diferencia > 2:
                                print("Diferecnia seleccionada no valida")
                                diferencia = int(input("¿cual diferencia desea encontrar?\n1.primera o 2.segunda\n"))
                            if (diferencia < 1 or diferencia > 2):
                                print("Opcion ingresada no valida")
                            # Primer diferencia
                            if (diferencia == 1):
                                segunda = (f(xi + h) - 2 * f(xi) + f(xi - h)) / (h ** 2)
                                tercera = (f(xi + 2 * h) - 2 * f(xi + h) + 2 * f(xi - h) - f(xi - 2 * h)) / (
                                            2 * (h ** 3))
                                cuarta = (f(xi + 2 * h) - 4 * f(xi + h) + 6 * f(xi) - 4 * f(xi - h) + f(xi - 2 * h)) / (
                                            h ** 4)
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
                                print("Para primer diferencia hacia adelante con: x=" + str(xi) + " y h=" + str(
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


                else:
                    break
