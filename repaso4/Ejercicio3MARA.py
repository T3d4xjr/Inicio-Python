# -*- coding: utf-8 -*- 
"""Crea un programa que calcule el daño de un ataque durante una batalla Pokémon.
La fórmula será la siguiente: daño = 50 * (ataque / defensa) * efectividad
Efectividad: x2 (súper efectivo), x1 (neutral), x0.5 (no es muy efectivo)
Sólo hay 4 tipos de Pokémon: 
Agua: x2 contra Fuego, x1 contra Eléctrico y x0.5 contra Planta
Fuego: x2 contra Planta, x1 contra Eléctrico y x0.5 contra Agua
Planta: x2 contra Agua, x1 contra Eléctrico y x0.5 contra Fuego
Eléctrico: x2 contra Agua, x1 contra Fuego y x0.5 contra Planta 
El programa recibe los siguientes parámetros:
Tipo del Pokémon atacante.
Tipo del Pokémon defensor.
Ataque: Entre 1 y 100.
Defensa: Entre 1 y 100.
Se deberán mostrar y pedir los datos por pantalla al usuario. Se deberá mostrar además el daño producido por el pokemon atacante
"""
#Funcion de batalla Pokemon donde nos mostrar todos los datos de la batalla mas el daño hecho al contrincante
efectividad = 0
def batallaPokemon():
    try:
        while(True):
            tipo1=str(input("Introduce el tipo del pokemon atacante: "))
            tipo2=str(input("Introduce el tipo del pokemon defensor: "))
            ataque=int(input("Ataque entre el 1 y el 100: "))
            defensa=int(input("Defensa entre el 1 y el 100: "))

            if tipo1 =="Agua" and tipo2 =="Fuego" or tipo1 =="Fuego" and tipo2 =="Planta" or tipo1 =="Planta" and tipo2 =="Agua" or tipo1 =="Electrico" and tipo2 =="Agua":
                efectividad = 2
            elif tipo1 =="Agua" and tipo2 =="Electrico" or tipo1 =="Fuego" and tipo2 =="Electrico" or tipo1 =="Planta" and tipo2 =="Electrico" or tipo1 =="Electrico" and tipo2 =="Fuego":
                efectividad = 1
            elif tipo1 =="Agua" and tipo2 =="Planta" or tipo1 =="Fuego" and tipo2 =="Agua" or tipo1 =="Planta" and tipo2 =="Fuego" or tipo1 =="Electrico" and tipo2 =="Planta ":
                efectividad = 0.5
            else:
                print("Esos tipos entre ellos todavia no se sabe que daño se haran por favor intentelo de nuevo.")
                continue

            daño =50*(ataque/defensa)*efectividad

            print("Tipo atacante: "+str(tipo1))
            print("Tipo defensor: "+str(tipo2))
            print("Ataque: "+str(ataque))
            print("Defensa: "+str(defensa))
            print("Daño recibido: "+str(daño))

            seguir=input("Quieres hacer otra batalla (s/n)").strip().lower()
            if seguir !="s":
                break
    except ValueError:
        print("Formato invalido.")
batallaPokemon()