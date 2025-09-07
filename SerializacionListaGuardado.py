#python
'''
La SERIALIZACION
Conciste en guardar en un fichero externo un Objeto,coleccion o diccionario en código binario. 

Utilización  a) Compartir un fichero por internet; b) Almacenar en una Base de datos

Método dump(): Volcado de datos al fichero binario externo
Metodo load(): carga de los datos del fichero binario externo
pickle Biblioteca necesaria para poder serializar

pickle.dump permite escribir binarios
'''

import pickle  #Biblioteca Necesaria para serializar

lista_nombres=["Pedro", "Ana", "Maria", "Isabel"]


fichero_binario=open("lista_nombres" , "wb") #( listName , permisos)  #wb=writer binary    esto abre un archivo llamdo lista_nombres

#pickle.dump(ListName, FileName)
pickle.dump(lista_nombres,fichero_binario)

fichero_binario.close()

del (fichero_binario)

