# -*- coding: utf-8 -*-
#Escribe un programa que lea un archivo de texto y cuente cuántas palabras contiene.

#Contador de palabras
numPalabra=0
#Abrir fichero
with open('archivos/datos.txt','r') as fichero:
    leer = fichero.read()
    palabras=leer.split()
    #Recorrer las palabras y sumar al contador
    for palabra in palabras:

        numPalabra+=1

print(numPalabra)

fichero.close()