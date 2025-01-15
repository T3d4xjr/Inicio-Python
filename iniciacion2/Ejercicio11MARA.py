# -*- coding: utf-8 -*-
#Escribir un programa que almacene la cadena de caracteres “contraseña” en una variable y 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

#Cadena contraseña 
cadena="contraseña"

while(True):
    #Intenta el usuario averiguar la contraseña
    cadenaUsuario=str(input("Introduzca una contraseña: "))
    #Si es incorrecta que siga intentando
    if cadenaUsuario !=cadena:
        print("Contraseña incorrecta")
    if cadenaUsuario ==cadena:
        print("Contraseña correcta")
        break;