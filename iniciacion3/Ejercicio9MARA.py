# -*- coding: utf-8 -*-
"""Crea un programa que gestione un inventario. Las opciones que se le muestran al usuario son:
Agregar producto. El usuario podrá añadir productos proporcionando nombre, cantidad y precio.
Actualizar producto. El usuario podrá modificar la cantidad de un producto.
Valor del inventario de un producto. El usuario podrá verificar el valor total de un producto.
Valor del inventario total. El usuario podrá verificar el valor total del inventario.
Mostrar el inventario. Se mostrará el valor del inventario (nombre de los productos, cantidad y precio)
Si el usuario no quiere realizar más acciones, se indicará y se terminará la ejecución.
Cosas a tener en cuenta:
Se deberá realizar usando diccionarios (con clave y valor)
No se puede ni actualizar ni ver el valor del inventario de un producto si no existe dicho producto.
Se pueden utilizar las funciones que se crean necesarias para que el código quede lo más limpio y funcional posible.
"""


def inventario():
    inventory={"nombre":[],"cantidad":[],"precio":[]}

    return inventory
def agregraProducto(inventory):
    nombreProducto=str(input("Agrega un nombre: "))
    cantidadProducto=int(input("Agrega una cantidad: "))
    precioProducto=float(input("Agrega un precio: "))
    
    
    inventory["nombre"].append(nombreProducto)
    inventory["cantidad"].append(cantidadProducto)
    inventory["precio"].append(precioProducto)
   
    return inventory
def actualizarProducto(inventory):

    nombreProducto=str(input("Dime el nombre del producto a actualizar: "))

   

    if nombreProducto in inventory["nombre"]:
        indice=inventory["nombre"].index(nombreProducto)

        cantidadActualizada=int(input("Agrega una nueva cantidad: "))
        
        inventory["cantidad"][indice] = cantidadActualizada
    else:
        print("No existe el producto")
    return inventory
def valorInventarioProducto(inventory):

    return inventory
def valorInventarioTotal(inventory):

    return inventory

inventory=inventario()
print("Inventario")
print("1.Agregar Producto")
print("2.Actualizar Producto")
print("3.Valor del inventario de un producto")
print("4.Valor inventario total")
print("5.Mostrar inventario")
print("6.Salir")

while True:
    
    opcion=int(input("Elige un numero: "))
    if opcion ==1:
        inventory=agregraProducto(inventory)
    if opcion ==2:
        inventory=actualizarProducto(inventory)
    if opcion ==3:
        print("")
    if opcion ==4:
        print("")
    if opcion ==5:
        print(inventory)
    if opcion ==6:
        print("Saliendo")
        break
