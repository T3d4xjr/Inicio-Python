# -*- coding: utf-8 -*-
"""
Dado un archivo “numeros.txt” que contiene un número por línea, escribe un programa que calcule:
La suma de todos los números.
El número máximo y mínimo.
La media.
"""

archivo=open("archivos/numeros.txt","r")

numeros=archivo.readlines()

numerosSuma=[]

for i in numeros:

    numerosSuma.append(int(i))

suma=sum(numerosSuma)
print("La suma es: "+str(suma))
numeroMaximo=max(numeros)
print("El numero maximo es: "+str(numeroMaximo))
numeroMinimo=min(numeros)
print("El numero minimo es: "+str(numeroMinimo))
media=suma/len(numerosSuma)
print("La media es: "+str(media))
archivo.close()
