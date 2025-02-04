# -*- coding: utf-8 -*-
"""Escribe un programa que lea el archivo “empleados.json”, 
calcule el salario medio de cada departamento 
y cree un archivo nuevo llamado “resumen_departamentos.json”
con los salarios medios por departamento."""

import json

# Acumula datos por departamento
listaDepartamento = {}

# Lee el archivo de empleados
with open("archivos2/empleados.json", "r") as fichero:
    empleados = json.load(fichero)

    # Acumula salarios y empleados por departamento
    for empleado in empleados:
        departamento = empleado.get("departamento")
        salario = empleado.get("salario")
        if departamento in listaDepartamento:
            listaDepartamento[departamento]["totalSalario"] += salario
            listaDepartamento[departamento]["nEmpleados"] += 1
        else:
            listaDepartamento[departamento] = {"totalSalario": salario, "nEmpleados": 1}

# Calcula salarios medios
salariosMedios = {}
for departamento, datos in listaDepartamento.items():
    salariosMedios[departamento] = datos["totalSalario"] / datos["nEmpleados"]

# Guarda el resultado
with open("archivos2/resumen_departamentos.json", "w") as archivo:
    json.dump(salariosMedios, archivo)
