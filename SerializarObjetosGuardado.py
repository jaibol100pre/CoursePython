#python

import pickle  #Biblioteca Necesaria para serializar


class Vehiculos:

    #Constructor
    def __init__(self, marca, modelo):
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
    #Metodos o comportamiento
    def arrancar(self):
        self.enmarcha=True
    def acelerar(self):
        self.acelera=True
    def frenar(self):
        self.frena=True
    def estado(self):
        print ("Marca: " , self.marca, "\nModelo: ", self.modelo, "\nEn marcha: " , self.enmarcha, "\nAcelerando: " , self.acelera, "\nFrenando: ", self.frena)  

coche1=Vehiculos("Ferrary" , "MXG")

coche2=Vehiculos("Toyota" , "Hilux")

coche3=Vehiculos("Ford" , "Fiesta")

coches=[coche1,coche2,coche3]

##Guardar

fichero=open("losCohes", "wb")  #Genera un archivo binario con el nombre los coches, en su interior los objetos

pickle.dump(coches,fichero) #pickle.dump(ObjetName, FileName)

fichero.close()

del (fichero)

