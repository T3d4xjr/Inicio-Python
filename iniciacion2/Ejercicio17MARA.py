
import random
#Escribir un programa que pida al usuario adivinar un número secreto entre 1 y 50. 
# El programa le tiene que ir dando pista si el número secreto es mayor o menor en cada
#  intento y si en menos de 7 intentos lo ha acertado, el usuario habrá ganado.
#  En caso contrario, habrá perdido.


# Generar un número secreto aleatorio entre 1 y 50
numeroSecreto = random.randrange(1, 51)

# Establecer el número de intentos disponibles
intento = 7
# Imprimir el número secreto para comprobar si funciona el codigo
print(numeroSecreto)

while True:
    
    # Solicitar al usuario que ingrese un número
    numeroUsuario = int(input("Introduzca un numero: "))

    # Comprobar si el número ingresado es mayor que el número secreto
    if numeroUsuario > numeroSecreto:
        print("El numero es menor")
        # Restar 1 al contador de intentos
        intento -= 1
        print(intento)
        
    # Comprobar si el número ingresado es menor que el número secreto
    elif numeroUsuario < numeroSecreto:
        print("El numero es mayor")
        # Restar 1 al contador de intentos
        intento -= 1
        print(intento)

    # Si el número ingresado es igual al número secreto y aún quedan intentos
    if intento > 0 and numeroUsuario == numeroSecreto:
        # Imprimir mensaje de victoria
        print("Has ganado")
        break

    # Si los intentos se agotan y el número no es el secreto
    elif intento == 0 and numeroUsuario != numeroSecreto:
        # Imprimir mensaje de derrota
        print("Has perdido")
        break
