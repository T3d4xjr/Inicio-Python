# -*- coding: utf-8 -*-
"""Dado un archivo de log (“servidor.log”) donde cada línea contiene un timestamp, 
una dirección IP y un mensaje, crea un programa que:
Cuente cuántas veces aparece cada dirección IP.
Extraiga todas las líneas que contienen un mensaje de error en un archivo errores.log.
"""
# Contar IPs y almacenar errores
ips = {}
errores = []

# Abrir archivo
with open("archivos/servidor.log", "r") as archivo:
    for linea in archivo:
        partes = linea.split()
        ip = partes[2]

        # Contar IP
        ips[ip] = ips.get(ip, 0) + 1

        # Guardar errores
        if "Error" in linea:
            errores.append(linea)

# Escribir errores
with open("archivos/errores.log", "w") as archivosErrores:
    archivosErrores.writelines(errores)

for ip, cantidad in ips.items():
    print(f"La ip: {ip} ha salido: {cantidad} veces")
