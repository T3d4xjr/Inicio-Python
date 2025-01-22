"""Crea una clase llamada Estudiante con los atributos nombre y calificaciones. 
Implementa un método que sirva para calcular el promedio de las calificaciones."""

class Estudiante():
    
    def __init__(self,nombre,calificaciones):
        self.nombre=nombre
        self.calificaciones=calificaciones
    
    def promedio(self):
        
        promedioCalificaciones=sum(self.calificaciones)/len(self.calificaciones)

        print("El estudiante: "+str(self.nombre)+" tiene un promedio de: "+str(promedioCalificaciones))


estudiante=Estudiante("Pepe",[4,3,4,5,6,8])

estudiante.promedio()

