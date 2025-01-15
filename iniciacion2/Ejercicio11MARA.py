#Escribir un programa que almacene la cadena de caracteres “contraseña” en una variable y 
# pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


cadena="contraseña"

while(True):
    cadenaUsuario=str(input("Introduzca una contraseña: "))
    if cadenaUsuario !=cadena:
        print("Contraseña incorrecta")
    if cadenaUsuario ==cadena:
        print("Contraseña correcta")
        break;