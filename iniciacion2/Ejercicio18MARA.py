# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario un número de al menos 4 cifras 
# e imprima por pantalla la suma de sus dígitos.

# Solicitar al usuario que ingrese un número de 4 dígitos
numero = input("Introduce un numero de 4 digitos: ")

# Verificar que el número ingresado es válido: que sea numérico y tenga al menos 4 cifras
while not (numero.isdigit() and len(numero) >= 4):
    # Si el número no es válido, solicita al usuario un nuevo número
    numero = input("Introduzca un numero valido: ")

# Sumar los dígitos 
suma = sum(int(digito) for digito in numero)

# Y lo imprimos
print("La suma es " + str(suma))
