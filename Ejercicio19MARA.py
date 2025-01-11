#Crea una tupla con tres elementos cualesquiera. 
# Luego, usa estos valores para crear un diccionario donde la primera clave será el primer elemento de la tupla y cuyo valor será el segundo elemento. 
# La segunda clave será el tercer elemento de la tupla y el valor será el que tú quieras. Imprime este diccionario por pantalla.

#Creamos una tupla.
tupla=("Cantidad",2,"mochila")
#Creamos un diccionario utilizando los datos de la tupla
diccionario ={tupla[0]:tupla[1],tupla[2]:"grande"}
#Y lo imprimimos
print(diccionario)