#Crea una lista de números del 1 al 5. Inserta el número 3.1416 de tal manera que la lista esté ordenada de menor a mayor. Muestra la lista resultante por pantalla.

#Creamos la lista
lista=[1,2,3,4,5]
#Añadimos el nuevo elemento
lista.append(3.1416)
#Lo ordenamos de menor a mayor
lista.sort()
#Y lo imprimimos
print(lista)