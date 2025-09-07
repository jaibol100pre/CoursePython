#Python
#Generadores de Python

#sintaxis:
'''
def NameFunction():
    code 
    yield 
'''

##Función Tradicional
def genera_numeros_pares (limite):
    num=1
    miLista=[]
    while num < limite:
        miLista.append(num*2)
        num=num+1
    return miLista
miLista=genera_numeros_pares (10)
print(miLista)

##Generador###


############
## YIELD ###
############




def genera_pares (limite):
    num=1
    while num < limite:
        yield num*2
        num=num+1
misPares=genera_pares (10)
for i in misPares:
 print(i, end='-')

#Los generadores estan pensado en el uso de funciones que se hacen iterativas y devuelven un conjunto de valores
#yield sustituye return 

def generaPares(limite):
    num=1
    while num<limite:
      yield num * 2    #a diferencia de return que devuelve un único valor la expresion yield devuelve un conjunto de valores
      num=num+1

##El ejemplo anterior demuestra que los valores a pesar que se almacen en una variable solo estan disponible si el código generador es consultado
##EN UNA FUNCIÓN tradicional se habría almacenado en una variable todo el conjunto de calores 
devuelvePares=genera_pares(10)
print(next(devuelvePares)) #imprime 4
print("Aquí podría ir más código") 
print(next(devuelvePares)) #imprime 6
print("Aquí podría ir más código") 
print(next(devuelvePares)) #imprime 4
print("Aquí podría ir más código")
print(next(devuelvePares)) #imprime 8


#yield from Utilizaremos esta expresión con funciones generadora anidadas, como por ejemplo, bucle anidados (for dentro de otro for)

def devuelve_ciudades(*ciudades): #-- el asterisco "*"" significa que recibierá un número x de elementos
   for elemento in ciudades:
      yield elemento

ciudades_devueltas=devuelve_ciudades("Caracas", "Charallave", "Barinas", "Vargas")

print(next(ciudades_devueltas)) #Devuelve el primer elemento  (ciudad)
print(next(ciudades_devueltas)) #Devuelve el segundo elemento (ciudad)



def devuelve_ciudades(*ciudades): #-- el asterisco "*"" significa que recibierá un número x de elementos
   for elemento in ciudades:
       for subElemento in elemento:   #Este Bucle for anidado recorre cada elemento y devuelve sus sub-elementos 
          yield subElemento

ciudades_devueltas=devuelve_ciudades("Caracas", "Charallave", "Barinas", "Vargas")

print(next(ciudades_devueltas)) #devuelve el primer sub-elemento (letras)
print(next(ciudades_devueltas)) #devuelve el segundo sub-elemento (letras)



###############
##YIELD FROM###
###############

'''
La función yield from  permite prescindir del bucle anidado, en cierto modo, "yield from" permite hacer un yiled desde el primer elemento 
'''

def devuelve_ciudades(*ciudades): #-- el asterisco "*"" significa que recibierá un número x de elementos
   for elemento in ciudades:
       ##for subElemento in elemento:   #Este Bucle for anidado recorre cada elemento y devuelve sus sub-elementos 
          yield from elemento

ciudades_devueltas=devuelve_ciudades("Caracas", "Charallave", "Barinas", "Vargas")

print(next(ciudades_devueltas)) #devuelve el primer sub-elemento (letras)
print(next(ciudades_devueltas)) #devuelve el segundo sub-elemento (letras)
