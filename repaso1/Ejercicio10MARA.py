# -*- coding: utf-8 -*- 
"""Escribe un programa que registre temperaturas diarias en 
un diccionario con la fecha como clave y la temperatura como valor. 
Además, tiene que tener las siguientes características:
Tiene que permitir al usuario ingresar nuevos registros.
Los datos deberán ser guardados en un archivo JSON.
Agrega una función que lea el JSON y muestre el promedio de temperaturas de la última semana.
Habría que gestionar que el usuario metiera valores no válidos.
"""
import json
def registrarTemperatura():
    try:
        diccionario={}
        fecha=input("Indique la fecha: ")
        temperatura=float(input("Indique la temperatura: "))
        
        diccionario[fecha]=temperatura
        with open("archivosRepaso/temperaturas.json", "w") as fichero:
            json.dump(diccionario, fichero)
    except ValueError:
            print("Ingresa los datos bien")
def calcularTemperatura():
    try:
        with open("archivosRepaso/temperaturas.json") as fichero:
            temperaturas = json.load(fichero)
            temperaturasUltimaSemana = list(temperaturas.values())[-7:]
            promedio = sum(temperaturasUltimaSemana) / len(temperaturasUltimaSemana)
            print("El promedio de la última semana es: " + str(promedio))
    except FileNotFoundError:
        print("No se puede leer el archivo")
while True:
    print("1.Registrar temperatura")
    print("2.Calcular temperatura ultima semana")
    print("3.Salir")
    opcion=input("Elige una opcion: ")
    if opcion=="1":
        registrarTemperatura()
    elif opcion=="2":
        calcularTemperatura()
    elif opcion=="3":
        print("Saliendo....")
        break
    else:
        print("Opcion no valida")