#Crea una lista de 10 números. Una vez creada, extrae los primeros 3 números y los últimos 3 números y muestra ambos resultados por pantalla.
lista=[1,2,3,4,5,6,7,8,9,10]
#Extraemos los 3 primeros
primerosNumeros =lista[:3]
#Extraemos los 3 ultimos
ultimosNumeros=lista[7:]
#Y los mostramos 
print(primerosNumeros +ultimosNumeros)