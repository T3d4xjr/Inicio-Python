"""Crea una clase llamada Rectángulo que tenga los atributos ancho y alto. 
Además, crea una propiedad llamada área que calcule automáticamente el área del rectángulo."""
# Clase Rectangulo con propiedades de altura, ancho y área
class Rectangulo:
    
    # Inicializa altura y ancho
    def __init__(self, altura, ancho):
        self.altura = altura
        self.ancho = ancho
    
    # Propiedad que calcula el área
    @property
    def area(self):
        return self.ancho * self.altura


# Crear un rectángulo
rectangulo = Rectangulo(3, 3)

# Imprimir atributos y área
print("Esto es la altura: " + str(rectangulo.altura))
print("Esto es el ancho: " + str(rectangulo.ancho))
print("Esto es el área: " + str(rectangulo.area))
print("------------------")

# Cambiar altura y mostrar nueva área
rectangulo.altura = 4
print("Nueva altura: " + str(rectangulo.altura))
print("Esto es el área: " + str(rectangulo.area))
