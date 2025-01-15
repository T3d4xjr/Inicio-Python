# -*- coding: utf-8 -*-
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
try:
    #Escribimos la palabra
    palabra=str(input("Introduce una palabra: "))
    #Escribimos la letra
    letra=str(input("Introduce una letra: "))
    #Contamos cuantas veces esa letra sale en la palabra
    contador=palabra.count(letra)
    #Y lo imprimimos
    print(contador)

except ValueError:
    print("Error")