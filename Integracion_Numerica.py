#importamos las librerias a utilizar
import sympy
from tabulate import tabulate
from math import e

#Definimos la funcion U4
def Integracion():
    #Desplegamos un menu
    print("..:Bienvenido:..")
    print("..Integracion numerica..")
    opc = int(input("Ingrese el numero de la opcion deseada\n1.Reglas de integracion numerica \n2.Integracion por Rosemberg\nOtro numero para salir\n "))
    while opc > 0 and opc < 3:
        #Reglas de integracion numerica
        if opc==1:
            # Desplegamos un menu
            opcion = int(input("\x1b[3;31m" + "Ingrese el numero de la regla para aproximar el valor de la integral\n""1.Trapecio Simple\n2.Trapecio compuesto\n3.Simpson 1/3 simple\n4.Simpson 1/3 compuesto\n5.Simpson 3/8 simple\n6.Simpson 3/8 compuesto\nOtro numero para salir " + "\x1b[0;30m"))
            while opcion > 0 or opcion < 7:
                # Trapecio simple
                if opcion == 1:
                    # Definimos nuestra variable independiente
                    x = sympy.symbols('x')
                    # Solicitamos al usuario que ingrese la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Pedimos el extremo inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # Pedimos el extremo superior del intervalo
                    b = int(input("Ingrese el valor de b "))
                    if (a < b):
                        # evaluamos el intervalo inferior en la funcion
                        A = sympy.sympify(Fx).subs(x, a)
                        # evaluamos el intervalo superior en la funcion
                        B = sympy.sympify(Fx).subs(x, b)

                        # Calculamos el valor aproximado por la regla de trapecio simple
                        TS = float((b - a) * ((A + B) / 2))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;36m", "El valor Aproximado de la integral por la regla del Trapecio Simple es ",
                              TS,
                              "\x1b[0;30m")
                    else:
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                # Trapecio Compuesto
                elif opcion == 2:
                    # Solicitamos el valor de los subintervalos
                    n = int(input("Ingrese el valor de n "))
                    # definimos la variable independiente
                    x = sympy.symbols('x')
                    # Pedimos al usuario la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Solicitamos el valor inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # Solicitamos el valor superior del intervalo
                    b = int(input("Ingrese el valor de b "))

                    if (a < b):
                        # Evaluamos el intervalo inferior en la funcion
                        A = sympy.sympify(Fx).subs(x, a)
                        # Evaluamos el intervalo superior en la funcion
                        B = sympy.sympify(Fx).subs(x, b)

                        # Calculamos en valor de la separacion entre cada subintervalo
                        h = (b - a) / n

                        # creamos una lista vacia
                        data = []
                        # Creamos la variable sigma que almacenara la sumatoria de todas las funciones evaluadas en x
                        sigma = 0
                        # definimos que el incremento empiece desde el intervalo inferior
                        i = a
                        # creamos un bucle para ir evaluando cada subintervalo en la funcion
                        while i <= b:
                            # evaluamos los subintervalos en la funcion
                            fxi = sympy.sympify(Fx).subs(x, i)
                            # Vamos sumando los valores de la evaluacion
                            sigma += fxi
                            # Pasamos los datos a nuesta tabla
                            data.append([i, fxi])
                            # incrementamos las interaciones en h
                            i += h
                        # imprimimos nuestra tabla
                        print(tabulate(data, headers=["Xi", "f(xi)"], showindex=True, tablefmt="pretty"))

                        # A la sumatoria de todas la evaluacion de las funciones le restamos el valor evaluado en los extremos del intervalo
                        sumatoria = sigma - (A + B)
                        # calculamos el valor de la regla del trapcio compuesto
                        TC = float((b - a) * ((A + (2 * sumatoria) + B) / (2 * n)))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;35m", "El valor aproximado de la integral por la regla del Trapecio Compuesto",
                              TC,
                              "\x1b[0;30m")
                    else:
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                # Simpson 1/3 simple
                elif opcion == 3:
                    # Definimos nuestra variable independiente
                    x = sympy.symbols('x')
                    # Solicitamos al usuario que ingrese la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Pedimos el extremo inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # evaluamos el intervalo inferior en la funcion
                    b = int(input("Ingrese el valor de b "))
                    # evaluamos el intervalo superior en la funcion

                    if (a < b):
                        A = sympy.sympify(Fx).subs(x, a)
                        # Pedimos el extremo superior del intervalo
                        B = sympy.sympify(Fx).subs(x, b)
                        # Calculamos el punto medio del intervalo
                        Xm = (a + b) / 2
                        # Evaluamos la funcion en el punto medio
                        Fxm = sympy.sympify(Fx).subs(x, Xm)

                        # Calculamos el valor aproximado por la regla de trapecio simple
                        S13S = float((b - a) * ((A + 4 * Fxm + B) / 6))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;36m", "El valor Aproximado de la integral por la regla de Simpson 1/3 Simple es ",
                              S13S,
                              "\x1b[0;30m")
                    else:
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                # Simpson 1/3 compuesto
                elif opcion == 4:
                    # Solicitamos el valor de los subintervalos
                    n = int(input("Ingrese el valor de n "))
                    # definimos la variable independiente
                    x = sympy.symbols('x')
                    # Pedimos al usuario la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Solicitamos el valor inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # Solicitamos el valor superior del intervalo
                    b = int(input("Ingrese el valor de b "))

                    if (a < b):
                        # Evaluamos el intervalo inferior en la funcion
                        A = sympy.sympify(Fx).subs(x, a)
                        # Evaluamos el intervalo superior en la funcion
                        B = sympy.sympify(Fx).subs(x, b)

                        # Calculamos en valor de la separacion entre cada subintervalo
                        h = (b - a) / n

                        # creamos una lista vacia
                        data = []
                        # Creamos las variables sigma y plus que almacenaran la sumatoria de todas las funciones evaluadas en x y en los puntos medios
                        sigm = 0
                        plus = 0
                        # definimos que el incremento empiece desde el intervalo inferior
                        i = a
                        # creamos un bucle para ir evaluando cada subintervalo en la funcion
                        while i <= b:
                            # evaluamos los subintervalos en la funcion
                            fxi = sympy.sympify(Fx).subs(x, i)
                            # Vamos sumando los valores de la evaluacion
                            sigm += fxi
                            # Pasamos los datos a nuesta tabla
                            data.append([i, fxi])
                            # incrementamos las interaciones en h
                            i += h

                        # imprimimos nuestra tabla
                        print(tabulate(data, headers=["Xi", "f(xi)"], showindex=True, tablefmt="pretty"))

                        # Creamos otra lista vacia para mostrar los datos al usuario
                        dat = []
                        # Creamos la variable Med para calcular el punto medio del sub intervalo
                        Med = (a + h) / 2
                        # Asginamos a la variable iteracion que empiece desde Med
                        it = Med
                        while it <= b:
                            # evaluamos los el punto medio de los subintervalos en la funcion
                            fxmed = sympy.sympify(Fx).subs(x, it)
                            # Vamos sumando los valores de la evaluacion
                            plus += fxmed
                            # Pasamos los datos a nuesta tabla
                            dat.append([it, fxmed])
                            # incrementamos las interaciones en h
                            it += h

                        # imprimimos nuestra tabla
                        print(tabulate(dat, headers=["Xmi", "f(Xmi)"], showindex=True, tablefmt="pretty"))

                        # A la sumatoria de todas la evaluacion de las funciones le restamos el valor evaluado en los extremos del intervalo
                        sumat = sigm - (A + B)
                        # calculamos el valor de la regla del trapcio compuesto
                        S13C = float((b - a) * ((A + (4 * plus) + (2 * sumat) + B) / (6 * n)))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;35m", "El valor aproximado de la integral por la regla del Trapecio Compuesto",
                              S13C,
                              "\x1b[0;30m")
                    else:
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                # Simpson 3/8 simple
                elif opcion == 5:
                    # Por definicion sabemos que n=3 para simpson 3/8 simple
                    n = 3
                    # definimos la variable independiente
                    x = sympy.symbols('x')
                    # Pedimos al usuario la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Solicitamos el valor inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # Solicitamos el valor superior del intervalo
                    b = int(input("Ingrese el valor de b "))

                    if (a < b):
                        # Evaluamos el intervalo inferior en la funcion
                        A = sympy.sympify(Fx).subs(x, a)
                        # Evaluamos el intervalo superior en la funcion
                        B = sympy.sympify(Fx).subs(x, b)

                        # Calculamos en valor de la separacion entre cada subintervalo
                        h = (b - a) / n

                        # creamos una lista vacia
                        data = []
                        # Creamos la variable sigma que almacenara la sumatoria de todas las funciones evaluadas en x
                        sigma = 0
                        # definimos que el incremento empiece desde el intervalo inferior
                        i = a
                        # creamos un bucle para ir evaluando cada subintervalo en la funcion
                        while i <= b:
                            # evaluamos los subintervalos en la funcion
                            fxi = sympy.sympify(Fx).subs(x, i)
                            # Vamos sumando los valores de la evaluacion
                            sigma += fxi
                            # Pasamos los datos a nuesta tabla
                            data.append([i, fxi])
                            # incrementamos las interaciones en h
                            i += h
                        # imprimimos nuestra tabla
                        print(tabulate(data, headers=["Xi", "f(xi)"], showindex=True, tablefmt="pretty"))

                        # A la sumatoria de todas la evaluacion de las funciones le restamos el valor evaluado en los extremos del intervalo
                        sumatoria = sigma - (A + B)
                        # calculamos el valor de la regla del trapcio compuesto
                        S38S = float((b - a) * ((A + (3 * sumatoria) + B) / 8))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;35m", "El valor aproximado de la integral por la regla del Trapecio Compuesto",
                              S38S,
                              "\x1b[0;30m")
                    else:
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                # Simpson 3/8 compuesto
                elif opcion == 6:
                    # Solicitamos el valor de los subintervalos
                    n = int(input("Ingrese el valor de n "))
                    # definimos la variable independiente
                    x = sympy.symbols('x')
                    # Pedimos al usuario la funcion
                    Fx = input("Ingrese la funcion en terminos de x\nf(x): ")
                    # Solicitamos el valor inferior del intervalo
                    a = int(input("Ingrese el valor de a "))
                    # Solicitamos el valor superior del intervalo
                    b = int(input("Ingrese el valor de b "))

                    if (a < b):
                        # Evaluamos el intervalo inferior en la funcion
                        A = sympy.sympify(Fx).subs(x, a)
                        # Evaluamos el intervalo superior en la funcion
                        B = sympy.sympify(Fx).subs(x, b)

                        # Calculamos en valor de la separacion entre cada subintervalo
                        h = (b - a) / n

                        # creamos una lista vacia
                        data = []
                        # Creamos las variables sigma y plus que almacenaran la sumatoria de todas las funciones evaluadas en x y en los puntos medios
                        sigm = 0
                        plus = 0
                        # definimos que el incremento empiece desde el intervalo inferior
                        i = a
                        # Creamos la variable Med para calcular el punto medio del sub intervalo
                        Med = ((i + h) - i) / n
                        # Creamos otra lista vacia para mostrar los datos al usuario
                        dat = []
                        # Asginamos a la variable iteracion que empiece desde Med
                        it = a + Med
                        # creamos un bucle para ir evaluando cada subintervalo en la funcion
                        while i <= b:
                            while it <= b:
                                # evaluamos los el punto medio de los subintervalos en la funcion
                                fxmed = sympy.sympify(Fx).subs(x, it)
                                # Vamos sumando los valores de la evaluacion
                                plus += fxmed
                                # incrementamos las interaciones en h
                                it += Med

                            # evaluamos los subintervalos en la funcion
                            fxi = sympy.sympify(Fx).subs(x, i)
                            # Vamos sumando los valores de la evaluacion
                            sigm += fxi
                            # Pasamos los datos a nuesta tabla
                            data.append([i, fxi])
                            # incrementamos las interaciones en h
                            i += h

                        # A la suma de la funcion evaluada en los puntos medios de los subintervalos le restamos la funcion evaluada en los subintervalos
                        fxmi = plus - sigm

                        # imprimimos nuestra tabla
                        print(tabulate(data, headers=["Xi", "f(xi)"], showindex=True, tablefmt="pretty"))

                        # A la sumatoria de todas la evaluacion de las funciones le restamos el valor evaluado en los extremos del intervalo
                        sumat = sigm - (A + B)
                        # calculamos el valor de la regla del trapcio compuesto
                        S13C = float((b - a) * ((A + (3 * fxmi) + (2 * sumat) + B) / (8 * n)))
                        # Devolvemos el resultado al usuario
                        print("\x1b[1;35m", "El valor aproximado de la integral por la regla del Trapecio Compuesto",
                              S13C,
                              "\x1b[0;30m")
                    else:
                        #si a es mayor o igual a b mandamos al usuario el mensaje
                        print("\x1b[1;31m" + "¡Ingrese un intervalo valido!" + "\x1b[0;30m")

                else:
                    break
                opcion = int(input("\x1b[3;31m" + "Ingrese el numero de la regla para aproximar el valor de la integral\n""1.Trapecio Simple\n2.Trapecio compuesto\n3.Simpson 1/3 simple\n4.Simpson 1/3 compuesto\n5.Simpson 3/8 simple\n6.Simpson 3/8 compuesto\nOtro numero para salir " + "\x1b[0;30m"))

       #Integracion por rosemberg
        elif opc==2:
            def print_row(lst):
                print(' '.join('%11.20f' % x for x in lst))

            def romberg(f, a, b, eps=1E-8):

                R = [[0.5 * (b - a) * (f(a) + f(b))]]
                print_row(R[0])
                n = 1
                while True:
                    h = float(b - a) / 2 ** n
                    R.append((n + 1) * [None])  # Agrega línea vacía
                    R[n][0] = 0.5 * R[n - 1][0] + h * sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (n - 1) + 1))  # para límites apropiados
                    for m in range(1, n + 1):
                        R[n][m] = R[n][m - 1] + (R[n][m - 1] - R[n - 1][m - 1]) / (4 ** m - 1)
                    print_row(R[n])
                    if abs(R[n][n - 1] - R[n][n]) < eps:
                        x = sympy.Symbol("x")
                        return print(
                            f"La integral de {f(x)} desde {a} hasta {b} es {R[n][n]} con un error relativo de {float(abs(R[n][n - 1] - R[n][n]))}")
                    n += 1

            print(romberg(lambda t: e ** t, 0, 1))
            break

        else:
            break
        opc = int(input("Ingrese el numero de la opcion deseada\n1.Reglas de integracion numerica \n2.Integracion por Rosemberg\nOtro numero para salir\n "))