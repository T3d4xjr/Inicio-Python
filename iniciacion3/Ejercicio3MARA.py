# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca una cantidad aleatoria de palabras, 
#de una en una. Si el usuario no quiere introducir más palabras, que introduzca “FIN”. 
#El programa tiene que devolver todas las palabras ordenadas alfabéticamente, 
#teniendo en cuenta las mayúsculas y las minúsculas. Se debe usar al menos una función.
lista=[]
#Funcion para que el usuario introduzca las palabras que quiera y finalizar con FIN
def palabrasOrdenadas():
    #Hacemos un bucle para que podamos  meter las palabras en una lista y dps ordenarlas.
    while True:
        #Pedimos las palabras al usuario
        palabras=str(input("Escribe las palabras que quieras.FIN para finalizar: "))
        #Hacemos un punto para finalizar cuando escriba FIN.
        if palabras =="FIN":
            break
        #Añadimos a una lista y ordenamos las palabras convirtiendolas en minusculas pero a la hora
        # de mostrarlo lo mostramos teniendo en cuenta si son mayusculas o minusculas.
        lista.append(palabras)
        lista.sort(key=str.lower)

        
        
    print("Palabras ordenadas: "+str(lista))
palabrasOrdenadas()