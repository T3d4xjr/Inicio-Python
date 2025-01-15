#Escribir un programa que pida al usuario 5 números e imprima por pantalla el mayor de ellos.
lista=[]
turno=0
for i in range(5):

    numeros=int(input("Introduzca unos numeros:"))
    lista.append(numeros)        
print(max(lista))