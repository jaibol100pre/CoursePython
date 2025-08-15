#Listas en Python
#Autor: Jaibol
#Clases06.py 06
#Una lista es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos de datos.
#Se definen usando corchetes [] y los elementos se separan por comas.
#Crear una lista
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
a,b,c = 0, 1, 2
print(' ')
print(a) #Imprime 0
print(' ')
print(b) #Imprime 1
print(' ')
print(c) #Imprime 2
print(' ')
while a < 10:
    print(a)
    a, b = b, a+b
