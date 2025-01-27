# -*- coding: utf-8 -*-
"""Crea un programa que tome entrada del usuario y la escriba en un archivo llamada “salida.txt”. 
Si el archivo ya existe, sobrescríbelo."""

cadena=input("Escribe una cadena de texto: ")

archivo=open("archivos/salida.txt","w")

archivo.write(cadena)

archivo.close