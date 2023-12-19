print("Programa de ordenamiento para 2, 3 o 4 números")
programa= int(input("Escribe de cuantos números deseas usar el programa: "))

if programa==2:
    num1= int(input("Ingrese número 1: "))
    num2= int(input("Ingrese número 2: "))
    if num1<num2:
        print ("Orden: ", num1, ", ", num2)
    elif num2<num1:
        print ("Orden: ", num2, ", ", num1)
    else:
        print ("Los 2 números son iguales")

elif programa==3:
    num1= int(input("Ingrese número 1: "))
    num2= int(input("Ingrese número 2: "))
    num3= int(input("Ingrese número 3: "))
    if num1<num2<num3:
        print ("Orden: ", num1, ", ", num2, ", ", num3)
    elif num1<num3<num2:
        print ("Orden: ", num1, ", ", num3, ", ", num2)
    elif num2<num1<num3:
        print ("Orden: ", num2, ", ", num1, ", ", num3)
    elif num2<num3<num1:
        print ("Orden: ", num2, ", ", num3, ", ", num1)
    elif num3<num1<num2:
        print ("Orden: ", num3, ", ", num1, ", ", num2)
    elif num3<num2<num1:
        print ("Orden: ", num3, ", ", num2, ", ", num1)
    else:
        print ("Los 3 números son iguales")

elif programa==4:
    num1= int(input("Ingrese número 1: "))
    num2= int(input("Ingrese número 2: "))
    num3= int(input("Ingrese número 3: "))
    num4= int(input("Ingrese número 4: "))
    if num1<num2<num3<num4:
        print ("Orden: ", num1, ", ", num2, ", ", num3, ", ", num4)
    elif num1<num3<num2<num4:
        print ("Orden: ", num1, ", ", num3, ", ", num2, ", ", num4)
    elif num1<num4<num2<num3:
        print ("Orden: ", num1, ", ", num4, ", ", num2, ", ", num3)
    elif num1<num4<num3<num2:
        print ("Orden: ", num1, ", ", num4, ", ", num3, ", ", num2)

    elif num2<num1<num3<num4:
        print ("Orden: ", num2, ", ", num1, ", ", num3, ", ", num4)   
    elif num2<num3<num1<num4:
        print ("Orden: ", num2, ", ", num3, ", ", num1, ", ", num4)
    elif num2<num4<num1<num3:
        print ("Orden: ", num2, ", ", num4, ", ", num1, ", ", num3)   
    elif num2<num4<num3<num1:
        print ("Orden: ", num2, ", ", num4, ", ", num3, ", ", num1)

    elif num3<num1<num2<num4:
        print ("Orden: ", num3, ", ", num1, ", ", num2, ", ", num4)
    elif num3<num2<num1<num4:
        print ("Orden: ", num3, ", ", num2, ", ", num1, ", ", num4)
    elif num3<num4<num2<num1:
        print ("Orden: ", num3, ", ", num4, ", ", num2, ", ", num1)
    elif num3<num4<num1<num2:
        print ("Orden: ", num3, ", ", num4, ", ", num1, ", ", num2)
        
    elif num4<num1<num2<num3:
        print ("Orden: ", num4, ", ", num1, ", ", num2, ", ", num3)
    elif num4<num2<num1<num3:
        print ("Orden: ", num4, ", ", num2, ", ", num1, ", ", num3)
    elif num4<num3<num2<num1:
        print ("Orden: ", num4, ", ", num3, ", ", num2, ", ", num1)
    elif num4<num3<num1<num2:
        print ("Orden: ", num4, ", ", num3, ", ", num1, ", ", num2)

    else:
        print ("Los 4 números son iguales")

else:
    print ("Solo están disponibles los programas de 2,3 y 4 números")