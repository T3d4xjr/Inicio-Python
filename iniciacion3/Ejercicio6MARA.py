# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca una cantidad de números aleatorios. 
# Si el usuario no quiere introducir más números, que introduzca “-1”. 
# El usuario no puede poder introducir datos que no sean números. 
# Se mostrará por pantalla el promedio, el máximo y el mínimo de la lista de números introducidos.
# Se deben utilizar al menos 4 funciones.

def pedir_numeros():
    listaNumeros = []
    while True:
        entrada = input("Introduce números aleatorios. Ingresa '-1' para finalizar: ")
        try:
            numero = int(entrada)  # Verifica si la entrada es un número
            if numero == -1:
                break  # Termina el bucle si el usuario ingresa -1
            listaNumeros.append(numero)
        except ValueError:  # Captura la excepción si la entrada no es un número entero
            print("Por favor, ingresa un número válido.")
    return listaNumeros     
    
def promedio():

    promedioNumeros=sum(listaNumeros)/len(listaNumeros)

    return promedioNumeros

def maximo():
    maximoNumero=max(listaNumeros)

    return maximoNumero
def minimo():
    minimoNumero=min(listaNumeros)

    return minimoNumero

listaNumeros=pedir_numeros()
print("Numeros: "+str(listaNumeros))

promedioNumeros=promedio()
print("Promedio: "+str(promedioNumeros))

maximoNumero=maximo()

print("Maximo: "+str(maximoNumero))
minimoNumero=minimo()

print("Minimo: "+str(minimoNumero))