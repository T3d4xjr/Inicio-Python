#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo, 
#representado con asteriscos (*), con la altura del número introducido.

altura=int(input("Introduca una altura: "))

for p in range(0,altura+1):

    print("*"*p)