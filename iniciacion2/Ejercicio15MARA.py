# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario 2 números y una operación 
# (suma, resta, multiplicación y división), calcule el resultado y lo imprima por pantalla.

#Numeros a introducir
numero=int(input("Introduzca un numero: "))
numero2=int(input("Introduzca otro numero: "))

#Clarito lo que tiene que poner el usuario para que haga las operaciones
operacion =str(input("Introduzca una operacion:Sumar = +,Restar = -,Multiplicar = *,Dividir = / : "))

#Operaciones con su resultado
if operacion =="+":
    resultado=numero+numero2
    print(resultado)
elif operacion =="-":
    resultado=numero-numero2    
    print(resultado)
elif operacion =="*":
    resultado=numero*numero2
    print(resultado)
elif operacion =="/":
    resultado=numero/numero2
    print(resultado)
else:
    print("Signo de operacion invalido")