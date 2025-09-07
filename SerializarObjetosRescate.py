#python

import pickle  #Biblioteca Necesaria para serializar
import SerializarObjetosGuardado

###Abrir o Leer

ficheroApertura=open("losCohes", "rb")

misCoches=pickle.load(ficheroApertura)

for c in misCoches:
    print(c.estado())