#Crea una cadena que contenga tu nombre y apellidos y devuelve por pantalla en qué posición aparece por primera vez la vocal “a”.

#Creamos la cadena
cadena="Miguel Angel Ruiz Aguilar"  
#Convertimos todas las letras a minuscula para facilitar la busqueda
minuscula=cadena.lower()
#Buscamos la posicion que sale la letra a
primerA=minuscula.find("a")
#Y la imprimimos
print(primerA)