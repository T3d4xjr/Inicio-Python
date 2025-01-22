# -*- coding: utf-8 -*-
"""
Clase CuentaBancaria que gestiona saldo mediante métodos para depositar, retirar y consultar.
"""

# Definición de la clase CuentaBancaria
class CuentaBancaria:
    # Constructor para inicializar atributos
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar dinero
    def depositar(self):
        dineroDepositado = int(input("Dime el dinero a introducir: "))
        if dineroDepositado < 0:
            print("No se pueden depositar cantidades negativas")
        else:
            self.saldo += dineroDepositado
            print(f"Titular: {self.titular} ha ingresado {dineroDepositado}€; saldo actual: {self.saldo}€")

    # Método para retirar dinero
    def retirar(self):
        dineroRetirado = int(input("Dime el dinero a retirar: "))
        if dineroRetirado < 0:
            print("No se pueden retirar cantidades negativas")
        elif dineroRetirado > self.saldo:
            print("No se puede retirar una cantidad mayor a tu saldo")
        else:
            self.saldo -= dineroRetirado
            print(f"Titular: {self.titular} ha retirado {dineroRetirado}€; saldo actual: {self.saldo}€")

    # Método para consultar el saldo
    def consultar(self):
        print(f"Titular: {self.titular} saldo actual: {self.saldo}€")


# Creación de una instancia y menú principal
persona = CuentaBancaria("Persona", 0)

print("Menú:")
print("1. Depositar")
print("2. Retirar")
print("3. Consultar saldo")
print("4. Salir")

# Bucle principal para interactuar con el menú
while True:
    opcion = input("Elige una opción: ")

    if opcion == "1":
        persona.depositar()
    elif opcion == "2":
        persona.retirar()
    elif opcion == "3":
        persona.consultar()
    elif opcion == "4":  # Salida del programa
        print("Gracias por usar nuestros servicios. ¡Hasta luego!")
        break
    else:
        print("Opción no válida.")
