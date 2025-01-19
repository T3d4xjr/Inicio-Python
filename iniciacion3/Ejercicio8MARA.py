# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca el nombre y la calificación de estudiantes. 
# Cuando no quiera introducir más estudiantes, que ponga la palabra “FIN”. 
# El programa tiene que detectar si se introduce algún alumno y nota iguales. 
# Se tendrá que devolver el promedio de notas, el mejor estudiante y el peor estudiante. 
# Se usarán al menos tres funciones.

def estudiantes():

    estudiante = {}
    while True:
        # Pedir nombre
        nombre = input("Introduce el nombre del estudiante (o escribe 'FIN' para terminar): ").strip()
        if nombre.upper() == "FIN":  # Terminar si se escribe "FIN"
            break
        
        if nombre in estudiante :
            print("El estudiante ya esta introducido.Escribe otro")
            continue
        
        # Pedir calificación
        try:
            calificacion = float(input("Introduce la calificación: "))
            estudiante[nombre] = calificacion  # Guardar nombre como clave y calificación como valor
        except ValueError:  # Validar que la calificación sea un número
            print("❌ Error: Introduce una calificación válida.")

    return estudiante
        
def promedioEstudiante(estudiante):

    if estudiante:  # Verifica si el diccionario tiene estudiantes
        promedio = sum(estudiante.values()) / len(estudiante)  # Promedio de calificaciones
        return promedio

    return promedio
def maxYmin(estudiante):
    #Calcula el promedio, el mejor estudiante y el peor estudiante.

    if estudiante:  # Verifica si el diccionario tiene estudiantes
        mejorEstudiante = max(estudiante, key=estudiante.get)  # Nombre del mejor estudiante
        peorEstudiante = min(estudiante, key=estudiante.get)   # Nombre del peor estudiante
        return mejorEstudiante, peorEstudiante

estudiante=estudiantes()

if not estudiante:
    print("No hay estudiantes")

promedio=promedioEstudiante(estudiante)

mejorEstudiante,peorEstudiante=maxYmin(estudiante)

print("Promedio: "+str(promedio))
print("Mejor estudiante: "+str(mejorEstudiante))
print("Peor estudiante: "+str(peorEstudiante))