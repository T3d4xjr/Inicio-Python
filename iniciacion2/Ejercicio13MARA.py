#Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango,
#  que sean bisiestos y múltiplos de 10. Nota: para que un año sea bisiesto debe ser divisible por 4 y
#  no debe ser divisible por 100, excepto que también sea divisible por 400.
numero = int(input("Introduce un año: "))

numero2 = int(input("Introduce otro año: "))

for i in range(numero,numero2):
    if i  % 4 == 0 and i  % 100 !=0 or i % 400 ==0:
        print(i)
        print("Es primo")
        if i % 10 == 0:
            print(i)
            print("Es multiplo de 10")
        else:
            print(i)
            print("No es multiplo de 10")
    else:
        print(i)
        print("No es primo")
        if i % 10 == 0:
            print(i)
            print("Es multiplo de 10")
        else:
            print(i)
            print("No es multiplo de 10")