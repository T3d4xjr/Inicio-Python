# Crea una cadena que contenga tu nombre y apellidos y devuelve por pantalla cuántas veces tiene la vocal “a”.

#Creamos la cadena
cadena="Miguel Angel Ruiz Aguilar"
#Convertimos todas las letras a minuscula para facilitar la busqueda
minuscula=cadena.lower()
#Vemos cuantas veces sale la a
contarVeces=minuscula.count("a",0)
#Y lo imprimimos
print(contarVeces)