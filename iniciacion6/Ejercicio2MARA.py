# -*- coding: utf-8 -*-
"""Escribe un programa que contenga un diccionario en Python y guardalo como un archivo “productos.json”. 
Haz que el diccionario sea de productos. (Asígnale tu los valores que consideres)
"""
import json
# Creanos un diccionario
productos={
    "nombre": "Manzana",
    "precio": 2,
    "color": "rojo"
}
#Y lo escribimos
with open("archivos2/productos.json","w") as fichero:
    json.dump(productos,fichero)