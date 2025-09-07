#colecciones en Python
#Autor: Jaibol
#Clases09.py 09
#Colecciones en Python
#colecciones son estructuras de datos que permiten almacenar múltiples valores.
#Listas 

lenguajes = { 'Java', 'Python', 'C++', 'JavaScript' }  # Definición de un conjunto (set)    
print('Lenguajes de programación:', lenguajes)  # Añadido para mostrar el contenido del conjunto        
#Los conjuntos son colecciones no ordenadas de elementos únicos, útiles para eliminar duplicados y realizar operaciones matemáticas como uniones e intersecciones.
# #Operaciones con conjuntos
lenguajes2 = { 'Perl', 'Ruby', 'Pascal' }  # Definición de otro conjunto
print('Lenguajes de programación 2:', lenguajes2)  # Añadido para mostrar el contenido del segundo conjunto
# Unión de conjuntos
union = lenguajes | lenguajes2  # Unión de conjuntos
print('Unión de conjuntos:', union)  # Añadido para mostrar el resultado de la unión
# Intersección de conjuntos
interseccion = lenguajes & lenguajes2  # Intersección de conjuntos
print('Intersección de conjuntos:', interseccion)  # Añadido para mostrar el resultado de la intersección
# Diferencia de conjuntos
diferencia = lenguajes - lenguajes2  # Diferencia de conjuntos  
print('Diferencia de conjuntos:', diferencia)  # Añadido para mostrar el resultado de la diferencia         

# Diferencia simétrica de conjuntos 
# Es la unión de los elementos que están en uno de los conjuntos pero no en ambos.
diferencia_simetrica = lenguajes ^ lenguajes2  # Diferencia simétrica de conjuntos          
print('Diferencia simétrica de conjuntos:', diferencia_simetrica)   # Añadido para mostrar el resultado de la diferencia simétrica         
#
                    