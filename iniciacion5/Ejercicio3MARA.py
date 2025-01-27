# -*- coding: utf-8 -*-
#Escribe un programa que lea un archivo de texto y cuente cuántas palabras contiene.

numPalabra=0
with open('archivos/datos.txt','r') as fichero:
    leer = fichero.read()
    palabras=leer.split()
    for palabra in palabras:

        numPalabra+=1

print(numPalabra)

fichero.close()