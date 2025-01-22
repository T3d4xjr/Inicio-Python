"""Crea una clase base llamada Vehiculo que tenga dos atributos llamados marca y modelo.
 Además, esta clase debe tener un método que muestre información del vehículo.
Después, crea dos clases derivadas llamadas Coche y Moto.
 Cada una de estas clases deben de tener un atributo adicional 
 específico y un método adicional específico para el tipo de vehículo.
	Prueba la clase creada con un ejemplo.
"""

# Clase Vehiculo que almacena la marca y modelo de un vehículo
class Vehiculo():
    
    # Inicializa marca y modelo
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    # Método para mostrar información del vehículo
    def mostrarInformacion(self):
        print("La marca de vehículo es: " + self.marca + " con modelo: " + self.modelo)

# Clase Coche que hereda de Vehiculo y tiene un atributo de depósito
class Coche(Vehiculo):
    
    # Inicializa el depósito del coche
    def __init__(self, deposito):
        self.deposito = deposito

    # Método para mostrar información específica del coche
    def mostrarCoche(self):
        print("El coche de marca: " + str(vehiculo.marca) + " tiene el depósito de tipo: " + str(self.deposito))

# Clase Moto que hereda de Vehiculo y tiene un atributo de depósito
class Moto(Vehiculo):
    
    # Inicializa el depósito de la moto
    def __init__(self, deposito):
        self.deposito = deposito

    # Método para mostrar información específica de la moto
    def mostrarMoto(self):
        print("La moto de marca: " + str(vehiculo.marca) + " tiene el depósito de tipo: " + str(self.deposito))

# Crear un objeto de la clase Vehiculo
vehiculo = Vehiculo("Audi", "coche")
# Crear objetos de la clase Coche y Moto
coche = Coche("Diesel")
moto = Moto("Gasolina")

# Mostrar información básica del vehículo
vehiculo.mostrarInformacion()

# Mostrar información específica del coche si el modelo es 'coche'
if vehiculo.modelo == "coche":
    coche.mostrarCoche()

# Cambiar el modelo del vehículo a 'moto'
vehiculo.modelo = "moto"
# Mostrar información específica de la moto si el modelo es 'moto'
vehiculo.mostrarInformacion()
if vehiculo.modelo == "moto":
    moto.mostrarMoto()
