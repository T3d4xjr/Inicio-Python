# -*- coding: utf-8 -*-
"""Escribe un programa que lea un archivo json llamado “datos.json”, 
carga los datos en un diccionario e imprima el valor asociado a la clave “nombre”."""
import json
with open("archivos2/datos.json") as fichero:
    menu =json.load(fichero)
    print(menu)
    for elemento in menu:
        print("La clave: "+str(elemento)+" tiene de valor:"+str(menu[elemento]))
        break