#Escribir un programa que imprima los primeros 10 números de la sucesión de Fibonacci. 
# La sucesión comienza con los números 0 y 1 y, a partir de éstos, 
# cada elemento es la suma de los dos números anteriores en la secuencia: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

def fibonacci(n):

    if n > 1:
        return fibonacci(n-1)+fibonacci(n-2)
    return n
for cantidad in range(10):
    print(fibonacci(cantidad))
    