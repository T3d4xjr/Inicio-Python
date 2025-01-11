#Crea un diccionario que contenga una clave llamada “numeros” y como valor de dicha clave una lista de números del 1 al 5. 
#Añade el número 7 a esa lista y luego cambia el primer valor de la lista a 0. Imprime el diccionario final por pantalla.

#Diccionario con una lista de valores
diccionario = {"numeros":[1,2,3,4,5]}
#Le añadimos el 7
diccionario["numeros"].append(7)
#Ycambiamos el primer valor por cero
diccionario["numeros"][0]=0
#Y lo imprimimos
print(diccionario)