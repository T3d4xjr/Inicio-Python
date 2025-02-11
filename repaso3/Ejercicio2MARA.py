# -*- coding: utf-8 -*- 
"""Ejercicio 2:
Realizar un programa que obtenga el máximo y el mínimo de una serie de datos proporcionados en Hexadecimal. 
Para ello, se le pasará una lista de datos en formato hexadecimal a través de pantalla, y 
tendrá que convertirlos primero a formato Binario, y a continuación a formato Decimal. 
Hay que realizar lo siguiente:
Crear una función que reciba una lista de números hexadecimales y devuelva una tupla con el máximo y su valor decimal.
Crear una función de conversión de formato hexadecimal a binario en base a la siguiente tabla:

Crear una función de conversión de formato binario a decimal. Se recuerda que para pasar de binario a decimal, 
se deben utilizar las potencias de 2 como en la imagen de abajo:
"""
# Tablas de conversión
dHexadecimal = {
    "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15
}
hexaBinario = {
    "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101",
    "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011",
    "C": "1100", "D": "1101", "E": "1110", "F": "1111"
}
# Lista de datos en formato hexadecimal
hexadecimal = ["1A", "2F", "B4", "FF", "00", "5D"]
# Función para convertir de binario a decimal
def binarioAdecimal(binario):
    decimal = 0
    longitud = len(binario)
    for i in range(longitud):
        # Multiplicamos el bit por 2 elevado a la potencia de su posición
        decimal += int(binario[i]) * (2 ** (longitud - 1 - i))
    return decimal
# Convertir de hexadecimal a binario y luego a decimal
binarios = []
decimales = []
def listaHexadecimalConversion():
    for num in hexadecimal:
        # Convertir cada dígito hexadecimal a binario usando la tabla hexaBinario
        binario = ''.join(hexaBinario[digit] for digit in num)
        # Convertir el número binario a decimal
        decimal = binarioAdecimal(binario)
        # Añadir los resultados a las listas correspondientes
        binarios.append(binario)
        decimales.append(decimal)

    # Obtener el máximo y el mínimo en decimal
    maximo = max(decimales)
    minimo = min(decimales)

    # Mostrar los resultados
    print("Lista de hexadecimales:", hexadecimal)
    print("Lista de binarios:", binarios)
    print("Lista de decimales:", decimales)
    print("Máximo en decimal:", maximo)
    print("Mínimo en decimal:", minimo)

listaHexadecimalConversion()