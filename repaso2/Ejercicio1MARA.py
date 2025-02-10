# -*- coding: utf-8 -*- 
"""Crea un programa que permita a un usuario registrar su horario de clases. Para ello:
Se debe pedir al usuario que ingrese el nombre de la materia, el día de la semana y la hora.
Almacenar la información en un diccionario donde la clave sea el día y el valor una lista de clases.
Guardar el diccionario en un archivo JSON.
El usuario puede indicar que quiere ver el horario de un día específico, por tanto, se realizará una función para leer el archivo y mostrar el horario de dicho día.
"""
import json

#Agregar las clases con sus horas y dia de la semana  y guardalas en un diccionario 
def agregarClase(horario):
    materia = input("Ingrese el nombre de la materia: ")
    dia = input("Ingrese el día de la semana: ")
    hora = input("Ingrese la hora de la clase (HH:MM): ")
    if dia not in horario:
        horario[dia] = []
    horario[dia].append({"materia": materia, "hora": hora})
    with open("archivosRepaso2/horario.json", "w") as fichero:
        json.dump(horario, fichero)
    print("Clase agregada exitosamente.")

#Ver el horario y el nombre de la clase asignado a un dia
def verHorario(horario):
    dia = input("Ingrese el día de la semana que desea consultar: ")
    if dia in horario:
        print("Horario del dia: "+str(dia))
        for clase in horario[dia]:
            print("Clase: "+str(clase["materia"])+" a las: "+str(clase["hora"]))
    else:
        print("No hay clases registradas para este día.")

try:
    with open("horario.json", "r") as fichero:
        horario = json.load(fichero)
except FileNotFoundError:
    horario = {}
#Menu interactivo
while True:
    print("1. Agregar clase")
    print("2. Ver horario de un día")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        agregarClase(horario)
    elif opcion == "2":
        verHorario(horario)
    elif opcion == "3":
        print("Saliendo ...")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
