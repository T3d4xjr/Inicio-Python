# -*- coding: utf-8 -*-
"""Crea un programa que permita al usuario:
Añadir nuevas notas (guardadas en un archivo notas.txt).
Leer todas las notas almacenadas.
Buscar notas por palabra clave.
Borrar una nota específica.
"""
#Funcion agregar nota
def agregarNota():
    nota = input("Escribe tu nota: ")
    with open("archivos/notas.txt","a") as archivo:
        archivo.write(nota + "\n")
    print("Nota añadida con éxito.")
#Funcion leer notas
def leerNotas():
    with open("archivos/notas.txt","r") as archivo:
        notas = archivo.readlines()
    print("Notas en el archivo.")
    print(str(notas))
#Funcion buscar nota
def buscarNota():
    palabra = input("Introduce una palabra clave para buscar: ")
    with open("archivos/notas.txt", "r") as archivo:
        resultados = [nota.strip() for nota in archivo if palabra in nota]
    print("Notas encontradas en el archivo.")
    print(str(resultados))
#Funcion borrar nota
def borrarNota():
    leerNotas()
    try:
        numero = int(input("Ingresa el número de la nota que deseas eliminar: "))
        with open("archivos/notas.txt", "r") as archivo:
            notas = archivo.readlines()
        if 1 <= numero <= len(notas):
            del notas[numero - 1]
            with open("archivos/notas.txt", "w") as archivo:
                archivo.writelines(notas)
            print("Nota eliminada con éxito.")
    except ValueError:
        print("Por favor, ingresa un número válido.")
#Funcion menu a eleccion del usuario
def menu():
    while True:
        print("\n--- Gestor de Notas ---")
        print("1. Añadir nueva nota")
        print("2. Leer todas las notas")
        print("3. Buscar notas por palabra clave")
        print("4. Borrar una nota específica")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregarNota()
        elif opcion == "2":
            leerNotas()
        elif opcion == "3":
            buscarNota()
        elif opcion == "4":
            borrarNota()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
menu()