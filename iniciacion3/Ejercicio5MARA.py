# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca una cantidad de horas, 
#el coste €/hora y el porcentaje de impuestos.
# Se tiene que mostrar por pantalla el sueldo bruto, 
#los impuestos que se pagarían y el sueldo neto. Para cada parámetro utilizar una función.

#Funcion donde recogemos los datos del usuarios de sus nHoras,coste y impuesto.
def programaTrabajo():

    nHoras=int(input("Introduzca un numero de horas: "))

    coste=int(input("Introduzca el dinero por hora: "))

    impuesto=int(input("Introduzca el impuesto: "))
    #Retornamos esos valores para poder utilizarlos despues.
    return nHoras,coste,impuesto
#Funcion que calcula el sueldoBruto
def sueldoBruto():

        dineroBruto=nHoras*coste

        return dineroBruto
#Funcion que calcula el dinero de impuestos a retirar
def impuestos():
        dineroImpuesto=dineroBruto*(impuesto/100)

        return dineroImpuesto
#Funcion que calcula el sueldoNeto
def sueldo_neto():
       sueldoNeto=dineroBruto-dineroImpuesto

       return  sueldoNeto

#Aqui son las llamadas a la funcion y mostramos los valores de cada una de las funciones
nHoras,coste,impuesto=programaTrabajo()

#Sueldo Bruto
dineroBruto=sueldoBruto()
print("Dinero bruto: "+str(dineroBruto))

dineroImpuesto=impuestos()
#Impuestos
print("Dinero de impuesto: "+str(dineroImpuesto))
#Sueldo Neto
sueldoNeto=sueldo_neto()
print("Dinero neto: "+str(sueldoNeto))