# -*- coding: utf-8 -*- 
"""Escribe un programa que administre una base de datos de películas. Para ello:
Usa una lista de tuplas con título, año y género.
Convierte la lista en un diccionario donde la clave es el género
 y el valor es una lista de películas de ese género.
Guarda el diccionario en un JSON y permite buscar películas por género.
"""
import json

peliculas = [
    ("El Padrino", 1972, "Crimen"),
    ("Pulp Fiction", 1994, "Crimen"),
    ("El Señor de los Anillos", 2001, "Fantasía"),
    ("Forrest Gump", 1994, "Drama"),
    ("Inception", 2010, "Ciencia Ficción"),
    ("Interstellar", 2014, "Ciencia Ficción"),
    ("Gladiador", 2000, "Acción"),
    ("Titanic", 1997, "Romance")
]
diccionario = {}
for titulo, anio, genero in peliculas:
    if genero not in diccionario:
        diccionario[genero] = []
    diccionario[genero].append({"titulo": titulo, "año": anio})

with open("archivosRepaso/peliculas.json", "w") as archivo:
    json.dump(diccionario, archivo)
def buscarGenero(genero):
    try:
        with open("archivosRepaso/peliculas.json", "r",) as archivo_json:
            data = json.load(archivo_json)
            
        if genero in data:
            for pelicula in data[genero]:
                print("La pelicula es: "+str(pelicula['titulo'])+" y el año: "+str(pelicula['año']))
        else:
            print("No se encontraron películas en el género.")
    except FileNotFoundError:
        print("Error: No se encontró el archivo de películas.")

genero = input("Ingresa un género para buscar: ")
buscarGenero(genero)