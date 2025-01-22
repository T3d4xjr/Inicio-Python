"""Crea una clase llamada Producto con los atributos nombre, precio y cantidad. 
Además, implementa los métodos para agregar o quitar existencias 
y para mostrar información del producto. 
En cada método se debería mostrar por pantalla la acción hecha en el producto."""
# Definición de la clase Vehiculo
class Vehiculo:
    def __init__(self):
        # Inicialización de atributos
        self.cantidad_total = 0  # Atributo para contar los vehículos
        self.color = input("Inserte un color de coche: ")
        self.marca = input("Inserte una marca de coche: ")
        self.deposito = input("Inserte un depósito de coche: ")

    # Método para verificar atributos y contar vehículos creados
    def contadorVehiculos(self):
        if self.color == "":  # Validación del color
            print("Debes introducir un color")
        elif self.marca == "":  # Validación de la marca
            print("Debes introducir una marca")
        elif self.deposito != "Gasolina":  # Validación del depósito
            print("Ese depósito no está en nuestro sistema")
        else:  # Incrementar el contador si todo es válido
            self.cantidad_total += 1
            print("Se ha creado un coche de color: " + str(self.color) +
                  " con la marca: " + str(self.marca) +
                  " de depósito: " + str(self.deposito) +
                  ". Cantidad de coches actuales creados: " + str(self.cantidad_total))


# Creación de una instancia del vehículo y opciones del menú
coche = Vehiculo()

print("1. Añadir coche al concesionario")
print("2. Salir")

# Bucle principal para interactuar con el programa
while True:
    opcion = input("Elige una opción: ")

    if opcion == "1":  # Llamada al método para añadir un vehículo
        coche.contadorVehiculos()
    elif opcion == "2":  # Salir del programa
        break