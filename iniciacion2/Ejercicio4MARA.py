#Escribir un programa que imprima la sumatoria de todos los múltiplos de 3 encontrados entre el 0 y el 100.
#Iniciamos una variable que va a ser la que imprimimos con el sumatorio
total = 0

#Este bucle esta hecho para que entre el 0 y el 100 y sea multiplos de 3 y lo metemos en una variable
for a in range(0,101,3):
    total=total+a
print(total)