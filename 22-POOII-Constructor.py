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
   
    #CONSTRUCTOR   define los estados iniciales (default)

    #Sintaxis de un método constructor:
    '''
    def __init__(self):
       self.propiedad1=Valor
       self.propiedad2=Valor
       self.propiedad3=Valor
    
    '''
    def __init__(self):
        #Propiedades
        self.largoChasis=250
        self.__anchoChasis=120  #Encapsulado prcediendo la propiedad con dos guiones "__", esto evita que sea accesible des de fuera del método
        self.__ruedas=4    #se prcede de dos guiones bajos "__" para encapsular las propiedades, es decir, evitar que sean modificadas
        self.enmarcha=False
    
    #metodo arrancar
    def arrancar(self,arrancamos):
        self.enmarcha=arrancamos
        if (self.enmarcha):
            return "El coche está en marcha"
        else:
            return "El coche está parado"
        
    #metodo estado    
    def estado(self):
        print("El coche tiene: " , self.__ruedas, "ruedas. un archo de: " , self.__anchoChasis, "y un largo de " , self.largoChasis  )


print ("------A continuación creamos nuestro primer objeto-----------")

miCoche=Coche() # <---- instancia de clase o ejemplarozar un clase
#NameObjeto.metodo
'''print( "Ancho: " ,  miCoche.largoChasis ) #Inprime el lago del chasis o sea la propiedad de la clase
print( "Largo: " ,  miCoche.anchoChasis ) 
print( "Ruedas:" ,  miCoche.ruedas ) 
'''
print(miCoche.arrancar(True))
miCoche.estado()

print ("------A continuación creamos un segundo objeto / instancia o ejemplar-----------")

miCoche2=Coche()
'''print( "Largo:" , miCoche2.largoChasis ) #Inprime el lago del chasis o sea la propiedad de la clase
print( "Ancho:" , miCoche2.anchoChasis ) 
print( "Ruedas:", miCoche2.ruedas ) 
'''

print(miCoche2.arrancar(False))
miCoche2.__ruedas=2 # <----- No se modifica el  valor de la propiedad porque ha sido encapsulado "___" en el constructor
miCoche2.estado()