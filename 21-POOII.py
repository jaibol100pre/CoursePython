#Python
#Programación Orientada a Objeto "POO"
'''
Clase: Modelo donde se redactan las caracteristicas comunes de un grupo de objetos (Chacis, Ruedas, Parabrisas)
Objeto: Ejemplar que pertenecen a una clase, ejemplo la clase Coche, una clase es sinónimo de Ejemplar de Clase / Instancias / Objeto de clases. 
Modularización: 
Encapsulamiento /encapsulación
Herencia:
Poliformismo:
'''

##Sintaxis de una Clases
'''
class NameClass():
    Code 
'''
#Objetos
class Coche():
    #propiedades o propiedad
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    
    #metodo arrancar
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
    #metodo estado    
    def estado(self):
        print("El coche tiene: " , self.ruedas, "ruedas. un archo de: " , self.anchoChasis, "y un largo de " , self.largoChasis  )



miCoche=Coche() # <---- instancia de clase o ejemplarozar un clase
#NameObjeto.metodo
'''print( "Ancho: " ,  miCoche.largoChasis ) #Inprime el lago del chasis o sea la propiedad de la clase
print( "Largo: " ,  miCoche.anchoChasis ) 
print( "Ruedas:" ,  miCoche.ruedas ) 
'''
print(miCoche.arrancar(True))
miCoche.estado()

print ("------A continuación creamos un segundo objeto-----------")

miCoche2=Coche()
'''print( "Largo:" , miCoche2.largoChasis ) #Inprime el lago del chasis o sea la propiedad de la clase
print( "Ancho:" , miCoche2.anchoChasis ) 
print( "Ruedas:", miCoche2.ruedas ) 
'''

print(miCoche2.arrancar(False))
miCoche2.estado()