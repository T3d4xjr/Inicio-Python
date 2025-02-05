# -*- coding: utf-8 -*- 
"""Escribe un programa que contenga un diccionario 
con información de clientes (nombre, correo, compras donde compras es una lista de productos).
 A continuación:
Guarda los datos en un archivo JSON.
Implementa una función que lea el JSON y devuelva el cliente con más compras.
"""
import json
def guardarClientes(clientes):
    with open("archivosRepaso/cliente.json", 'w') as fichero:
        json.dump(clientes, fichero)
def clienteMasCompras():
    with open("archivosRepaso/cliente.json", 'r') as fichero:
        clientes = json.load(fichero)

        masCompras=max(clientes, key=lambda c: len(clientes[c]['compras']))
        print("Cliente con mas compras "+str(masCompras))

clientes = {
    "Juan Pérez": {"correo": "juan@example.com", "compras": ["Manzanas", "Peras"]},
    "Ana Gómez": {"correo": "ana@example.com", "compras": ["Naranjas", "Uvas", "Kiwis"]},
    "Luis Martínez": {"correo": "luis@example.com", "compras": ["Plátanos"]}
}

guardarClientes(clientes)
clienteMasCompras()