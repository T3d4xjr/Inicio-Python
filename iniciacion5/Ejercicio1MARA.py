# -*- coding: utf-8 -*-
"""Escribe un programa que lea un archivo llamado “datos.txt” e 
imprime su contenido línea por línea y muestra el número total de líneas que tiene el archivo."""

archivo=open('archivos/datos.txt','r')

#Lee el archivo
lineas=archivo.readlines()
numLinea=0

#Recorre cada linea y cuenta e l numero total
for linea in lineas:

    numLinea +=1
    print(linea)
print("Numero total de lineas: "+str(numLinea))
archivo.close()