#Codigo MRU n MRUA (:()
print("===CODIGO-BOLAÑO===\n")
print("Bienvenido al programa de MRU.")

#Menus
def mostrar_info():
    print("===============")
    print("1. Tiempo")
    print("2. Velocidad")
    print("3. Distancia")
    print("===============")

def mostrar_info2():
    print("===============")
    print("1. Velocidad Final")
    print("2. Aceleración")
    print("3. Tiempo")
    print("4. Distancia")
    print("===============")
def mostrar_blop():
    print("===========")
    print("1. MRU")
    print("2. MRUA")
    print("===========")

#Operaciones MRU
def operaciones():
    pregunta = int(input("Escoja que resultado desea obtener: "))
    if pregunta == 1:
        A = float(input("Ingresa la distancia en M: "))
        B = float(input("Ingresa la velocidad en M/S: "))
        print(f"\nEl resultado es: {(A / B):.2f} Sec")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info()
            operaciones()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    elif pregunta == 2:
        C = float(input("Ingresa la distancia en M: "))
        D = float(input("Ingresa el tiempo Sec: "))
        print(f"\nLa velocidad es: {(C / D):.2f} M/S")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info()
            operaciones()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    elif pregunta == 3:
        E = float(input("Ingresa la velocidad M/S: "))
        F = float(input("Ingresa el tiempo Sec: "))
        print(f"\nLa distancia es:  {(E * F):.2f} M")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info()
            operaciones()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    else:
        print("Valor no valido")

#Operaciones MRUA
def operacionesM():
    bil = int (input("Escoja el resultado que desea obtener: "))
    if bil == 1:
        v1 = float(input("Ingrese la velociadad inicial en m/s: "))
        a = float(input("Ingrese la aceleracion en m/s^2: "))
        t = float(input("Ingrese el tiempo en s: "))
        print(f"\nLa velocidad final es de: {(v1 + a * t):.2f} m/s")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info2()
            operacionesM()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    elif bil == 2:
        v1 = float(input("Ingrese la velociadad inicial en m/s: "))
        v = float(input("Ingrese la velocidad final en m/s: "))
        t = float(input("Ingrese el tiempo en s: "))
        print(f"\nLa aceleracion es de: {((v - v1) / t):.2f} m/s^2")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info2()
            operacionesM()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    elif bil == 3:
        v1 = float(input("Ingrese la velociadad inicial en m/s: "))
        v = float(input("Ingrese la velocidad final en m/s: "))
        a = float(input("Ingrese la aceleracion en m/s^2: "))
        print(f"\nEl tiempo es de: {((v - v1) / a):.2f} s" )
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info2()
            operacionesM()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    elif bil == 4:
        v1 = float(input("Ingrese la velociadad inicial en m/s: "))
        t = float(input("Ingrese el tiempo en s: "))
        a = float(input("Ingrese la aceleracion en m/s^2: "))
        print(f"\nLa velocidad es de: {(v1 * t + (1/2) * a * t**2):.2f} m")
        var = (input("¿Deseas hacer otra opercaión? si/no: ")).lower()
        if var == "si":
            mostrar_info2()
            operacionesM()
        elif var == "no":
            print("Gracias por participar.")
        else:
            print("Valor invalido.")
    else:
        print("Valor no valido")

#Variables e información para MRU
def bola_m():
    print("==============")
    print("Escojiste MRU.")
    print("==============")    
    bola = input("¿Quieres saber que es MRU? si/no: ").lower()
    if bola == "si":
        print("\nEs un tipo de movimiento en el que un objeto se desplaza en línea recta con velocidad constante, es decir, no cambia ni su rapidez ni su dirección, por lo tanto su aceleración es cero. En este programa podras obtener el tiempo, la velocidad y la distancia.\n")
        pelos = input("Quieres pasar a las operaciones? si/no: ").lower()
        if pelos == "si":
            mostrar_info()
            operaciones()
        else:
            print("Gracias por ver.")
    elif bola == "no":
        pelos = input("\nQuieres pasar a las operaciones? si/no: ").lower()
        if pelos == "si":
            mostrar_info()
            operaciones()
        else:
            print("Gracias por ver.")
    else:
        print("Valor invalido.")

#Variables e información para MRUA
def blips():
    print("==============")
    print("Esojiste MRUA.")
    print("==============")
    klown = input("¿Quieres saber que es MRUA? si/no: ").lower()
    if klown == "si":
        print("\nEl MRUA es un movimiento en línea recta donde un objeto cambia su velocidad de manera constante debido a una aceleración fija, es decir, su velocidad aumenta o disminuye uniformemente con el tiempo. dentro de este programa podras obtener velocidad, aceleración, tiempo y distancia.\n")
        pelos = input("\nQuieres pasar a las operaciones? si/no: ").lower()
        if pelos == "si":
            mostrar_info2()
            operacionesM()
        else:
            print("Gracias por ver.")
    elif klown == "no":
        pelos = input("Quieres pasar a las operaciones? si/no: ").lower()
        if pelos == "si":
            mostrar_info2()
            operacionesM()
        else:
            print("Gracias por ver")
    else:
        print("Gracias por ver")

#Menu de selección
mostrar_blop()
blop = input("¿Que metodo deseas utilizar? 1/2 ")
if blop == "1":
    bola_m()
elif blop == "2":
    blips()
else:
    print("Valor invalido, gracias por ver.")
