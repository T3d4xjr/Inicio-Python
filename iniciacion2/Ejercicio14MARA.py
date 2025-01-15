# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario 5 números e imprima por pantalla el mayor de ellos.
# Crear una lista vacía para almacenar los números introducidos
lista = []

# Bucle que se repite 5 veces
for i in range(5):
    numeros = int(input("Introduzca unos numeros:"))
    lista.append(numeros)  # Agregar el número ingresado a la lista

# Imprimir el número máximo de la lista 
print(max(lista))
