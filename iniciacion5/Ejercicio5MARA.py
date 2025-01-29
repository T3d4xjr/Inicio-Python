# -*- coding: utf-8 -*-
"""Escribe un programa que lea un archivo CSV llamado “datos.csv” y muestre cada fila como una lista. 
A continuación, convierte los datos en un diccionario, donde la primera fila del CSV se usa como claves."""

archivo=open("archivos/datos.csv","r")
diccionario = {}

lista=archivo.readlines()
claves = lista[0].split(",")
for clave in claves:
    diccionario[clave] = []


for linea in lista[1:]:
    valores = linea.strip().split(",")
    for i in range(len(claves)):
        diccionario[claves[i]].append(valores[i])
        
print(diccionario)

archivo.close()