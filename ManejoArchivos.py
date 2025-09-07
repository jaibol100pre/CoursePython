#Python
#Fase
from io import open

#Escribir en un archivo
'''
archivo_texto=open("archivo.txt" , "w")
frase="Estupendo día para estudiar Python •\n el miercoles"
archivo_texto.write(frase)
archivo_texto.close()
'''

#Leer un archivo
'''
archivo_texto=open("archivo.txt" , "r")
texto=archivo_texto.read()
print(texto)
archivo_texto.close()
'''
##Guardar la información del archivo en una lista
'''
archivo_texto=open("archivo.txt" , "r")
lineas_texto=archivo_texto.readlines() #Guarda las lńeas en una lista
type(lineas_texto)
archivo_texto.close()
#Indexar la información desde una posición en la lista
#print(lineas_texto[0]) #Para acceder a la primera línea
'''

#Leer la información con el bucle for
'''
for a in lineas_texto:
    print (a)

'''

#"Agregar Información"

''' 
archivo_texto=open("archivo.txt" , "a")
archivo_texto.write("\n siempre es bueno estudiar")
'''


'''
archivo_texto=open("archivo.txt" , "r")
archivo_texto.seek(11) #posiciona el puntero en la posicion 11
archivo_texto.seek(0) #posiciona el puntero en la ultima posición
'''

#print(archivo_texto.read(10)) #lee desde la psición 0 hasta la 10
#print(archivo_texto.read(15)) #lee los primero 15 caracteres
#archivo_texto.seek(len(archivo_texto.read())/2)

'''
archivo_texto=open("archivo.txt" , "r")
archivo_texto.seek(len(archivo_texto.readline()))
print(archivo_texto.read())
'''
'''
archivo_texto=open("archivo.txt" , "r+") #Lectura y escritura
archivo_texto.write("\n Estoy deseoso de aprender a programar") #Sustitye la primera línea eliminando lo que ya exista
'''

archivo_texto=open("archivo.txt" , "r+") #Lectura y escritura

#print(archivo_texto.readlines())

lista_texto=archivo_texto.readlines()
lista_texto[2]="Esta línea ha sido incluida desde el exterior"
archivo_texto.writelines(lista_texto)
archivo_texto.close()