# -*- coding: utf-8 -*-
#Modifica el programa anterior para que el usuario no introduzca palabras repetidas.

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
        # Verificamos si la palabra ya está en la lista sin distinguir mayúsculas o minúsculas
        if palabras.lower() in (p.lower() for p in lista):
            print("Esa palabra ya esta en la lista pon una diferente")
        else:
            # Agregamos la palabra a la lista si no está repetida
            lista.append(palabras)
            #Y la ordenamos sin tener en cuenta si son mayusculas o minusculas las ordena a todas
            lista.sort(key=str.lower)
        
        
    print("Palabras ordenadas: "+str(lista))
palabrasOrdenadas()