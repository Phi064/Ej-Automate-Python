import random, sys

#Sistema de Puntuación
victorias = 0
derrotas = 0
empates = 0
ronda = 1

#Variables de los movimientos
mov_player = ''
mov_pc = ''

while True:
    #Elección del usuario
    print("PIEDRA, PAPEL, TIJERA")
    #Añadido un contador de rondas
    print("RONDA " + str(ronda))
    ronda += 1
    print("Elige: (P)iedra, P(A)pel, (T)ijeras o (S)alir")
    mov_player = str(input().lower()) #Me aseguro de que se puedan usar mayúsculas y minúsculas

    while True:
        if mov_player == "s":
            sys.exit()
        if mov_player == "p":
            print("PIEDRA CONTRA...")
            break
        elif mov_player == "a":
            print("PAPEL CONTRA...")
            break
        elif mov_player == "t":
            print("TIJERAS CONTRA...")
            break
        else:
            print("Por favor, introduce un valor válido")
            
    #Elección del PC
    while True:
        random_mov = random.randint(1,3)
        if random_mov == 1:
            mov_pc = 'p'
            print("PIEDRA")
            break
        elif random_mov == 2:
            mov_pc = 'a'
            print("PAPEL")
            break
        elif random_mov == 3:
            mov_pc = 't'
            print("TIJERA")
            break
            
    #Comparación de los movimientos y actualización de las Victorias, Derrotas y Empates
    while True:
        if mov_player == mov_pc:
            print("EMPATE!")
            empates += 1
            break
        elif mov_player == 'p' and mov_pc == 'a':
            print("GANA PAPEL!")
            derrotas += 1
            break
        elif mov_player == 'p' and mov_pc == 't':
            print("GANA PIEDRA!")
            victorias += 1
            break
        elif mov_player == 'a' and mov_pc == 'p':
            print("GANA PAPEL!")
            victorias += 1
            break
        elif mov_player == 't' and mov_pc == 'p':
            print("GANA PIEDRA!")
            derrotas += 1
            break
        elif mov_player == 'a' and mov_pc == 't':
            print("GANA TIJERAS!")
            derrotas += 1
            break
        elif mov_player == 't' and mov_pc == 'a':
            print("GANA TIJERAS!")
            victorias += 1
            break
    print("Victorias: " + str(victorias) + " Derrotas: " + str(derrotas) + " Empates: " + str(empates)) #Resultado Actual
