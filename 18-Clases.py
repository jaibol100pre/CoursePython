#Tuplas en Python
#Autor: Jaibol
#Clases18.py 18     
#Clases en python   

class Persona:  #define la clase
    def __init__(self, nombre,apellido): #Constructor
        self.nombre = nombre
        self.apellido = apellido

    def saludar(self): #Instancia Actual
        print(f"Hola nombre es: {self.nombre} y mi apellido es {self.apellido}")


#instancia de la clase    
persona1=Persona("Jaibol", 'Santaella')
persona1.saludar()

persona2=Persona("Gilbert", 'Santaella')
persona2.saludar()

