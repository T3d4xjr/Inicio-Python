# -*- coding: utf-8 -*-
"""Crea un programa que lea un archivo de texto grande (“grande.txt”) y lo divida en varios archivos más pequeños, 
cada uno con un número específico de líneas (por ejemplo, 100 líneas por archivo)."""

lineaArchivo=15

with open("archivos/grande.txt","r") as archivo:
    lista=archivo.readlines()

    lineasArchivo=len(lista)

    for i in range(0,lineasArchivo,lineaArchivo):

        archivosNuevos=open("archivos/grande_" + str(i) + ".txt", "w")

        archivosNuevos.writelines(lista[i:i+lineaArchivo])

archivo.close()
archivosNuevos.close()