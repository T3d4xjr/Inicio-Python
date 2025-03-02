# -*- coding: utf-8 -*- 
"""
Crea un programa que gestione una biblioteca de juegos de mesa. 
El usuario introducirá los siguientes datos de cada juego: Nombre, Editorial, Mecánica y Dificultad (Número de 0 - 5.0).
Cada vez que el usuario introduzca un juego, se creará un objeto “Juego de mesa” y se almacenará en una lista.
Cuando el usuario haya terminado de añadir juegos de mesa, se le ofrecerá la opción para poder guardar el listado en formato json. Solo se guardará si el usuario lo decide.

"""
import json

#Clase biblioteca que tiene los valores que la contienen y los muestra
class Biblioteca:

    def __init__(self,nombre,editorial,mecanica,dificultad):
       self.nombre=nombre
       self.editorial=editorial
       self.mecanica=mecanica
       self.dificultad=dificultad

    def __str__(self):
        return f"Nombre: {self.nombre},Editorial: {self.editorial},Mecanica: {self.mecanica},Dificultad: {self.dificultad}" 

#Clase juegoMesa donde vamos a tener una lista y añadiremos valores con el formato ya definido en la clase biblioteca.
class JuegoMesa:

    def __init__(self):
        self.Juegos=[]
    
    def añadirJuego(self,nombre,editorial,mecanica,dificultad):
        self.Juegos.append(Biblioteca(nombre,editorial,mecanica,dificultad))
    
    def listarJuego(self):
        for juego in self.Juegos:
            print(juego)
            return juego
        print("Ningun juego se encontro")
        return None
    def guardarJuego(self):
        with open("archivos3/juegos.json","w") as fichero:
            json.dump([juego.__dict__ for juego in self.Juegos],fichero)
        print("Añadidos correctamente")
        exit()
    def salirJuego(self):
        print("Saliendo de los juegos sin guardarlos.")
        exit()

juego =JuegoMesa()

#Menu principal.
while True:
    print("Biblioteca de juegos")
    print("1. Añadir juego")
    print("2. Lista juegos")
    print("3. Terminar de  añadir juegos")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        editorial = input("Editorial: ")
        mecanica = input("Mecanica: ")
        dificultad=input("Dificultad (valores del 0-5.0): ")
        juego.añadirJuego(nombre,editorial,mecanica,dificultad)
    elif opcion == "2":
        juego.listarJuego()
    elif opcion == "3":
        
        print("Elige una opcion.")
        print("1.Guardar juegos en json ")
        print("2.No guardarlos.")

        opcion2 = input("Selecciona una opción: ")
    
        if opcion2 == "1":
            juego.guardarJuego()
        elif opcion2 == "2":
            juego.salirJuego()
        else:
            print("Opcion no valida.")
    else:
        print("Opción no válida, intenta de nuevo.")
    