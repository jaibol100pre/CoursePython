#Python
#Programación Orientada a Objeto "POO"
'''
Herencia: transferir comportamiento de una super clase o clase padre a una subclase

'''

##Sintaxis de una Clases

#SuperClase
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

class Furgoneta(Vehiculos):

    def carga(self, cargar):
        self.cargado=cargar
        if (self.cargado):
            return "La furgoneta está cargada"
        else:
            return "La furgoneta no está cargada"

##Herencia
#class NameClass(NameSuperClass)
class Moto(Vehiculos): ##Hereda todo los comportamientos de la clase Vehiculo
    ##Compotamiento propios
    hcaballito=""
    def caballito(self):  #metodo o comportamiento
       self.hcaballito="Voy haciendo caballito"
    #Sobreescribiendo la clase,   agrego un método con el mismo nombre y agrego propiedades adicionales.  
    def estado(self):
        print ("Marca: " , self.marca, "\nModelo: ", self.modelo, "\nEn marcha: " , self.enmarcha, "\nAcelerando: " , self.acelera, "\nFrenando: ", self.frena, self.hcaballito, "\n" , self.hcaballito )  

class VElectricos(): 
    def __init__(self): 
        self.autonomia=100
    
    def cargarEnergia(self): #metodo o comportamiento
        self.cargando=True


###Herencia Múltiples###
class BicicletaElectrica(VElectricos,Vehiculos):  #Hereda de dos clases, pero el constructor que reconoce es el de la primera clases que se menciona (VElectricos)
    pass

miBici=BicicletaElectrica()
    
