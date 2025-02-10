# -*- coding: utf-8 -*- 
"""Escribe un programa que contenga una función que reciba un párrafo como cadena y realice lo siguiente:
Cuente la frecuencia de cada palabra y la almacene en un diccionario.
Ordene el diccionario de mayor a menor frecuencia.
Maneje excepciones en caso de recibir un dato incorrecto (por ejemplo, un número en lugar de un texto).
"""

def funcionCadena():
    try:
        cadena=str(input("Escribe un parrafo: "))

        cadenaSplit=cadena.split(" ")
        frecuencia={}

        #Cuenta cada palabra y va almacenandolas en un diccionario por su frecuencia
        for palabra in cadenaSplit:
            if palabra in frecuencia:
                frecuencia[palabra]+=1
            else:
                frecuencia[palabra]=1
        
        #Nos piden que ordenemos por mayor a menor frecuencia para ello recorremos el diccionario ordenandolo 
        # y utilizando la funcion lambda con valor x que seria todos los elementos y cogeria el segudo elemento que haya en el diccionario en este caso la frecuencia 
        #Por el simple hecho que el diccionario en el 0 esta la clave y en el 1 esta los valores de esa clase que son la frecuencia que queremos ordenar

        ordenarFrecuencia=dict(sorted(frecuencia.items(),key=lambda x:x[1],reverse=True))
        print(frecuencia)
        print(ordenarFrecuencia)
    except ValueError as e:
        print("Error de valor:", e)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
    
funcionCadena()