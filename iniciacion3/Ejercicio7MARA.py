# -*- coding: utf-8 -*-
#Crea un programa que pida al usuario que introduzca una contraseña. Se tiene que verificar si la contraseña es segura, para ello tiene que cumplir:
#Tiene que tener más de 8 caracteres.
#Tiene que tener al menos una mayúscula y una minúscula.
#Tiene que tener al menos un número.
#Tiene que tener un carácter especial como +, ), /…

#Por pantalla se mostrará si la contraseña es segura 
# (si cumple todo lo anterior) o 
# si tiene que mejorar en algún parámetro (indicando que parámetro tiene que mejorar). 
# Se tienen que usar al menos 4 funciones.


def contraseñaValida():


    return input("Introduce una contraseña: ")

def caracteres(contraseña):

   return len(contraseña) > 8

def mayusYminus(contraseña):

    mayuscula=any(caracter.isupper() for caracter in contraseña)
    minuscula=any(caracter.islower() for caracter in contraseña)

    return mayuscula and minuscula
def minNumero(contraseña):

    return any(caracter.isdigit() for caracter in contraseña)

def caracterEspecial(contraseña):

    return any(caracter in "+)/!@#$%^&*()-_=<>?;:,.[]" for caracter in contraseña)

def verificar(contraseña):
    segura = True

    if not caracteres(contraseña):
        print("La contraseña debe tener al menos una mayúscula y una minúscula.")
        segura = False
    if not mayusYminus(contraseña):
        print("La contraseña debe tener al menos una mayuscula y una minuscula.")
        segura = False
    if not caracterEspecial(contraseña):
        print("La contraseña debe tener al menos un carácter especial (+, ), /, etc.).")
        segura = False
    return segura

contraseña=contraseñaValida()

if verificar(contraseña):
    print("¡Contraseña segura!")
else:
    print("Por favor, mejora tu contraseña según los requisitos.")