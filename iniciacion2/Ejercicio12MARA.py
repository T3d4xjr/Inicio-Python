#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.

# Pedir al usuario un número entero
numero = int(input("Introduce un numero: "))

# Un número primo debe ser mayor que 1
if numero > 1:
    # Verificar si tiene divisores desde 2 hasta el número - 1
    for i in range(2, int(numero**0.5) + 1):  
        if numero % i == 0:  
            print("Numero no primo")
            break
    else:
        # Si el bucle no encuentra divisores, es primo
        print("Numero primo")
else:
    print("Numero no primo")
