diccionario={"nombre":"Juan","edad":18,"ciudad":"sevilla"}
diccionario2={"nickname":"perez"}

diccionario.update(diccionario2)
del(diccionario["ciudad"])

valores =diccionario.values()

print (valores)