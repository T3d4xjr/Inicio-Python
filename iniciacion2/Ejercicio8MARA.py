# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario una palabra y 
#luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

try:
    #Introducimos la palabra
    palabra=str(input("Introduce una palabra: "))

    #la dividimos en letras y le damos la vuelta
    split=" ".join(reversed(palabra))

    print(split)
except ValueError:
    print("Error")