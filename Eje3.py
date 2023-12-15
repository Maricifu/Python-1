def calcular_promedio(notas):
    return sum(notas) / len(notas)

def main():
    # Pedir al usuario que ingrese las notas
    notas = [] #lista vacia
    for i in range(4):
        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    # Calcular el promedio
    promedio = calcular_promedio(notas)

    # Mostrar el resultado
    print(f"El promedio de las notas es: {promedio}")

if __name__ == "__main__":
    main()
