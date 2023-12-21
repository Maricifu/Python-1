#programa ADN

def calcular_porcentaje_parentesco(muestra, cromosoma):
    coincidencias = sum(muestra[i] == cromosoma[i] for i in range(len(muestra)))
    porcentaje = (coincidencias / len(muestra_usuario)) * 100
    return porcentaje


def buscar_sospechoso(muestra, nombres, cromosomas):
    mejor_porcentaje = 0
    sospechoso = ""

    for i in range(len(nombres)):
        nombre = nombres[i]
        cromosoma = cromosomas[i]
        porcentaje = calcular_porcentaje_parentesco(muestra_usuario, cromosoma)

        if porcentaje > mejor_porcentaje:
            mejor_porcentaje = porcentaje
            sospechoso = nombre

    return sospechoso, mejor_porcentaje

nombres = ["Pedro", "Juan", "Diego"]
cromosomas = ["00000101010101010101", "00101010101101110111", "00100010010000001001"]

muestra_usuario = input("Ingrese la secuencia encontrada en la escena del crimen (20 caracteres): ")
sospechoso, porcentaje_parentesco = buscar_sospechoso(muestra_usuario, nombres, cromosomas)

print(f"\nSospechoso: {sospechoso}")
print(f"Porcentaje de parentesco: {porcentaje_parentesco}%")

