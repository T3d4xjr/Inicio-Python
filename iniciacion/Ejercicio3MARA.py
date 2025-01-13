#Crea una cadena que sea “Sistemas de Gestión Empresarial”. Imprime lo siguiente por pantalla:
#a.Sólo la primera palabra
#b.Sólo la segunda palabra
#c.Pasa todo el texto a mayúscula e imprímelo
#d.Quita los espacios en blanco del texto e imprímelo
#e.Imprime la longitud de cada uno de los apartados anteriores.

#Creamos la cadena
cadena ="Sistemas de Gestión Empresarial"
#Aqui hacemos cada paso esta asociado a la letra corespondiente.
a=cadena[0]
b=cadena[1]
c=cadena.upper()
d=cadena.replace(" ","")
e=len(cadena)
#Imprimimos los resultados
print(a)
print(b)
print(c)
print(d)
print(e)

