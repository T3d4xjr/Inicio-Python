# -*- coding: utf-8 -*-
"""Escribe un programa que lea el archivo “estudiantes.json” y que calcule y 
muestre por pantalla la media de las calificaciones y el estudiante con las calificaciones más altas."""
import json

with open("archivos2/estudiantes.json","r") as fichero:
    estudiantes = json.load(fichero) 
    lista = [] 
    print(estudiantes)    
    for estudiante in estudiantes:  
        calificacion = estudiante.get("calificacion") 
        lista.append(calificacion)
            
    media = sum(lista) / len(lista)
    print(media)
    mejorCalificacion=max(lista)
    for estudiante in estudiantes:  
        if estudiante.get("calificacion") ==mejorCalificacion:
            mejorEstudiante=estudiante.get("nombre")
    print("El alumno: "+str(mejorEstudiante)+" tiene la mejor nota con: "+str(mejorCalificacion))
         
