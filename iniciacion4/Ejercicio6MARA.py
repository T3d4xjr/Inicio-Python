"""
Crea una clase llamada Animal con un método llamado hacer_sonido. 
A continuación, crea dos clases hijas llamadas Perro y Gato que 
sobreescriban el método anterior para imprimir los sonidos específicos de cada animal."""

# Clase base Animal
class Animal:
    def hacer_sonido(self):
        print("Qué sonido hará el animal")

# Clase Perro
class Perro(Animal):
    def hacer_sonido(self):
        print("El animal hizo guau, debe ser un perro")

# Clase Gato
class Gato(Animal):
    def hacer_sonido(self):
        print("El animal hizo miau, debe ser un gato")


# Instancias de las clases
animal = Animal()
perro = Perro()
gato = Gato()

# Llamada al método de la clase base
animal.hacer_sonido()

# Selección de animal
opcion = int(input("Qué animal será si pones un número entero entre el 1 o el 2: "))

if opcion == 1:
    perro.hacer_sonido()
elif opcion == 2:
    gato.hacer_sonido()
else:
    print("Opción no válida")