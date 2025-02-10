# -*- coding: utf-8 -*- 
"""Escribe un programa que, a partir de una lista de tuplas 
con información de personas (nombre, edad, altura) realice lo siguiente:
Convierta esta lista en un diccionario donde la clave sea el nombre 
y los valores sean las demás características.
Guarde este diccionario en un archivo JSON.
Además, escribe una función que lea el JSON y muestre la 
información de la persona más alta y la de mayor edad.
"""
import json
personas = [
    ("Ana", 25, 1.68),
    ("Luis", 30, 1.75),
    ("Carlos", 22, 1.80),
    ("Marta", 28, 1.65),
    ("Jorge", 35, 1.70)
]
def conversionDiccionario(personas):
    diccionario = {}
    for nombre, edad, altura in personas:
        diccionario[nombre] = {"edad": edad, "altura": altura}
    with open("archivosRepaso/archivo3.json", "w") as fichero:
        json.dump(diccionario, fichero)

    return diccionario  
def personasAltaMayor(): 
    with open("archivosRepaso/archivo3.json", "r") as fichero:
        datos=json.load(fichero)

        personaAlta = ""
        maxAltura = 0

        personaMayor = ""
        maxEdad = 0

        for nombre,info in datos.items():
            if info["altura"] >maxAltura:
                maxAltura=info["altura"]
                personaAlta=nombre
            if info["edad"] >maxEdad:
                maxEdad=info["edad"]
                personaMayor=nombre
        print("La persona: "+str(personaAlta)+" es la mas alta con : "+str(maxAltura)+" cm")
        print("La persona: "+str(personaMayor)+" es la mas mayor con : "+str(maxEdad)+" años")
diccionario=conversionDiccionario(personas)
personasAltaMayor()