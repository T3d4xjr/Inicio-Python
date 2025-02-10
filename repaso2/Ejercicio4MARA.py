# -*- coding: utf-8 -*- 
"""Crea un programa que simule un pequeño ecosistema con animales y plantas. Para ello:
Usa una clase “SerVivo” con atributos como nombre y energía. 
Crea las clases “Animal” y “Planta”, donde:
Los animales pueden moverse y gastar energía.
Los animales pueden comer para ganar energía
Las plantas pueden crecer con el tiempo.
Las plantas ganan energía haciendo la fotosíntesis en el tiempo.
Simula la interacción entre ellos en un ciclo de tiempo, por ejemplo, 6 días. Esto lo puedes implementar en una función que sea la simulación del ciclo.
Cada uno puede definir los porcentajes de crecimiento, energía, movimiento, etc, como quiera.
Se irá mostrando por pantalla, día por día, los valores de los animales y las plantas definidas.
"""
import random

#Clase serVivo
class SerVivo:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia
    
    def __str__(self):
        return self.nombre + ": Energia = " + str(self.energia)
#Clase Planta y sus funciones
class Planta(SerVivo):
    def crecer(self):
        crecimiento = random.randint(2, 5)
        self.energia += crecimiento
        print(self.nombre + " ha crecido y ganado " + str(crecimiento) + " de energía.")
    
    def fotosintesis(self):
        ganancia = random.randint(3, 7)
        self.energia += ganancia
        print(self.nombre + " ha realizado fotosíntesis y ganado " + str(ganancia) + " de energía.")
#Clase Animal y sus funciones
class Animal(SerVivo):
    def moverse(self):
        gasto = random.randint(5, 10)
        self.energia -= gasto
        print(self.nombre + " se ha movido y perdido " + str(gasto) + " de energía.")
    
    def comer(self, planta):
        if planta.energia > 0:
            alimento = min(random.randint(5, 15), planta.energia)
            planta.energia -= alimento
            self.energia += alimento
            print(self.nombre + " ha comido de " + planta.nombre + " y ganado " + str(alimento) + " de energía.")
        else:
            print(self.nombre + " no tiene suficiente energía para ser comida.")
#Simulacion de los seis dias del crecimiento de los animales y su energia
def simulacionEcosistema(dias):
    plantas = [Planta("Árbol", 20), Planta("Arbusto", 15)]
    animales = [Animal("Conejo", 30), Animal("Ciervo", 40)]
    
    for dia in range(1, dias + 1):
        print("Dia: " + str(dia))
        for planta in plantas:
            planta.fotosintesis()
            planta.crecer()
        for animal in animales:
            animal.moverse()
            animal.comer(random.choice(plantas))
        print("\nEstado del ecosistema:")
        for planta in plantas:
            print(planta)
        for animal in animales:
            print(animal)
            
simulacionEcosistema(6)