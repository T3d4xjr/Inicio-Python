# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca una cantidad aleatoria de palabras, 
#de una en una. Si el usuario no quiere introducir más palabras, que introduzca “FIN”. 
#El programa tiene que devolver todas las palabras ordenadas alfabéticamente, 
#teniendo en cuenta las mayúsculas y las minúsculas. Se debe usar al menos una función.
def palabrasOrdenadas():
    while True:
        lista=[]
        palabras=str(input("Escribe las palabras que quieras.FIN para finalizar: "))
        lista.append(palabras)
        if palabras =="FIN":
            break
        
        lista.sort(key=str.lower)

        
        
    print("Palabras ordenadas: "+str(lista))
palabrasOrdenadas()