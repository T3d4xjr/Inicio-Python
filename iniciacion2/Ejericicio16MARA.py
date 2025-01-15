#Escribir un programa que pida al usuario 4 palabras y las muestre ordenadas alfabéticamente,
# separadas por comas, por pantalla

lista=[]
for i in range(4):

    lista.append(str(input("Introduzca unas palabras :")))
      
lista.sort()
print(",".join(lista))