# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo, 
#representado con asteriscos (*), con la altura del número introducido.

#Introduce la altura el usuario
altura=int(input("Introduca una altura: "))
#la recorremos desde cero sumando uno
for p in range(0,altura+1):
    #y esos valores los concatenamos con los asteriscos
    print("*"*p)