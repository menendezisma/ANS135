import sympy

def Diferenciacion():
    x = sympy.symbols("x")
    print("..:Bienvenido:..")
    print("..Derivacion numerica..")
    opc = int(input("Ingrese el numero de la opcion deseada\n1.Diferencia finita \n2.Extrapolacion de Richardson\nOtro numero para salir "))

    while opc > 0 and opc < 3:
        if opc == 1:
            opc2 = int(input(
                "que metodo desea realizar\n1.Diferencia finita hacia adelante \n2.Diferencia finita hacia atras \n3.diferencia finita centrada"
                "\n4.Formula de los tres puntos \n5.Formula de los cinco puntos\n6.Cualquier numero para Salir "))
            while opc2 > 0 and opc2 < 6:
                if opc2 == 1:

                    fx = (input("Digite la funcion algebraica en terminos de x: "))
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
                    fx = (input("Digite la funcion algebraica en terminos de x: "))
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
                    fx = (input("Digite la funcion algebraica en terminos de x: "))
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
                    fx = (input("Digite la funcion algebraica en terminos de x: "))
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
                    fx = (input("Digite la funcion algebraica en terminos de x: "))
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
                else:
                    break
