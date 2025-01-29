# -*- coding: utf-8 -*-
"""Crea un programa que tome entrada del usuario y la escriba en un archivo llamada “salida.txt”. 
Si el archivo ya existe, sobrescríbelo."""

#Cadena introducida por el usuario
cadena=input("Escribe una cadena de texto: ")
#Abrir fichero
archivo=open("archivos/salida.txt","w")
#Escribir  fichero con la linea
archivo.write(cadena)

archivo.close()