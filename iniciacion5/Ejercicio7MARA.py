# -*- coding: utf-8 -*-
"""Crea un programa que lea un archivo de texto grande (“grande.txt”) y lo divida en varios archivos más pequeños, 
cada uno con un número específico de líneas (por ejemplo, 100 líneas por archivo)."""
#Las lineas maximas de cada archivo
lineaArchivo=15
#Abrir archivo
with open("archivos/grande.txt","r") as archivo:
    lista=archivo.readlines()

    lineasArchivo=len(lista)
    #Recorrear cada linea y escribir en los nuevos archivos hasta el limite puesto
    for i in range(0,lineasArchivo,lineaArchivo):

        archivosNuevos=open("archivos/grande_" + str(i) + ".txt", "w")

        archivosNuevos.writelines(lista[i:i+lineaArchivo])

archivo.close()
archivosNuevos.close()