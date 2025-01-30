# -*- coding: utf-8 -*-
"""Escribe un programa que lea el archivo “empleados.json”, calcule el salario medio de cada departamento 
y cree un archivo nuevo llamado “resumen_departamentos.json” con los salarios medios por departamento."""

import json

listaDepartamento = {}

with open("archivos2/empleados.json", "r") as fichero:
    empleados = json.load(fichero)

    for empleado in empleados:
        departamento = empleado.get("departamento")
        salario = empleado.get("salario")

        if departamento in listaDepartamento:
            listaDepartamento[departamento]["totalSalario"] += salario
            listaDepartamento[departamento]["nEmpleados"] += 1
        else:
            listaDepartamento[departamento] = {
                "totalSalario": salario,
                "nEmpleados": 1
            }
salariosMedios = {}

for departamento,departamentoDatos in listaDepartamento.items():
    salariosMedios[departamento]=departamentoDatos["totalSalario"]/departamentoDatos["nEmpleados"]

with open("archivos2/resumen_departamentos.json", "w") as archivo:
    json.dump(salariosMedios, archivo)


