import math

def calcular_perimetro (radio):
    return 2 * math.pi * radio

def calcular_area (radio):
    return math.pi * radio ** 2 

def main (): 
    #Entrada por consola del radio
    radio= float(input("Ingrese el radio: "))

    #calcular perimetro y area 
    perimetro= calcular_perimetro(radio)
    area= calcular_area(radio)

    #salida por consola de los resultados
    print(f"Perimetro: ", perimetro)
    print(f"Area: ", area)

if __name__== "__main__":
    main()
    