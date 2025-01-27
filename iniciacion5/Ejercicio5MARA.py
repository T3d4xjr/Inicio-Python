# -*- coding: utf-8 -*-
"""Escribe un programa que lea un archivo CSV llamado “datos.csv” y muestre cada fila como una lista. 
A continuación, convierte los datos en un diccionario, donde la primera fila del CSV se usa como claves."""

archivo=open("archivos/datos.csv","r")

lista=archivo.read()
listaSeparada=lista.split(",")

diccionario = {
    listaSeparada[0]: [listaSeparada[4], listaSeparada[9], listaSeparada[14]],
    listaSeparada[1]: [listaSeparada[5], listaSeparada[10], listaSeparada[15]],
    listaSeparada[2]: [listaSeparada[6], listaSeparada[11], listaSeparada[16]],
    listaSeparada[3]: [listaSeparada[7], listaSeparada[12], listaSeparada[17]]
}

print("Las claves son: "+str(diccionario.keys()))
print("Los valores son: "+str(diccionario.values()))

archivo.close()