# -*- coding: utf-8 -*- 
"""Con una función, tendrás que crear un diccionario 
con información de 5 libros (título, autor, año y precio) y guardarlo en un archivo json.
Otra función deberá leer el archivo json y convertir los 
precios de los libros a otra moneda (por ejemplo, de EUR a USD). 
Tendréis que buscar el valor de la conversión
"""
import json


def guardadoDiccionario():
    libros = [
        {"titulo": "Los tres vientos", "autor": "Picasso", "año": 2001, "precio": 24},
        {"titulo": "Cien años de soledad", "autor": "Gabriel García Márquez", "año": 1967, "precio": 30},
        {"titulo": "El principito", "autor": "Antoine de Saint-Exupéry", "año": 1943, "precio": 18},
        {"titulo": "1984", "autor": "George Orwell", "año": 1949, "precio": 22},
        {"titulo": "Don Quijote", "autor": "Miguel de Cervantes", "año": 1605, "precio": 35}
    ]
    
    with open("archivosRepaso/archivo1.json","w") as fichero:

        json.dump(libros,fichero)

    return libros

def conversion(dolares):

    
    try:

        with open("archivosRepaso/archivo1.json","r") as fichero:
            libros=json.load(fichero)

            for libro in libros:
                euros=libro["precio"]
                libro["dolares"]=euros*dolares

            for libro in libros:

                print(str(libro))


        return libros
    except FileNotFoundError as e:
        print(str(e))

guardadoDiccionario()

conversion(1.12)


