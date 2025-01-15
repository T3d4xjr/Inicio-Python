# -*- coding: utf-8 -*-
#Escribir un programa que imprima la sumatoria de todos los números entre el 0 y el 100.

#Iniciamos una variable que va a ser la que imprimimos con el sumatorio
total = 0
#Este bucle esta hecho para que entre el 0 y el 100  y lo metemos en una variable
for a in range(0,101):
     
     total =total + a
#La imprmimos sin poner en tabulador para que nos muestre el ultimo numero del bucle que es la suma total.
print(total)