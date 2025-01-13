#Al diccionario anterior, añade una nueva clave que sea “Nickname” y añadele el valor correspondiente a tus datos. 
#Además, borra la clave ciudad  y luego muestra por pantalla los tres valores.

#Creamos de nuevo el diccionario con lo nuevo
diccionario={"nombre":"Juan","edad":18,"ciudad":"sevilla","nickname":"perez"}
#Borramos la clave pedida

del(diccionario["ciudad"])
#Cogemos los valores
valores =diccionario.values()
#Y los imrpimimos
print (valores)