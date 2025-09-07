#python

# pickle.load permite leer archivos binarios.

import pickle  #Biblioteca Necesaria para serializar

fichero=open("lista_nombres" , "rb")  # rb= read binary

lista=pickle.load(fichero)

print(lista)



