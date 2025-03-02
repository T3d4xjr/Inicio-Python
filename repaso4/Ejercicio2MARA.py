# -*- coding: utf-8 -*- 
"""Crea una función, que dado un año, indique el elemento y animal correspondiente en el ciclo sexagenario del zodíaco chino.
Info: https://www.travelchinaguide.com/intro/astrology/60year-cycle.htm
El ciclo sexagenario se corresponde con la combinación de los elementos madera, fuego, tierra, metal, agua y 
los animales rata, buey, tigre, conejo, dragón, serpiente, caballo, oveja, mono, gallo, perro, cerdo (en este orden).
Cada elemento se repite dos años seguidos.
El último ciclo sexagenario comenzó en 1984 (Madera Rata).
"""

#Funcion que recoge los elementos y los animales y los corresponde a su año en el ciclo sexagenario
def cicloSexagenario(agno):
    elementos=["madera","madera","fuego","fuego","tierra","tierra","metal","metal","agua","agua"]
    animales=["rata","buey","tigre","conejo","dragón","serpiente","caballo","oveja","mono","gallo","perro","cerdo"]

    agnoBase=1984
    modulo =(agno-agnoBase)%60
    signo =elementos[modulo%10]
    animal=animales[modulo%12]

    return signo+"-"+animal

#Mostar animal y elemento asignado al año
print(cicloSexagenario(1971))