# -*- coding: utf-8 -*-
"""
Crea una clase llamada Persona que tenga los atributos nombre, edad y altura. 
Además implementa los dos siguientes métodos: 
Método saludar: imprime un mensaje con el nombre de la persona y su edad
Método información: imprime un mensaje con la información de la altura de la persona."""
# Definición de la clase Persona
class Persona:

    def __init__(self, nombre, edad, altura):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura

    # Método para saludar
    def saludar(self):
        print("Mi nombre es " + str(self.nombre) + " y tengo " + str(self.edad) + " años")

    # Método para mostrar la altura
    def informacion(self):
        print("Mi altura es " + str(self.altura) + "cm")

# Creación de una instancia y llamadas a métodos
persona1 = Persona("Pepe", 18, 1.77)
persona1.saludar()
persona1.informacion()
