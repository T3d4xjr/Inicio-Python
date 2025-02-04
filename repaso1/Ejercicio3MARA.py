# -*- coding: utf-8 -*- 
"""Escribe un programa que permita realizar lo siguiente:
Con una función, se le pedirá al usuario que introduzca un texto. 
Ese texto se almacenará en una lista
Se convertirán todas las palabras a letras minúsculas y 
se eliminarán los signos de puntuación
Si el usuario ingresa un número en vez de un texto, 
se manejará la excepción y se solicita que vuelva a ingresar una cadena válida.
"""

def usuariolista():
    while True:
        cadena = input("Escribe un texto o salir par finalizar el programa : ")
        
        if cadena=="salir":
            break
        if any(numero.isdigit() for numero in cadena):
            print("La cadena contiene un numero intentelo de nuevo")
        
        signos = ",.!¿¡?"

        cadenaSinSigno = cadena.translate(str.maketrans('', '', signos))

        lista = [cadenaSinSigno.lower()]

        print(lista)
        
        

usuariolista()
