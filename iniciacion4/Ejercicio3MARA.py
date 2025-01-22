# -*- coding: utf-8 -*-
"""Crea una clase llamada Vehiculo con un atributo de clase llamado cantidad_total. 
Este atributo debe llevar la cuenta de cuántos vehículos han sido creados. 
Además, haz que la clase tenga tres atributos."""

class Vehiculo():

    def __init__(self):
        self.cantidad_total =0
        self.color=input("Inserte un color de coche: ")
        self.marca=input("Inserte una marca de coche: ")
        self.deposito=input("Inserte un deposito de coche: ")

    def contadorVehiculos(self):
        if self.color =="":
            print("Debes introducir un color")
        elif self.marca =="":
            print("Debes introducir una marca")
        elif  self.deposito !="Gasolina":
            print("Ese deposito no esta en nuestro sistema")
        else:
            self.cantidad_total +=1
            print("Se ha creado un coche de color: "+str(self.color)+" con la marca: "
                  +str(self.marca)+(" de deposito: "+str(self.deposito)
                  +" . Cantidad de coches actuales creados: "+str(self.cantidad_total)))

coche=Vehiculo()

print("1.Añadir coche al concesionario")
print("2.Salir")
while True:
    
    opcion=input("Elige una opcion: ")

    if opcion=="1":
        coche.contadorVehiculos()
    elif opcion=="2":
        break
            