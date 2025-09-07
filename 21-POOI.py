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
    Pass 
'''
#Clase
class Coche():
    #Propiedades o propiedad (similar a una variable)
    largoChasis=250
    anchoChasis=120
    ruedas=4
    enmarcha=False
    #Sintaxis de un Metodo
    '''
    def NombreMetodo(self):
        pass
    '''
    def arrancar(self): #Metodo o comportamiento son funciones que pertenecen a una clase
        #self.NombrePropiedad
        self.enmarcha=True    #Self hace referencia al objeto o instancia y se puede ver como un parámetro que recibe un método, siempre precede a una propiedad

    def estado(self):   #Metodo o comportamiento son funciones que pertenecen a una clase
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
    #comportamiento
    #metodo es una función especial que pertenece a una clase
    '''
    def NameFunction(self):  #Self hace referencia al propio objeto perteneciente  a la clase, es decir, a la instancia
        pass
    '''

#Sintaxis de un Objeto / Instancia
'''
NombreObjeto=NombreClase()
'''
miCoche=Coche() # <---- instancia de clase / ejemplar de clase /  Objeto

#NombreObjeto.Propiedad 
print( miCoche.largoChasis ) #Inprime el lago del chasis o sea la propiedad de la clase
print( miCoche.anchoChasis ) 
print( miCoche.ruedas ) 

#Sintaxis:
'''
  Objeto.NombreComportamiento() o NombreObjeto.Metodo()
'''

miCoche.arrancar() #<-----------Lo arrancamos es decir devuelve True en self.enmarcha

print( miCoche.estado() ) #<-----Devuelve True porque lo arrancamos.


Camion=Coche()
Camion.ruedas=8 #<----- Se modifica porque no hemos encapsulado
print( Camion.ruedas )

print( Camion.estado() ) #<-----Devuelve False porque no lo arrancamos.
