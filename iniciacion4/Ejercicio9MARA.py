"""Crea una clase llamada Libro y una clase llamada Biblioteca. 
La clase Biblioteca debe permitir agregar libros, 
eliminarlos y mostrar un listado de todos los libros. 
Ten en cuenta que cada libro deberá tener dos atributos llamados titulo y autor."""

# Clase Libro con atributos título y autor
class Libro():
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

# Clase Biblioteca que hereda de Libro, gestiona libros
class Biblioteca(Libro):
    def agregar(self):  # Agrega un libro a la lista
        tituloLibro = str(input("Di el título del libro: "))
        self.titulo.append(tituloLibro)
        autorLibro = str(input("Di el autor del libro: "))
        self.autor.append(autorLibro)

    def quitar(self):  # Retira un libro de la lista
        tituloRetirar = str(input("Retira este título: "))
        indice = self.titulo.index(tituloRetirar)
        self.titulo.pop(indice)
        self.autor.pop(indice)

    def mostrar(self):  # Muestra todos los libros y autores
        print("Libros: " + str(self.titulo) + " Autores: " + str(self.autor))

# Instanciación de libro y biblioteca, y menú de opciones
libro = Libro([], [])
biblioteca = Biblioteca(libro.titulo, libro.autor)

print("Menú:")
print("1. Agregar libro")
print("2. Retirar libro")
print("3. Mostrar libros")
print("4. Salir")

while True:
    opcion = int(input("Elige una opción: "))
    if opcion == 1:
        biblioteca.agregar()
    elif opcion == 2:
        biblioteca.quitar()
    elif opcion == 3:
        biblioteca.mostrar()
    elif opcion == 4:
        print("Saliendo")
        break
    else:
        print("Opción no válida")
