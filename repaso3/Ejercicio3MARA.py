# -*- coding: utf-8 -*- 
"""Ejercicio 3:
Realizar un programa para la gestión de un cine. 
El cine tiene una sala rectangular con 5 filas y 4 columnas de butacas. 
Escribir un programa que permita gestionar la reserva de butacas con los siguientes requisitos:
El programa mostrará una matriz con el carácter X para las butacas libres y O para las ocupadas y preguntará por la fila y columna de la butaca a reservar.
Si el usuario introduce una fila o una columna no válidas, se le avisará y se le volverá a preguntar.
Si la fila y la columna introducida corresponde a una butaca ocupada, se avisará al usuario y se le volverá a preguntar.
Si la butaca está libre se reservará y se volverá a preguntar al usuario si quiere hacer más reservas.
El programa terminará cuando el usuario no quiera hacer más reservas.
"""
#Sala del cine 
sala =[['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X'],
 ['X', 'X', 'X', 'X']]
#Funcion para mostrar cada fila de la sala
def mostrarSala():
    for fila in sala:
        print(fila)
mostrarSala()

#Menu para hacer reservas o terminar y ver cuantas a reservado.
while True:
        print("1.Hacer reserva")
        print("2.Terminar reservas")
        opcion=input("Elige una opcion: ")
        if opcion =="1":
            try:
                filareserva = int(input("Ingrese la fila a reservar (0,1,2,3,4): "))
                columnareserva = int(input("Ingrese la columna a reservar (0,1,2,3): "))
                if filareserva < 0 or filareserva > 4 or columnareserva < 0 or columnareserva > 3:
                    print("La fila o la columna de la butaca no existe.Intentelo de nuevo")
                elif sala[filareserva][columnareserva] != "X":
                    print("La butuaca que quieres seleccionar esta ya seleccionada.Intentelo de nuevo")
                else:
                        sala[filareserva][columnareserva] = "O"
                mostrarSala() 
            except ValueError:
                print("¡Error! Por favor, ingrese un número válido para fila y columna.")
        elif opcion =="2":
            print("Gracias por sus reservar aqui mostraremos las seleccionadas con una O")
            mostrarSala()
            break