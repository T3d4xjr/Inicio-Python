# -*- coding: utf-8 -*- 
"""Crea un programa que tenga una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
Además deberá mostrar un menú con las siguientes opciones
1. Añadir contacto
2. Lista de contactos
3. Buscar contacto
4. Editar contacto
5. Cerrar agenda
"""
#Clase contacto que tiene los valores que la contienen y los muestra
class Contacto:

    def __init__(self,nombre,telefono,email):
        self.nombre=nombre
        self.telefono=telefono
        self.email=email

    def __str__(self):
        return f"Nombre: {self.nombre}, telefono: {self.telefono}, email: {self.email}"

#Clase agenda donde vamos a tener una lista y añadiremos valores con el formato ya definido en la clase Contacto.
class Agenda:

    def __init__(self):
        self.contactos =[]

    def AnadirContacto(self,nombre,telefono,email):
        
        self.contactos.append(Contacto(nombre,telefono,email))
        print("Añadido correctamente")

    def listarContactos(self):
        if not self.contactos:
            print("No hay contactos en la agenda.")
        else:
            for contacto in self.contactos:
                print(contacto)
    def buscarContacto(self,nombre):

        for contacto in self.contactos:
            if contacto.nombre.lower()==nombre.lower():
                print(contacto)
                return contacto
        print("Contacto no encontrado")
    def editarContacto(self, nombre):
        contacto = self.buscarContacto(nombre)
        if contacto:
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_telefono = input("Nuevo teléfono: ")
            nuevo_email = input("Nuevo email: ")
            contacto.nombre, contacto.telefono, contacto.email = nuevo_nombre, nuevo_telefono, nuevo_email
            print("Contacto actualizado correctamente.")

    def cerrarAgenda(self):
        print("Cerrando agenda...")
        exit()

# Menú principal
agenda = Agenda()
while True:
    print("Agenda de Contactos")
    print("1. Añadir contacto")
    print("2. Lista de contactos")
    print("3. Buscar contacto")
    print("4. Editar contacto")
    print("5. Cerrar agenda")
    
    opcion = input("Selecciona una opción: ")
    
    if opcion == "1":
        nombre = input("Nombre: ")
        telefono = input("Teléfono: ")
        email = input("Email: ")
        agenda.AnadirContacto(nombre, telefono, email)
    elif opcion == "2":
        agenda.listarContactos()
    elif opcion == "3":
        nombre = input("Nombre del contacto a buscar: ")
        agenda.buscarContacto(nombre)
    elif opcion == "4":
        nombre = input("Nombre del contacto a editar: ")
        agenda.editarContacto(nombre)
    elif opcion == "5":
        agenda.cerrarAgenda()
    else:
        print("Opción no válida, intenta de nuevo.")
    