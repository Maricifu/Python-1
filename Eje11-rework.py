cant= int(input("¿Cuantos números deseas ingresar?: "))

numeros= []
numeros2= []

for i in range (cant):
    n=int(input("Ingresa los números: "))
    numeros.append(n)

    for j in range (len(numeros)+1):
        if numeros[j:]>numeros[:j+1]:
            numeros2.append(numeros[j:])


print (numeros2)
