# -*- coding: utf-8 -*- 
"""Escribe un programa que tenga una función que pida al
 usuario que ingrese una lista de números separados por comas. 
 A partir de esa función, se hará lo siguiente:
Convierte la entrada en una lista de enteros.
Calcula la suma y el promedio.
Maneja excepciones si el usuario ingresa un valor que no es un número.
"""

def ingresarNumeros():
    try:
        cadenaNumeros = input("Ingresa una lista de números separados por comas: ")
        
        lista = [int(numero.strip()) for numero in cadenaNumeros.split(",")]
        
        suma = sum(lista)
        promedio = suma / len(lista)
        
        print(f"La suma es: {suma}")
        print(f"El promedio es: {promedio}")
    
    except ValueError:
        print("Error: Por favor ingresa solo números separados por comas.")

ingresarNumeros()
