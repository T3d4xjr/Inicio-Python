# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario un número entero positivo 
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
#Utilizamos el try para capturar si hay excepciones de cualquier tipo si no es un numero
try:
    numeroIntroducido =int(input("Pon un numero positivo: "))
    #Recorremos ese numero
    for numeros in range(0,numeroIntroducido,1):
        
        #Y aqui mostramos los numeros que sean impares
        if numeros % 2 != 0 :
            print(numeros)
        #Mostramos un error en caso de lo que el usuario no ha dado no sea un numero
        
except ValueError:
    print("Debes introducir un numero") 