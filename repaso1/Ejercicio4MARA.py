# -*- coding: utf-8 -*- 
"""Escribe un programa que administre un diccionario de ventas de productos 
con la siguiente estructura:
Se deberá:
Escribir una función que calcule el total de ingresos.
Guardar los datos en un archivo json.
Implementar una función para que se pueda actualizar el inventario restando productos vendidos y guardando los cambios en el json
"""
import json

ventas ={
    "producto1":{"precio":10,"cantidad":5},
    "producto2":{"precio":20,"cantidad":3}
}

def calcularIngresos(ventas):
    totalIngresos=0
    for producto,datos in ventas.items():
        ingreso=datos["precio"] * datos["cantidad"]
        totalIngresos+=ingreso
        print("Producto: "+str(producto)+" ingreso: "+str(ingreso))

    print("Total ingresos "+str(totalIngresos))

    ventas["total"]=totalIngresos
    with open("archivosRepaso/archivo2.json","w") as fichero:
        json.dump(ventas,fichero)

def actualizarProducto(producto,cantidad):
    try:
        with open("archivosRepaso/archivo2.json","r") as fichero:
                ventas = json.load(fichero)
        if producto in ventas:
            if ventas[producto]["cantidad"] >= cantidad:
                ventas[producto]["cantidad"] -= cantidad
    
        with open("archivosRepaso/archivo2.json","w") as fichero:
            json.dump(ventas,fichero)     

    except FileNotFoundError:
        print("El archivo de ventas no existe. Guarda primero los datos iniciales.")

calcularIngresos(ventas)
actualizarProducto("producto1",2)