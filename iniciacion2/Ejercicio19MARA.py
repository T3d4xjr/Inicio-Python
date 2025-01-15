# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario una palabra y compruebe si es un palíndromo o no.

# Pedir al usuario que ingrese una palabra
palabra = str(input("Introduzca una palabra: "))

# Crear la versión invertida de la palabra utilizando el rebanado con paso -1
palabraReves = palabra[::-1]

# Comparar la palabra original con la invertida
if palabra == palabraReves:
    # Si son iguales, es un palíndromo
    print("Es palindromo")
else:
    # Si no son iguales, no es un palíndromo
    print("No es palindromo")
