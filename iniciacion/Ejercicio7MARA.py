#Haz lo mismo que en el ejercicio anterior pero busca la primera vez que aparece la vocal “a” sin tener en cuenta tu nombre.

#Creamos la cadena
cadena="Miguel Angel Ruiz Aguilar"  
#Convertimos todas las letras a minuscula para facilitar la busqueda
cadena.lower()
#Aqui lo que hacemos esque empezamos a buscar despues de cada nombre en mi cado a partir del 12 caracter pero eso cambia.
primerA=cadena[12:].find("a")
#Y lo imprimimos
print(primerA)