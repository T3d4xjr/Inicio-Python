#Escribir un programa en el que se pregunte al usuario por una frase y una letra, 
# y muestre por pantalla el número de veces que aparece la letra en la frase.
try:
    palabra=str(input("Introduce una palabra: "))

    letra=str(input("Introduce una letra: "))

    contador=palabra.count(letra)

    print(contador)

except ValueError:
    print("Error")