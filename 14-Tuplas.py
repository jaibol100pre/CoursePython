#Tuplas en Python
#Autor: Jaibol
#Clases14.py 14     
#Una tupla es una colección ordenada e inmutable de elementos, que pueden ser de diferentes tipos de datos.
#Se definen usando paréntesis () y los elementos se separan por comas.
my_tuple = tuple()
my_other_tuple = ()
my_other_tuple = ('uno', 'dos', 'dos','tres', 4, 5, True)
print(type(my_tuple))  # Añadido para mostrar el tipo de dato de la variable 'my_tuple'
print(type(my_other_tuple))  # Añadido para mostrar el tipo de dato de la variable 'my_other_tuple'
print(len(my_other_tuple))  # Añadido para mostrar la longitud de la tupla      
print(my_other_tuple[0])  # Añadido para mostrar el primer elemento de la tupla
print(my_other_tuple[3:5])  # Añadido para mostrar los elementos desde el índice 3 al 4 de la tupla     
print(my_other_tuple.count('dos'))  # Añadido para contar cuántas veces aparece 'dos' en la tupla
print(my_other_tuple.index(4))  # Añadido para encontrar el índice del primer elemento que es igual a 4 en la tupla
print(my_other_tuple.index('tres'))  # Añadido para encontrar el índice del primer elemento que es igual a 'tres' en la tupla
print(my_other_tuple.index(True))  # Añadido para encontrar el índice del primer elemento que es igual a True en la tupla
my_tree_tuple=my_other_tuple  # Añadido para asignar 'my_other_tuple' a 'my_tree_tuple'
print(my_tree_tuple)  # Añadido para mostrar el contenido de 'my_tree_tuple
my_for_tuple=my_other_tuple+my_tree_tuple  # Añadido para concatenar 'my_other_tuple' y 'my_tree_tuple'
print(my_for_tuple)  # Añadido para mostrar el contenido de 'my_for_tuple
del my_other_tuple  # Añadido para eliminar 'my_other_tuple'
#print(my_other_tuple)  # Añadido para mostrar un error al intentar acceder a 'my_other_tuple' después de eliminarla
#print(my_other_tuple)  # Añadido para mostrar el contenido de 'my_for_tuple' después de eliminar 'my_other_tuple'
#my_other_tuple.remove('dos')  # Añadido para eliminar la primera aparición de 'dos' en 'my_other_tuple'
#print(my_other_tuple)  # Añadido para mostrar el contenido de 'my_other_tuple' después de eliminar 'dos'
# my_other_tuple.clear()  # Añadido para limpiar 'my_other_tuple', pero esto generará un error porque las tuplas son inmutables     
# my_other_tuple.append('nuevo_elemento')  # Añadido para agregar un nuevo elemento a 'my_other_tuple', pero esto generará un error porque las tuplas son inmutables
# my_other_tuple.remove('dos')  # Añadido para eliminar 'dos' de 'my_other_tuple', pero esto generará un error porque las tuplas son inmutables 
print('Recorriendo la tupla con un bucle for:')
#for item my_other_tuple:  # Añadido para recorrer 'my_for_tuple'
#    print(item)  # Añadido para mostrar cada elemento de 'my_for_tuple'     
#print('')  # Añadido para mantener el formato de salida limp