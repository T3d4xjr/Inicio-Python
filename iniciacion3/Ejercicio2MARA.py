# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario dos años.
#Tiene que tener al menos una función donde se les pase ambos números y se calcule la cantidad de años bisiestos 
#que hay entre esos dos años. Por pantalla se tienen que mostrar esta cantidad y que años son los bisiestos. 
#Nota: el usuario puede meter los años en cualquier orden, es decir, no tiene por qué ser primero el mayor o el menor.

def años():
    #Pedimos los dos años al usuario
    año1=int(input("Escribe el primer año: "))

    año2=int(input("Escribe el segundo año: "))
    #Creamos una lista y una cantidad
    lista=[]
    cantidad=0
    #Aqui iteramos si el año1 es mayor al año2 cambiamos los valores para realizar el bucle
    if(año1>año2):
        año1,año2=año2,año1
        for bisiesto in range(año1,año2):
            #Comprobacion de que un año es bisiesto
            if bisiesto  % 4 == 0 and bisiesto  % 100 !=0 or bisiesto % 400 ==0: 
                #Añadimos a la lista los años bisiestos y sumamos la cantidad
                lista.append(bisiesto)
                cantidad+=1
                
    else:
        for bisiesto in range(año1,año2):
            #Comprobacion de que un año es bisiesto
            if bisiesto  % 4 == 0 and bisiesto  % 100 !=0 or bisiesto % 400 ==0:    
                #Añadimos a la lista los años bisiestos y sumamos la cantidad
                lista.append(bisiesto)
                cantidad+=1
    #Mostramos por pantalla al usuario los años bisiestos y cuantos años bisiestos hay
    print("Cantidad: "+str(cantidad))
    print("Los años que son bisiestos "+str(lista))
                
años()



