#Clase Persona
class Persona():
    #Constructor:
    def __init__(self, primer_nombre, primer_apellido,  cedula):
        self.nombre=primer_nombre
        self.apellido=primer_apellido
        self.cedula=cedula
    #Método
    def descripcion (self):
        print("Primer_nombre: ", self.nombre, "Primer_apellido: " , self.apellido , "Cédula: " , self.cedula )

#Instancia/Objeto
Persona1=Persona("Pedro", "Garcias", 11252125)
print(Persona1.nombre)
print(Persona1.apellido)
print(Persona1.cedula)
Persona1.descripcion() 

#Clase Alumno (Hereda de la clase Persona)
class Alumno(Persona):
    #Constructor
    def __init__(self, tipo, edad, grado, nombre_alumno, apellido_alumno, cedula_alumno):
         #Llamada a constructor de la clase padre
         super().__init__(nombre_alumno, apellido_alumno, cedula_alumno) 
         self.tipo=tipo
         self.edad=edad
         self.grado=grado 
    #Método
    def descripcion(self): #Reescribiendo el método descripción
        super().descripcion() #llamo el método descripción de la clase padre
        print( "Tipo: " , self.tipo ,  "Edad: ", self.edad , "Grado: " , self.grado)

 #Instancia/Objeto   
Alumno1=Alumno( "Alumno", "22", "6to Grado" , "Julio", "Perez" , 10252525 )
Alumno1.descripcion() #Se hace referencia al método descripción de la clase Alumno (hija)

##Para saber si pertenece una Instancia a una Clase  "ISISTANCE"
if isinstance (Alumno1,Persona):
    print ("Alumno1 pertenece a la Clase Persona")
elif isinstance (Alumno1,Alumno ):
    print ("Alumno1 pertenece a la Clase Alumno")
elif isinstance (Alumno1,Alumno ) and isinstance (Alumno1,Persona):
    print ("Alumno1 Si pertenece a ambas Clases")
else:
    print("Alumno1 No pertenece a ninguna de las clase")

if isinstance   (Persona1,Alumno):
    print ("Persona1 Si pertenece a la Clase Alumno")  
elif isinstance (Persona1,Persona):
    print ("Persona1 Si pertenece a la clase Persona")
elif isinstance (Persona1,Alumno) and isinstance (Persona1,Persona):
    print ("Paersona1 Si pertenece a ambas Clases")
else:
    print("Persona1  No pertenece a ninguna de las clases")