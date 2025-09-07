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
    def __init__(self):
        self.__largoChasis=250
        self.__anchoChasis=120  #Encapsulado "__"
        self.__ruedas=4    #se prcede de dos guiones bajos "__" para encapsular las propiedades, es decir, evitar que sean modificadas
        self.__enmarcha=False
    
    #metodo arrancar
    def arrancar(self,arrancamos):
        self.__enmarcha=arrancamos 
        if (self.__enmarcha):
            chequeo=self.__chequeo_interno()

        if (self.__enmarcha and chequeo):
            return "El coche está en marcha"
        elif (self.__enmarcha and chequeo==False):
            return "Algo ha ido mal en el chequeo, no podemos arrancar"
        else:
            return "El coche está parado"
        
    #metodo estado    
    def estado(self):
        print("El coche tiene: " , self.__ruedas, "ruedas. un archo de: " , self.__anchoChasis, "y un largo de " , self.__largoChasis  )

    #metodo chequeo

    def __chequeo_interno (self):
        print ("Realizando chequeo")
        self.gasolina="Ok"
        self.aceite="Ok"
        self.puertas="Cerradas"   

        if (self.gasolina=="Ok" and self.aceite=="Ok" and self.puertas=="Cerradas"):
            return True
        else:
            return False

##print ("------A continuación creamos nuestro primer objeto-----------")

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
miCoche2.__ruedas=2 # <----- No se modifica el  valor de la propiedad porque ha sido encapsulado "___" en el constructor
miCoche2.estado()