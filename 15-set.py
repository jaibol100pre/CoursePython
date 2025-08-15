#15-set.py
#Sets en Python
#Autor: Jaibol
#Un set es una colección no ordenada de elementos únicos, que no permite duplicados.
#Se definen usando llaves {} o la función set().    
#Crear un set vacío
st=set()
my_other_set = { }  # Añadido para corregir la sintaxis
st = {1, 2, 3, 'cuatro', 'cinco', True, 3.14}
print('Mi conjunto:', st)  # Añadido para mostrar el conjunto completo
print('')  # Añadido para mantener el formato de salida limpio
fruits = {'banana', 'orange', 'mango', 'lemon'}
print('Frutas:', fruits)  # Añadido para mostrar el conjunto de frutas
print('')  # Añadido para mantener el formato de salida limpio
print('Longitud del conjunto de frutas:', len(fruits))  # Añadido para mostrar la longitud del conjunto de frutas   
print('Frutas:', fruits)  # Añadido para mostrar el conjunto de frutas
print( type(st))    # Añadido para mostrar el tipo de st
print(len(st))  # Añadido para mostrar la longitud del conjunto st
'''
print(fruits[1])  # Añadido para mostrar el segundo elemento del conjunto de frutas, pero esto generará un error porque los conjuntos no son indexables
print('')  # Añadido para mantener el formato de salida limpio
'''
fruits = {'banana', 'orange', 'mango', 'lemon'}
print(fruits)  # Añadido para mostrar el conjunto de frutas
fruits.add('Apple')  # Añadido para agregar un nuevo elemento al conjunto
#print('Frutas después de agregar Apple:', fruits)  # Añadido para mostrar el conjunto de frutas después de agregar Apple
print(fruits)  # Añ
fruits.add('banana')  # Añadido para agregar banana, aunque los conjuntos no permiten duplicados
print('Frutas después de agregar banana:', fruits)  # Añadido para mostrar el conjunto de frutas después de agregar banana
print('')  # Añadido para mantener el formato
fruits.clear() #Añadido para limpiar el conjunto de frutas
print(fruits)  # Añadido para mostrar el conjunto de frutas después de limpiar limpio
print('')  # Añadido para mantener el formato de salida limpio
fruits = {'banana', 'orange', 'mango', 'lemon'}
# Añadido para evitar el error de indexación
#fruits_list = list(fruits)  # Convertir el conjunto a una lista para acceder por índice
#print(fruits_list[1])  # Ahora se puede acceder al segundo elemento
# print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo agregar un elemento al conjunto
fruits.add('kiwi')
print('Frutas después de agregar kiwi:', fruits)  # Añadido para mostrar el conjunto de frutas después de agregar kiwi
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo eliminar un elemento del conjunto
fruits.remove('banana')
print('Frutas después de eliminar banana:', fruits)  # Añadido para mostrar el conjunto de frutas después de eliminar banana
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo eliminar un elemento que no existe sin generar un error
fruits.discard('apple')  # Esto no generará un error si 'apple' no está en el conjunto
print('Frutas después de intentar eliminar apple:', fruits)  # Añadido para mostrar el conjunto de frutas después de intentar eliminar apple
print('')
# Añadido para mostrar cómo limpiar el conjunto
fruits.clear()
print('Frutas después de limpiar:', fruits)  # Añadido para mostrar el conjunto de frutas después de limpiar
print('')  # Añadido para mantener el formato de salidalimpio
# Añadido para mostrar cómo comprobar si un elemento está en el conjunto
print('¿Está mango en el conjunto de frutas?', 'mango' in fruits)  # Añadido para mostrar si 'mango' está en el conjunto de frutas
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo encontrar la intersección entre dos conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
intersection = set1.intersection(set2) #imprime los valores que están en ambos conjuntos
print('Intersección entre set1 y set2:', intersection)  # Añadido para mostrar la intersección entre set1 y set2
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo encontrar la unión entre dos conjuntos
union = set1.union(set2)
print('Unión entre set1 y set2:', union)  # Añadido para
print('')  # Añado para mantener el formato de salida limpio
# Añadido para mostrar cómo encontrar la unión entre dos conjuntos
union = set1.union(set2)
print('Unión entre set1 y set2:', union)  # Añadido para    mostrar la unión entre set1 y set2
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo encontrar la diferencia entre dos conjuntos             
difference = set1.difference(set2)
print('Diferencia entre set1 y set2:', difference)  # Añadido para mostrar la diferencia entre set1 y set2
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo encontrar la diferencia simétrica entre dos conjuntos
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
difference = set1.difference(set2)
print('Diferencia entre set1 y set2:', difference) # Añadido para mostrar la diferencia entre set1 y set2 imprime los valores que están en set1 pero no en set2
symmetric_difference = set1.symmetric_difference(set2) 
print('Diferencia simétrica entre set1 y set2:', symmetric_difference)  #   # Añadido para mostrar la diferencia simétrica entre set1 y set2 imprime valores que están en uno u otro conjunto, pero no en ambos
print('')  # Añadido para mantener el formato de salida limpio      
# Añadido para mostrar cómo convertir un conjunto a una lista
set_to_list = list(st)
print('Conjunto convertido a lista:', set_to_list)  # Añadido para mostrar el conjunto convertido a lista
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo convertir una lista a un conjunto           
list_to_set = set([1, 2, 2, 3, 4])
print('Lista convertida a conjunto:', list_to_set)  # Añadido para mostrar la lista convertida a conjunto
print('')  # Añadido para mantener el formato de salida limpio
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print('Set1:', set1)  # Añadido para mostrar el conjunto set1
set1.remove(1)  # Añadido para eliminar el primer elemento del conjunto
print('Set1 luego de borrar el primer elemento', set1 )  #   # Añadido para mostrar la diferencia simétrica entre set1 y set2 imprime valores que están en uno u otro conjunto, pero no en ambos
print('')  # Añadido para mantener el formato de salida limpio
#eliminar un set
del set1  # Añadido para eliminar el conjunto set1
print('Set1 eliminado')  # Añadido para indicar que set1 ha sido eliminado
print('')  # Añadido para mantener el formato de salida limpio

# Añadido para mostrar cómo comprobar si un conjunto es un subconjunto de otro
set_a = {1, 2}
set_b = {1, 2, 3, 4}
print('¿Es set_a un subconjunto de set_b?', set_a.issubset(set_b))  # Añadido para mostrar si set_a es un subconjunto de set_b
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo comprobar si un conjunto es un superconjunto de otro
print('¿Es set_b un superconjunto de set_a?', set_b.issuperset(set_a))  # Añadido para mostrar si set_b es un superconjunto de set_a
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo comprobar si dos conjuntos son disjuntos
set_x = {1, 2, 3}
set_y = {4, 5, 6}
print('¿Son set_x y set_y disjuntos?', set_x.isdisjoint(set_y))  # Añadido para mostrar si set_x y set_y son disjuntos  

print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo iterar sobre un conjunto
for fruit in fruits:
    print('Fruta:', fruit)  # Añadido para mostrar cada fruta en el conjunto de frutas
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo usar un conjunto en una función
def print_set_elements(s):
    for element in s:
        print('Elemento del conjunto:', element)  # Añadido para mostrar cada elemento del conjunto
print_set_elements(fruits)  # Añadido para llamar a la función con el conjunto
print('')  # Añadido para mantener el formato de salida limpio