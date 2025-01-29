# -*- coding: utf-8 -*-
"""Crea un programa que pida al usuario una palabra para buscar y una palabra para sustituir. 
Se deberá leer un archivo llamado “texto.txt” y  reemplazar todas las palabras que sean igual 
a la introducida por el usuario por la otra palabra especificada por el usuario. 
Guarda el resultado en un nuevo archivo llamado “modificado.txt”"""
#Abrir fichero
archivo=open('archivos/texto.txt','r')
#Abrir fichero
modificadoArchivo=open('archivos/modificado.txt','w')
#Cadenas buscar y sustituir
cadenaBuscar=input("Introduce una palabra a buscar: ")

cadenaSustituir=input("Introduce una palabra a sustituir: ")
#Nuevo archivo con sus replaces
modificadoArchivo.write(archivo.read().replace(cadenaBuscar,cadenaSustituir))

archivo.close()

modificadoArchivo.close()