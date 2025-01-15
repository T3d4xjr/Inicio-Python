import math
#Escribir un programa que pida al usuario 5 números e imprima por pantalla el mayor de ellos.
lista=[]
turno=0
while True:

    numeros=int(input("Introduzca unos numeros:"))
    lista.append(numeros)
    turno+=1
    if turno ==5 :
        
        print(max(lista))
        break