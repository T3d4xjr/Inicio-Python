# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario los datos de altura y base de un rectángulo.
#Tiene que tener al menos dos funciones en las que se les pase los datos de la altura y la base del rectángulo 
#y devuelvan el área y el perímetro del mismo. Estos dos datos se tienen que mostrar al usuario por pantalla.

#Definimos una funcion llamada datosRectangulo para conseguir la altura y la base
def datosRectangulo():
    #Conseguimos la altura por entrada de usuario
    altura=int(input("Indique la altura : "))
    #Conseguimos la base por entrada de usuario
    base=int(input("Indique la base : "))
    #Retornamos esos datos
    return altura,base
#Definimos una funcion calculos rectangulos para calcular el area y el perimetro del rectangulo con los datos anteriores
def calculosRectangulo():
        #Calculos de area y perimetro
        area=altura*base
        perimetro=2*(altura+base) 
        #Retornamos esos datos
        return area,perimetro
#En orden vamos consiguiendo los datos de las funciones y los imprimimos
altura,base=datosRectangulo()
print(altura)
print(base)
#En orden vamos consiguiendo los datos de las funciones y los imprimimos
area,perimetro=calculosRectangulo()
print(area)
print(perimetro)
