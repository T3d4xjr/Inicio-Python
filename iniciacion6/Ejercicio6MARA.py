# -*- coding: utf-8 -*-
"""Escribe un programa que haga la validación de un archivo json. 
Para ello, se deberá intentar cargar el archivo json y si no es válido, 
mostrar un mensaje de error al usuario con el código de la excepción. 
En caso de que el archivo sea válido, también se deberá mostrar por pantalla."""
import json
#Abrimos el archivo dentro de un try cacth y si salta una excepcion saldra el mensaje
try:
    with open("archivos2/eejercicio3.json","r") as fichero:
        datos = json.load(fichero) 
    print("El archivo JSON es válido.")
    print(datos)
except FileNotFoundError as e:
    print("El archivo no es valido"+str(e))