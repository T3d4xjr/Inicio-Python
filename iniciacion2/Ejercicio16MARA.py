# -*- coding: utf-8 -*-
#Escribir un programa que pida al usuario 4 palabras y las muestre ordenadas alfabéticamente,
# separadas por comas, por pantalla

# Crear una lista vacía para almacenar las palabras introducidas
lista = []

for i in range(4):
    # Solicitar al usuario que ingrese una palabra y agregarla a la lista
    lista.append(str(input("Introduzca unas palabras: ")))

# Ordenar la lista alfabéticamente
lista.sort()

#Mostramos por pantalla la lista separadas por comas
print(",".join(lista))
