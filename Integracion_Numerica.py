#importamos las librerias a utilizar
import sympy
from tabulate import tabulate

#Definimos la funcion U4
def Integracion():
    #Desplegamos un menu
    opcion = int(input("\x1b[1;31m"+"Ingrese el numero de la regla para aproximar el valor de la integral\n"
        "1.Trapecio Simple\n2.Trapecio compuesto\n3.Simpson 1/3 simple\n4.Simpson 1/3 compuesto\n5.Simpson 3/8 simple\n6.Simpson 3/8 compuesto\nOtro numero para salir "+"\x1b[0;30m"))

    while opcion > 0 and opcion < 7:
        #Trapecio simple
        if opcion==1:
            #Definimos nuestra variable independiente
            x=sympy.symbols('x')
            #Solicitamos al usuario que ingrese la funcion
            Fx = input("Ingrese la funcion en terminos de x ")
            #Pedimos el extremo inferior del intervalo
            a=int(input("Ingrese el valor de a "))
            #evaluamos el intervalo inferior en la funcion
            A=sympy.sympify(Fx).subs(x,a)
            # Pedimos el extremo superior del intervalo
            b=int(input("Ingrese el valor de b "))
            # evaluamos el intervalo superior en la funcion
            B = sympy.sympify(Fx).subs(x, b)

            #Calculamos el valor aproximado por la regla de trapecio simple
            TS=float((b-a)*((A+B)/2))
            #Devolvemos el resultado al usuario
            print("\x1b[1;36m","El valor Aproximado de la integral por la regla del Trapecio Simple es ",TS ,"\x1b[0;30m")

        #Trapecio Compuesto
        elif opcion==2:
            #Solicitamos el valor de los subintervalos
            n = int(input("Ingrese el valor de n "))
            #definimos la variable independiente
            x = sympy.symbols('x')
            #Pedimos al usuario la funcion
            Fx = input("Ingrese la funcion en terminos de x ")
            #Solicitamos el valor inferior del intervalo
            a = int(input("Ingrese el valor de a "))
            #Evaluamos el intervalo inferior en la funcion
            A = sympy.sympify(Fx).subs(x, a)
            # Solicitamos el valor superior del intervalo
            b = int(input("Ingrese el valor de b "))
            # Evaluamos el intervalo superior en la funcion
            B = sympy.sympify(Fx).subs(x, b)

            #Calculamos en valor de la separacion entre cada subintervalo
            h = (b - a) / n

            #creamos una lista vacia
            data=[]
            #Creamos la variable sigma que almacenara la sumatoria de todas las funciones evaluadas en x
            sigma = 0
            #definimos que el incremento empiece desde el intervalo inferior
            i=a
            #creamos un bucle para ir evaluando cada subintervalo en la funcion
            while i<=b:
                #evaluamos los subintervalos en la funcion
                fxi=sympy.sympify(Fx).subs(x,i)
                #Vamos sumando los valores de la evaluacion
                Sigma=fxi=sympy.sympify(Fx).subs(x,i)
                #Pasamos los datos a nuesta tabla
                data.append([i,fxi])
                #Ocupamos una variable auxiliar para ocupar los datos despues
                sigma+=Sigma
                #incrementamos las interaciones en h
                i += h
            #imprimimos nuestra tabla
            print(tabulate(data,headers=["Xi","f(xi)"],showindex=True,tablefmt="pretty"))

            #A la sumatoria de todas la evaluacion de las funciones le restamos el valor evaluado en los extremos del intervalo
            sumatoria = sigma - (A + B)
            #calculamos el valor de la regla del trapcio compuesto
            TC = float((b - a) * ((A+(2*sumatoria)+B)/(2*n)))
            #Devolvemos el resultado al usuario
            print("\x1b[1;35m", "El valor aproximado de la integral por la regla del Trapecio Compuesto", TC, "\x1b[0;30m")

        #Simpson 1/3 simple
        elif opcion == 3:
            # Definimos nuestra variable independiente
            x = sympy.symbols('x')
            # Solicitamos al usuario que ingrese la funcion
            Fx = input("Ingrese la funcion en terminos de x ")
            # Pedimos el extremo inferior del intervalo
            a = int(input("Ingrese el valor de a "))
            # evaluamos el intervalo inferior en la funcion
            A = sympy.sympify(Fx).subs(x, a)
            # Pedimos el extremo superior del intervalo
            b = int(input("Ingrese el valor de b "))
            # evaluamos el intervalo superior en la funcion
            B = sympy.sympify(Fx).subs(x, b)
            #Calculamos el punto medio del intervalo
            Xm=(a+b)/2
            #Evaluamos la funcion en el punto medio
            Fxm = sympy.sympify(Fx).subs(x, Xm)

            # Calculamos el valor aproximado por la regla de trapecio simple
            S13S = float((b - a) * ((A +4*Fxm+ B) / 6))
            # Devolvemos el resultado al usuario
            print("\x1b[1;36m", "El valor Aproximado de la integral por la regla de Simpson 1/3 Simple es ", S13S,
                  "\x1b[0;30m")


        #Simpson 1/3 compuesto
        elif opcion == 4:
            print()

        #Simpson 3/8 simple
        elif opcion == 5:

            print()
        #Simpson 3/8 compuesto
        elif opcion == 6:
            print()

        else:
            break

        opcion = int(input("\x1b[1;31m" + "Ingrese el numero del metodo par aproximar el valor de la integral\n"
                    "1.Trapecio Simple\n2.Trapecio compuesto\n3.Simpson 1/3 simple\n4.Simpson 1/3 compuesto\n5.Simpson 3/8 simple\n6.Simpson 3/8 compuesto\nOtro numero para salir " + "\x1b[0;30m"))