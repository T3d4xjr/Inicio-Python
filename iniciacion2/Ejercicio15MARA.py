#Escribir un programa que pida al usuario 2 números y una operación 
# (suma, resta, multiplicación y división), calcule el resultado y lo imprima por pantalla.

numero=int(input("Introduzca un numero: "))
numero2=int(input("Introduzca otro numero: "))

operacion =str(input("Introduzca una operacion:Sumar = +,Restar = -,Multiplicar = *,Dividir = / : "))

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