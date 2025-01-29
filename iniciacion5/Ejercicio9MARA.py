# -*- coding: utf-8 -*-
"""Escribe un programa que lea un archivo llamado “log.txt” y detecte las líneas duplicadas, 
escribiendo las únicas en un nuevo archivo llamado “limpio.txt.”"""
#Abrir archivo
with open("archivos/log.txt", "r") as archivo:
    lineas = archivo.readlines()

lineasUnicas = []
#recorrer lineas archivo y guardar las no repetidas
for linea in lineas:
    if linea not in lineasUnicas:
        lineasUnicas.append(linea)

with open("archivos/limpio.txt", "w") as archivoLimpio:
    archivoLimpio.writelines(lineasUnicas)

print("Archivo creado sin lineas duplicadas")