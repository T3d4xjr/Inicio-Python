# -*- coding: utf-8 -*-
"""Escribe un programa que convierta una cadena de json en un diccionario. 
Una vez que se haya hecho la conversión, deberá modificar uno de los valores 
(el que cada uno considere) y volver a convertir el diccionario en un json."""
import json

#Abrimos un archivo y hacemos que mediante clave modifiquemos y escribamos en un nuevo fichero
with open("archivos2/Ejercicio3.json","r") as fichero:

    cadena=json.load(fichero)
    print(cadena)

    valorModificado=input("Dime la ciudad a cambiar: ")

    cadena["ciudad"]=valorModificado
    print(cadena)
fichero.close()
with open("archivos2/Ejercicio4.json","w") as fichero:
    json.dump(cadena,fichero)
fichero.close()