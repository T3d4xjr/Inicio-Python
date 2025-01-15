# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados todo en una misma línea por comas
try:
    # Pedimos un número entero positivo al usuario
    numeroIntroducido = int(input("Pon un número positivo: "))
    
    # Verificamos si el número es positivo
    if numeroIntroducido < 0:
        print("Por favor, introduce un número entero positivo.")
    else:
        # Generamos la cuenta atrás y mostramos en una sola línea separada por comas
        cuenta_atras = ", ".join(str(i) for i in range(numeroIntroducido, -1, -1))
        print(cuenta_atras)
except ValueError:
    print("Debes introducir un número válido.")
