# -*- coding: utf-8 -*- 
"""
Realizar un programa que simule el juego de las tres en raya. Se deben cumpli las siguientes condiciones:
Cada jugador solo debe colocar su ficha una vez por turno y no debe ser sobre una casilla ya ocupada. 
En caso de que el jugador haga trampa el ganador será el otro. 
Para ganar se debe conseguir realizar una línea recta (horizontal, vertical o diagonal) con la misma ficha. 
El tablero es de 3x3 y cualquier casilla podrá estar vacía u ocupada sólo por una ficha X o 0.
El programa debe realizar las siguientes operaciones:
Mostrar el tablero por pantalla.
Poner una ficha en una cuadrícula comprobando que no está ocupada.
Comprobar si se produce tres en raya e indicar si es de X o de O, o si hay empate.

Se debe realizar sin necesidad de ninguna librería aparte.
"""
tablero = []
print("Vamos a jugar al tres en raya. \n")

#Crear el tablero par jugar
for i in range(3):
    row = []
    for j in range(3):
        row.append("-")
    tablero.append(row)
#Mostrar tablero
def mostrar_tablero():
    for fila in tablero:
        print(fila)
mostrar_tablero()
#Menu donde iteramos los jugadores y sus acciones para saber si hacen trampa o ganaron o quedaron empatados
while True:
        try:
            filajugador1 = int(input("Ingrese la fila jugador 1 (0, 1, 2): "))
            columnajugador1 = int(input("Ingrese la columna jugador 1 (0, 1, 2): "))

            if filajugador1 < 0 or filajugador1 > 2 or columnajugador1 < 0 or columnajugador1 > 2:
                print("Buen intento pero te saliste del tablero gana el jugador 2")
                break
            elif tablero[filajugador1][columnajugador1] != "-":
                print("La casilla ya está ocupada.Buen intento gana el jugador 2.")
                break
            else:
                tablero[filajugador1][columnajugador1] = "X"
                
            mostrar_tablero()                
            filajugador2 = int(input("Ingrese la fila jugador 2 (0, 1, 2): "))
            columnajugador2 = int(input("Ingrese la columna jugador 2 (0, 1, 2): "))

            if filajugador2 < 0 or filajugador2 > 2 or columnajugador2 < 0 or columnajugador2 > 2:
                print("Buen intento pero te saliste del tablero gana el jugador 1")
                break
            elif tablero[filajugador2][columnajugador2] != "-":
                print("La casilla ya está ocupada.Buen intento gana el jugador 1.")
                break
            else:
                tablero[filajugador2][columnajugador2] = "O"
            mostrar_tablero()    

            if (tablero[0][0] == tablero[1][1] == tablero[2][2] == "X" or 
                tablero[0][2] == tablero[1][1] == tablero[2][0] == "X" or 
                tablero[0][0] == tablero[0][1] == tablero[0][2] == "X" or 
                tablero[1][0] == tablero[1][1] == tablero[1][2] == "X" or 
                tablero[2][0] == tablero[2][1] == tablero[2][2] == "X" or 
                tablero[0][0] == tablero[1][0] == tablero[2][0] == "X" or 
                tablero[0][1] == tablero[1][1] == tablero[2][1] == "X" or 
                tablero[0][2] == tablero[1][2] == tablero[2][2] == "X"):
                print("Jugadsor 1 ha ganado")
                break
            elif (tablero[0][0] == tablero[1][1] == tablero[2][2] == "O" or 
                tablero[0][2] == tablero[1][1] == tablero[2][0] == "O" or 
                tablero[0][0] == tablero[0][1] == tablero[0][2] == "O" or 
                tablero[1][0] == tablero[1][1] == tablero[1][2] == "O" or 
                tablero[2][0] == tablero[2][1] == tablero[2][2] == "O" or 
                tablero[0][0] == tablero[1][0] == tablero[2][0] == "O" or 
                tablero[0][1] == tablero[1][1] == tablero[2][1] == "O" or 
                tablero[0][2] == tablero[1][2] == tablero[2][2] == "O"):
                print("Jugador 2 ha ganado")
                break
            if all(celda != "-" for fila in tablero for celda in fila):
                print("¡Empate!")
                break        
        except ValueError:
            print("¡Error! Por favor, ingrese un número válido para fila y columna.")  
            

