# -*- coding: utf-8 -*-
"""Escribe un programa que coja dos archivos de texto (“archivo1.txt” y “archivo2.txt”) 
y los combine en un nuevo archivo llamado “combinado.txt”, alternando las líneas de ambos archivos."""

#Abrir archivos
archivo1 = open("archivos/archivo1.txt", "r")
archivo2 = open("archivos/archivo2.txt", "r")
lineasArchivo1 = archivo1.readlines()
lineasArchivo2 = archivo2.readlines()

archivo1.close()
archivo2.close()

archivoCombinado = open("archivos/combinado.txt", "w")
#Pillar la longitud maxima
longitudMaximaArchivos = max(len(lineasArchivo1), len(lineasArchivo2))
#Recorrer alternando
for i in range(longitudMaximaArchivos):
    if i < len(lineasArchivo1):
        archivoCombinado.write(lineasArchivo1[i])
    if i < len(lineasArchivo2):
        archivoCombinado.write(lineasArchivo2[i])
print("Archivos combinados")