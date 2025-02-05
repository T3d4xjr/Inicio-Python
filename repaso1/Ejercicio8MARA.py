
# -*- coding: utf-8 -*- 
"""Escribe un programa que un programa que 
lea un archivo de texto con datos de ventas (como producto, cantidad y precio). A continuación:
Almacena la información en una lista de diccionarios.
Calcula el total de ventas por producto.
Escribe un informe con los resultados en un nuevo archivo de texto.
"""

# Leer archivo de ventas y almacenar en una lista de diccionarios
def leerVentas():
    ventas = []
    with open("archivosRepaso/ventas.txt", 'r') as fichero:
        lista = fichero.readlines()
        for fila in lista[1:]:
            datos = fila.strip().split(',')
            venta = {
                'producto': datos[0],
                'cantidad': int(datos[1]),
                'precio': float(datos[2])
            }
            ventas.append(venta)
    return ventas
def totalVentas(ventas):
    totalProductos = {}
    for venta in ventas:
        producto = venta['producto']
        total = venta['cantidad'] * venta['precio']
        if producto in totalProductos:
            totalProductos[producto] += total
        else:
            totalProductos[producto] = total
    return totalProductos
def escribirInforme(resultados):
    with open("archivosRepaso/ventas2.txt",'w') as fichero:
        for producto, total in resultados.items():
            fichero.write("Productos: "+str(producto+" total ingresado: "+str(total)))


ventas = leerVentas()
resultados = totalVentas(ventas)
escribirInforme(resultados)