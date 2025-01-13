#Escribir un programa que pida al usuario un número entero positivo y 
# muestre por pantalla la cuenta atrás desde ese número hasta cero separados todo en una misma línea por comas
try:
    numeroIntroducido =int(input("Pon un numero positivo: "))
    #Recorremos ese numero
    for numeros in range(0,numeroIntroducido,1):
        
        print(numeros)
        #Mostramos un error en caso de lo que el usuario no ha dado no sea un numero
        
except ValueError:
    print("Debes introducir un numero") 