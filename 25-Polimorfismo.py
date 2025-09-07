#Python
##Polimorfismo
class Coche():
    #metodo o comportamiento
    def desplazamiento (self):
        print("Me desplazo en 4 ruedas")
    #metodo o comportamiento
class Moto():
    def desplazamiento(self):
        print("Me desplazo utilizando 02 ruedas")
class Camion():
    #metodo o comportamiento
    def desplazamiento(self):
        print("Me desplazo utilizando 06 ruedas")
###Instancias##
miVehiculo=Moto()
miVehiculo.desplazamiento()     
miVehiculo2=Coche()
miVehiculo2.desplazamiento()
miVehiculo3=Camion()
miVehiculo3.desplazamiento()


##Aplicando poliformismo

def desplazamientoVehiculo(vehiculo):   #funcion (parametro)
    vehiculo.desplazamiento()

miMoto=Moto()
desplazamientoVehiculo(miMoto)

miCoche=Coche()
desplazamientoVehiculo(miCoche)

miCamion=Camion()
desplazamientoVehiculo(miCamion)