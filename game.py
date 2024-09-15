import numpy as np
import os
from time import sleep
from random import randint
import keyboard
import msvcrt

maain = True #Estados del juego
game = False
win = False
over = False

stdsize1 = 8 #configuración predeterminada
stdsize2 = 15
puntos = 40
puntaje = 0


def clear_input_buffer(): 
    while msvcrt.kbhit():
        msvcrt.getch()  

def casillaOcupada(mapa, size1, size2, posOcupadas):
    while True:
        pos1 = randint(0, size1-1)
        pos2 = randint(0, size2-1)
        if (pos1, pos2) not in posOcupadas:
            posOcupadas.add((pos1, pos2))
            return pos1, pos2
#               4     11    ->   al crear el mapa con estos valores ocurre un error
def crearMapa(size1, size2):
    map = np.full((size1,size2)," ")
    posOcupadas = set()

    for i in range(0,round((size1*size2)*0.2)):
        pos1, pos2 = casillaOcupada(map, size1, size2, posOcupadas)
        map[pos1][pos2] = "X"
    for i in range(0,puntos):
        pos1, pos2 = casillaOcupada(map, size1, size2, posOcupadas)
        map[pos1][pos2] = "O"
    playerPos1, playerPos2 = casillaOcupada(map, size1, size2, posOcupadas) #posición al azar del jugador
    map[playerPos1][playerPos2] = "▶" #El jugador

    return map, playerPos1, playerPos2

def winn(mapa, size1, size2): #Función que determina si el jugador gano
    for i in range(0,size1-1):
        for j in range(0,size2-1):
            if mapa[i][j] == "O":
                return False
    return True

while maain: #bucle principal
    while True:
        clear_input_buffer()
        print("---Snake game---")
        print("1. Jugar\n2. Ajustes\n3.salir", end="\n")
        opt = input(":")
        try:
            opt = int(opt)
            break
        except ValueError:
            print("Las opciones solo son números!")
            sleep(1)
            os.system('cls')
    os.system('cls')

    if opt == 1:
        map, pos1, pos2 = crearMapa(stdsize1,stdsize2)
        puntaje = 0
        game = True
        while game:
            print(map, end="")
            print("puntos:",puntaje)

            if keyboard.is_pressed('w'): #control de movimientos del jugador
                if pos1==0:
                    map[pos1][pos2] = "▲"
                else:
                    if map[pos1-1][pos2] == "O":    
                        puntaje = puntaje + 1
                        map[pos1-1][pos2] = "▲"
                        map[pos1][pos2] = " "
                        pos1 = pos1-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1-1][pos2] == "X":  
                        game = False
                        over = True
                    else:                           
                        map[pos1-1][pos2] = "▲"
                        map[pos1][pos2] = " "
                        pos1 = pos1-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True

            elif keyboard.is_pressed('s'):
                if pos1+1==stdsize1:
                    map[pos1][pos2] = "▼"
                else:
                    if map[pos1+1][pos2] == "O":
                        puntaje = puntaje +1
                        map[pos1+1][pos2] = "▼"
                        map[pos1][pos2] = " "
                        pos1 = pos1+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1+1][pos2] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1+1][pos2] = "▼"
                        map[pos1][pos2] = " "
                        pos1 = pos1+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True

            elif keyboard.is_pressed('a'):
                if pos2 == 0:
                    map[pos1][pos2] = "◀"
                else:
                    if map[pos1][pos2-1] == "O":
                        puntaje = puntaje + 1
                        map[pos1][pos2-1] = "◀"
                        map[pos1][pos2] = " "
                        pos2 = pos2-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1][pos2-1] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1][pos2-1] = "◀"
                        map[pos1][pos2] = " "
                        pos2 = pos2-1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                        
            elif keyboard.is_pressed('d'):
                if pos2+1 == stdsize2:
                    map[pos1][pos2] = "▶"
                else:
                    if map[pos1][pos2+1] == "O":
                        puntaje = puntaje + 1
                        map[pos1][pos2+1] = "▶"
                        map[pos1][pos2] = " "
                        pos2 = pos2+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
                    elif map[pos1][pos2+1] == "X":
                        game = False
                        over = True
                    else:
                        map[pos1][pos2+1] = "▶"
                        map[pos1][pos2] = " "
                        pos2 = pos2+1
                        if winn(map, stdsize1, stdsize2):
                            game = False
                            win = True
            sleep(0.1)
            os.system('cls')
            
            while win:
                print("Ganaste!!! XD")
                sleep(2)
                os.system('cls')
                win = False

            while over:
                print("Perdiste!!! XD")
                puntaje = 0
                sleep(2)
                os.system('cls')
                over = False

    elif opt == 2:
        while True:
            while True:
                print("Acá podras ajustar el tamaño del mapa")
                print("y la cantidad de puntos en el mapa")
                print("1. tamaño del mapa\n2. cantidad de puntos")
                ans = input(":")
                try:
                    ans = int(ans)
                    break
                except ValueError:
                    print("Las opciones solo son números!")
                    sleep(1)
                    os.system('cls')

            if ans == 1:
                while True:
                    print("Digita el alto del mapa, menor a 8 y mayor a 4")
                    print("valores actuales:", stdsize1, stdsize2)
                    stdsize1 = input(":")
                    try:
                        stdsize1 = int(stdsize1)
                        if stdsize1 <= 8 and stdsize1 > 4:
                            break
                        else:
                            print("Digite un numero menor o igual a 8 y mayor que 4")
                            sleep(1)
                            os.system('cls')
                    except ValueError:
                        print("Digite un numero")
                        sleep(1)
                        os.system('cls')
                while True:
                    print("Digita al ancho del mapa, menor a 15 y mayor a 11")
                    stdsize2 = input(":")
                    try:
                        stdsize2 = int(stdsize2)
                        if stdsize2 <= 15 and stdsize2 > 11:
                            break
                        else:
                            print("Digite un numero menor o igual a 15 y mayor a 11")
                            sleep(1)
                            os.system('cls')
                    except ValueError:
                        print("Digite un numero")
                        sleep(1)
                        os.system('cls')
                print("Cambios realizados!")
                print("valores actuales:", stdsize1, stdsize2)
                sleep(1)
                os.system('cls')
                break    
            elif ans == 2:
                while True:
                    print("Digita la cantidad de puntos")
                    puntos = int(input(":"))
                    if puntos >= stdsize1*stdsize2:
                        print("Cantidad de puntos no valida! debe ser menor a: ", stdsize1*stdsize2)
                        sleep(2)
                        os.system('cls')
                    else:
                        print("cantidad de puntos fijada en", puntos)
                        print("Cambio exitoso")
                        sleep(2)
                        os.system('cls')
                        break
                break
            else:
                print("Opción no valida, :(")
                sleep(1)
                os.system('cls')
    elif opt == 3:
        print("Terminando ejecución")
        break
    else:
        print("Opción no valida, :(")
        sleep(1)
        os.system('cls')