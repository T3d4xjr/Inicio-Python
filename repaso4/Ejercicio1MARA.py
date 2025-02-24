# -*- coding: utf-8 -*- 
"""Crea una función que reciba dos array, un booleano y retorne un array.
Si el booleano es verdadero buscará y retornará los elementos comunes de los dos array.
Si el booleano es falso buscará y retornará los elementos no comunes de los dos array.
"""

def buscarElementos():
    array=["manzana","platano","pera"]
    array2=["naranja","platano","pera","papa"]
    repetidos=[]
    noRepetidos=[]
    for elemento in array:
        for elemento2 in array2:
            if elemento  in array2:
                    repetidos.append(elemento)
                    break
            if elemento not in array2:
                 noRepetidos.append(elemento)
                 break
    for elemento2 in array2:
        for elemento in array:
            if elemento2 not in array:
                    noRepetidos.append(elemento2)
                    break
            
    mensaje=(input("Manda un true para ver los repetios y un false para los no repetidos:"))  
     
    if mensaje=="true":
        print("Elementos repetidos: "+str(repetidos))

    elif mensaje=="false":
        print("Elementos no repetidos: "+str(noRepetidos))
    else:
        print("Formato desconocido")

buscarElementos()