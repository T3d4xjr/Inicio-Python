# -*- coding: utf-8 -*-
"""Escribe un programa que lea dos archivos json y combine ambos archivos en un único diccionario 
y se guarde en un nuevo archivo json."""
import json

with open("archivos2/Ejercicio3.json","r") as fichero1:
    cadena1=json.load(fichero1)
fichero1.close()
with open("archivos2/Ejercicio4.json","r") as fichero2:
    cadena2=json.load(fichero2)
fichero2.close()
with open("archivos2/Ejercicio5.json","w") as fichero3:
    json.dump([cadena1,cadena2],fichero3)

fichero3.close()