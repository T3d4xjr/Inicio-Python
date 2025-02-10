# -*- coding: utf-8 -*- 
"""Crea un programa que haga una simulación de una carrera entre tres coches:
Usa una lista de tuplas para representar los coches ((nombre, velocidad)). 
En cada "turno", cada coche avanza una distancia aleatoria basada en su velocidad. Además, se deberá mostrar en cada ronda la distancia de cada coche.
La carrera termina cuando uno de los cachos supera 100 unidades de distancia.
Se debe mostrar quién ganó la carrera.
"""
import random

#Funcion donde tenemos unos coches iniciales con una velocidad random y donde en cada turno vas subiendo hasta llegar a la meta.
def iniciarCarrrera():
    coches = [("Coche 1", random.randint(5, 15)),
              ("Coche 2", random.randint(5, 15)),
              ("Coche 3", random.randint(5, 15))]
    
    posiciones = {coche[0]: 0 for coche in coches}
    turno=0
    while max(posiciones.values()) < 100:
        turno+=1
        print("Estado de la carrera:")
        
        print("Turno: "+str(turno))
        for coche, velocidad in coches:
            avance = random.randint(1, velocidad)
            posiciones[coche] += avance
            
            print("Coche: "+str(coche)+" va a: "+str(posiciones[coche])+" unidades")

        input("Presione Enter para siguiente turno")
        
    
    ganador = max(posiciones, key=posiciones.get)
    print("El ganador es "+str(ganador))

iniciarCarrrera()