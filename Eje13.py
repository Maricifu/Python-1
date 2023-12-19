#Para ganar un set un jugador debe ganar 6 juegos, ademas debe haber ganado dos juegos mas que su rival
#si el juego esta empatado a 5 juegos gana el primero que llegue a 7 
#Si el juego esta empatado a 6 gana el primero que llegue a 7
#Sabiendo que el jugador A ha ganado *m* juegos, y el jugador B, *n* juegos, al periodista le gustaría saber:

# - si A ganó el set, o
# - si B ganó el set, o
# - si el set todavía no termina, o
# - si el resultado es inválido (por ejemplo, 8-6 o 7-3).

def determinar_ganador_set(jugadorA, jugadorB):
    if jugadorA < 6 and jugadorB < 6:
        return "Aún no termina"
    
    if abs(jugadorA - jugadorB) < 2:
        return "Inválido"
    
    if jugadorA >= 6 and jugadorA - jugadorB >= 2:
        return "Ganó A"
    
    if jugadorB >= 6 and jugadorB - jugadorA >= 2:
        return "Ganó B"
    
    if jugadorA == 6 and jugadorB == 6:
        return "Aún no termina"
    
    if jugadorA == 7 and jugadorB == 5:
        return "Ganó A"
    
    if jugadorB == 7 and jugadorA == 5:
        return "Ganó B"
    
    if jugadorA == 7 and jugadorB == 6:
        return "Aún no termina"
    
    if jugadorB == 7 and jugadorA == 6:
        return "Aún no termina"
    
    return "Inválido"

def main():
    print("Programa para determinar ganador de un set de tenis")
    jugadorA = int(input("Juegos ganados por A: "))
    jugadorB = int(input("Juegos ganados por B: "))
    
    resultado = determinar_ganador_set(jugadorA, jugadorB)
    print(resultado)

if __name__ == "__main__":
    main()