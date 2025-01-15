# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario números hasta que introduzca un -1.
#  Cuando introduzca un -1, se devolverá por pantalla el promedio de los números ingresados.

# Inicializamos una lista para guardar los números
numeros = []

# Bucle que pide números hasta que se ingresa un -1
while True:
    numero = float(input("Introduce un número (o -1 para terminar): "))
    
    # Salir del bucle si el número es -1
    if numero == -1:
        break
    
    # Agregar el número a la lista
    numeros.append(numero)

# Verificar si se han ingresado números
if numeros:
    # Calcular el promedio
    promedio = sum(numeros) / len(numeros)
    print("El promedio de los números ingresados es: "+str(promedio))

