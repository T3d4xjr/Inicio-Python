#Escribir un programa que pida al usuario una palabra y 
#luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.

try:
    palabra=str(input("Introduce una palabra: "))

    
    split=" ".join(reversed(palabra))

    print(split)
except ValueError:
    print("Error")