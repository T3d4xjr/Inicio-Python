# -*- coding: utf-8 -*- 
"""Crea un programa que simule un cajero automático con las siguientes características:
Un diccionario almacenará usuarios (clave) y sus saldos (valor).
Implementa funciones para depositar, retirar y consultar saldo. Todas estas operaciones tiene que poder hacer el usuario.
Maneja errores como fondos insuficientes o intentos de retiro de cantidades no válidas.
"""
import json
usuarios = {"user1": 1000, "user2": 500, "user3": 1500}
#Depositar dinero
def depositar(usuario):
    dinero = float(input("Ingrese el dinero a depositar: "))
    if dinero > 0:
        usuarios[usuario] += dinero
        print("Deposito exitoso")
    else:
        print("Dinero no válido.")
#Retirar dinero
def retirar(usuario):
    dinero = float(input("Ingrese el dinero a retirar: "))
    if dinero > 0 and dinero <= usuarios[usuario]:
        usuarios[usuario] -= dinero
        print("Retiro exitoso.")
    elif dinero > usuarios[usuario]:
        print("Fondos insuficientes.")
    else:
        print("Dinero no válido.")
#Mostrar saldo
def consultarSaldo(usuario):
    print("Su saldo actual es: "+str(usuarios[usuario]))

#Cajero en forma de menu con sus acciones por cada usuario
usuario = input("Ingrese su usuario: ")
if usuario not in usuarios:
    print("Usuario no encontrado.")
else:
    while True:
        print("1.Depositar")
        print("2. Retirar")
        print("3. Consultar saldo")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            depositar(usuario)
        elif opcion == "2":
            retirar(usuario)
        elif opcion == "3":
            consultarSaldo(usuario)
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")