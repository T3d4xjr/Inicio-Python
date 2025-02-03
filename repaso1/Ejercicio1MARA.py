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
        print(cadenaSplit)
        frecuenPalabra=[]
        contarFrecuencia=[]
        diccionarioPalabras={"palabras":""}
        diccionarioFrecuenciaOrdenado={"frecuencia":""}
        
        for palabra in cadenaSplit:
            if palabra in frecuenPalabra:
                print("La palabra: "+palabra+" repetida se contar pero no se mostrara")
            else:
                frecuenPalabra.append(palabra)
                diccionarioPalabras["palabras"]=frecuenPalabra
                contarFrecuencia.append(cadenaSplit.count(palabra))
                contarFrecuencia.sort(reverse=True)
                diccionarioFrecuenciaOrdenado["frecuencia"]=contarFrecuencia
        diccionarioPalabras["palabras"].sort(reverse=True) 
        print(str(diccionarioPalabras))
        print(str(diccionarioFrecuenciaOrdenado))
    except ValueError as e:
        print("Error de valor:", e)
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
    
funcionCadena()