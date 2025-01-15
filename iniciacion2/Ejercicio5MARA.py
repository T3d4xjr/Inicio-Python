# -*- coding: utf-8 -*-
#Escribir un programa que imprima los primeros 10 números de la sucesión de Fibonacci. 
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
# cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

# Inicializar los dos primeros números de la secuencia de Fibonacci
fibo_anterior = 0
fibo_actual = 1

# Imprimir el primer número de la secuencia
print(fibo_anterior)

# Recorremos para imprimir los siguientes 9 números 
for p in range(9):
    print(fibo_actual)  # Imprimir el número actual
    # Calcular el siguiente número de la secuencia
    fibo_siguiente = fibo_anterior + fibo_actual
    # Actualizar los valores para la siguiente iteración
    fibo_anterior = fibo_actual
    fibo_actual = fibo_siguiente
