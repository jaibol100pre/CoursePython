#Listas en Python
#Autor: Jaibol
#Clases05.py 05
#Una lista es una colección ordenada y mutable de elementos, que pueden ser de diferentes tipos de datos.
#Se definen usando corchetes [] y los elementos se separan por comas.
#Crear una lista vacía
mylist=list()
print(type(mylist))
print(len(mylist))  # Añadido para mostrar la longitud de la lista vacía
myotherlist=list([1,2,3,4,5])
print(type(myotherlist))
print(len(myotherlist))
print(myotherlist[0])  # Añadido para mostrar el primer elemento de la lista
print(myotherlist[3:5])  # Añadido para mostrar el segundo elemento de la lista
mi_lista = [1, 2, 3, 'cuatro', 'cinco', True, 3.14]
print('Mi lista:', mi_lista)  # Añadido para mostrar la lista completa
print('')  # Añadido para mantener el formato de salida limpio
#Acceder a los elementos de una lista por su índice (comienza en 0)
print('Primer elemento:', mi_lista[0])  # Añadido para mostrar el primer elemento
print('Segundo elemento:', mi_lista[1])  # Añadido para mostrar el segundo elemento
print('Último elemento:', mi_lista[-1])  # Añadido para mostrar el último elemento
print('')  # Añadido para mantener el formato de salida limpio
misDatos=['Jaibol', 44, 'Python', True, 3.14]
nombre=misDatos[0] #Añadido para mostrar la lista completa de datos
edad=misDatos[1]#adido para mostrar la lista completa de datos
lenguaje=misDatos[2]#Añadido para mostrar la lista completa de datos
edo_civil=misDatos[3]#Añadido para mostrar la lista completa de datos
pi=misDatos[4]#Añadido para mostrar la lista completa de datos
print('Nombre:', nombre)  # Añadido para mostrar el nombre
print('Edad:', edad)  # Añadido para mostrar la edad        
print('Lenguaje:', lenguaje)  # Añadido para mostrar el lenguaje
print('Estado Civil:', edo_civil)  # Añadido para mostrar el estado civil
print('Pi:', pi)  # Añadido para mostrar el valor de Pi
nombre, edad, lenguaje, edo_civil, pi = misDatos  # Asignación múltiple de variables
print('Nombre:', nombre)  # Añadido para mostrar el nombre
print('Edad:', edad)  # Añadido para mostrar la edad
print('Lenguaje:', lenguaje)  # Añadido para mostrar el lenguaje
print('Estado Civil:', edo_civil)  # Añadido para mostrar el estado civil
myotherlist=list([1,2,3,4,5])
myotherlist.count(1)  # Añadido para contar cuántas veces aparece el número 1 en la lista
print('El número 1 aparece', myotherlist.count(1), 'veces en la lista')  # Añadido para mostrar el resultado del conteo
#Modificar un elemento de la lista
mi_lista[3] = 'cuatro_modificado'
print('Lista después de modificar el cuarto elemento:', mi_lista)  # Añadido para mostrar la lista modificada
print('')  # Añadido para mantener el formato de salida limpio
#Agregar un elemento al final de la lista
mi_lista.append('nuevo_elemento')
print('Lista después de agregar un nuevo elemento:', mi_lista)  # Añadido para          mostrar la lista después de agregar un elemento
print('')  # Añadido para mantener el formato de salida limpio
#Eliminar un elemento de la lista por su valor
mi_lista.remove(2)
print('Lista después de eliminar el elemento 2:', mi_lista)  # Añadido para mostrar la lista después de eliminar un elemento
print('')  # Añadido para mantener el formato de salida limpio
#Recorrer una lista con un bucle for
print('Recorriendo la lista:')



fruits = ['banana', 'orange', 'mango', 'lemon']
fruits.insert(2, 'apple') # insert apple between orange and mango
print(fruits)           # ['banana', 'orange', 'apple', 'mango', 'lemon']
fruits.insert(3, 'lime')   # ['banana', 'orange', 'apple', 'lime', 'mango', 'lemon']
print(fruits)  

fruits.remove('banana')
print(fruits)  


fruits.pop()  # Elimina el elemento  la la última posición (lemon)
print(fruits)  # Añadido para mostrar la lista después de eliminar el último elemento
print('')  # Añadido para mantener el formato de salida limpio


fruits.pop(1)  # Elimina el elemento en el índice 1 (orange)
print(fruits)  # Añadido para mostrar la lista después de eliminar el elemento en el índice 1
print('')  # Añadido para mantener el formato de salida limpio


fruits_copy = fruits.copy()  # Crea una copia de la lista
print('Copia de la lista:', fruits_copy)  # Añadido para mostrar la


fruits.reverse()  # Invierte el orden de los elementos en la lista
print('Lista después de invertir el orden:', fruits)  # Añadido para mostrar la lista después de invertir el orden
print('')  # Añadido para mantener el formato de


fruits.sort()  # Ordena los elementos de la lista en orden ascendente
print('Lista después de ordenar:', fruits)  # Añadido para mostrar la lista después de ordenar
print('')  # Añadido para mantener el formato de salida limpio




for elemento in mi_lista:   
    print(elemento)  # Añadido para mostrar cada elemento de la lista en una nueva línea
    
# El parámetro end='-' se usa para imprimir los elementos en una sola línea separados por guiones

a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
print('')  # Añadido para finalizar la línea después de imprimir la serie de Fibonacci


