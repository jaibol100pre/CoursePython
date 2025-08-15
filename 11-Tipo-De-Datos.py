#Tipos de Datos en Python
#Autor: Jaibol
#Clases11.py 11
#Tipos de datos en Python   
#Python tiene varios tipos de datos incorporados, incluyendo:

#1. Números: enteros (int), flotantes (float) y complejos (complex).
numero_entero = 42  # Entero
print ('El tipo de variable es: ' , type(numero_entero))  # Añadido para mostrar el tipo de dato de la variable 'numero_entero'

numero_flotante = 3.14  # Flotante
print ('El tipo de variable es: ' , type(numero_flotante))  # Añadido para mostrar el tipo de dato de la variable 'numero_flotante'

numero_complejo = 1 + 2j  # Complejo     
print ('El tipo de variable es: ' , type(numero_complejo))  # Añadido para mostrar el tipo de dato de la variable 'numero_complejo'  

#2. Cadenas de texto (str): secuencias de caracteres.
Cadena_texto='Jaibol'
print ('El tipo de variable es: ' , type(Cadena_texto))  # Añadido para mostrar el tipo de dato de la variable 'nombre'

#3. Listas (list): colecciones ordenadas y mutables de elementos.
miLista = [1, 2, 3, 'Python', True]  # Lista con diferentes tipos de datos
print ('El tipo de variable es: ' , type(miLista))  # Añadido para mostrar el tipo de dato de la variable 'miLista'

#4. Tuplas (tuple): colecciones ordenadas e inmutables de elementos.
miTupla = (1, 2, 3, 'Python', True)  # Tupla con diferentes tipos de datos
print ('El tipo de variable es: ' , type(miTupla))  # Añado para mostrar el tipo de dato de la variable 'miTupla'

#5. Conjuntos (set): colecciones no ordenadas de elementos únicos.
miConjunto = {1, 2, 3, 'Python', True}  # Conjunto con diferentes tipos de datos
print ('El tipo de variable es: ' , type(miConjunto))  # Añadido para mostrar el tipo de dato de la variable 'miConjunto'

#6. Diccionarios (dict): colecciones de pares clave-valor.  
miDiccionario = {'nombre': 'Jaibol', 'edad': 30, 'lenguaje': 'Python'}  # Diccionario con diferentes tipos de datos
print ('El tipo de variable es: ' , type(miDiccionario))  # Añadido para mostrar el tipo de dato de la variable 'miDiccionario'

#Tipos de datos adicionales
#7. Booleanos (bool): valores de verdad, True o False.
repuesta=True
print ('El tipo de datos es:' , type(repuesta))  # Añadido para mostrar el tipo de dato de la variable 'respuesta'

#8. None: un tipo especial que representa la ausencia de valor. 
miNone = None  # Representa la ausencia de valor
print ('El tipo de variable es: ' , type(miNone))  # Añadido para mostrar el tipo de dato de la variable 'miNone'

print (type(print('Hola')))  # Añadido para mostrar el tipo de datos none de la función print

#9. Bytes: secuencias de bytes inmutables.      
MyBytes = b'Hola'  # Secuencia de bytes
print ('El tipo de variable es: ' , type(MyBytes))  # Añadido para mostrar el tipo de dato de la variable 'MyBytes' 

#10. Bytearray: secuencias de bytes mutables.
#11. Memoryview: permite acceder a los datos de un objeto de bytes sin copiarlo.
#12. Frozenset: una versión inmutable de un conjunto.   
#13. Enumeraciones (Enum): una clase que define un conjunto de constantes con nombre.
#14. Tipos personalizados: puedes definir tus propios tipos de datos usando clases.     
#15. Funciones: en Python, las funciones son objetos de primera clase y pueden ser asignadas a variables, pasadas como argumentos y devueltas desde otras funciones.
#16. Módulos: archivos que contienen definiciones y declaraciones de Python, que pueden ser importados en otros scripts.    
#17. Clases: plantillas para crear objetos, que pueden contener atributos y métodos.
#18. Archivos: objetos que representan archivos abiertos en el sistema de archivos, permitiendo leer y escribir datos.  
#19. Generadores: funciones que permiten iterar sobre una secuencia de valores sin almacenarlos todos en memoria al mismo tiempo.
#20. Corutinas: funciones que pueden ser pausadas y reanudadas, permitiendo la concurrencia cooperativa.
#21. Context Managers: objetos que definen métodos __enter__ y __exit__, permitiendo gestionar recursos de manera eficiente.
#22. Iteradores: objetos que implementan el protocolo de iteración, permitiendo recorrer una secuencia de elementos uno a uno.
#23. Descriptores: objetos que definen los métodos __get__, __set__ y __delete__, permitiendo controlar el acceso a los atributos de una clase.
#24. Tipos de datos de tipo cadena: como str, bytes y bytearray, que representan secuencias de caracteres y bytes.
#25. Tipos de datos de tipo numérico: como int, float y complex, que representan números enteros, de punto flotante y complejos respectivamente.
#26. Tipos de datos de tipo secuencia: como list, tuple y range, que representan colecciones ordenadas de elementos.
#27. Tipos de datos de tipo mapeo: como dict, que representan colecciones de pares clave-valor.
#28. Tipos de datos de tipo conjunto: como set y frozenset, que representan colecciones no ordenadas de elementos únicos.
#29. Tipos de datos de tipo booleano: como bool, que representan valores de verdad (True o False    ).
repuesta=False
print ('El tipo de datos es:' , type(repuesta))  # Añadido para mostrar el tipo de dato de la variable 'respuesta'
#30. Tipos de datos de tipo None: como NoneType, que representa la ausencia de valor.
#31. Tipos de datos de tipo archivo: como file, que representan archivos abiertos en el sistema de archivos.
#32. Tipos de datos de tipo función: como function, que representan funciones definidas por el usuario o incorporadas en Python.
#33. Tipos de datos de tipo módulo: como module, que representan módulos importados en el programa.
#34. Tipos de datos de tipo clase: como class, que representan clases definidas por el usuario.
#35. Tipos de datos de tipo objeto: como object, que es la clase base de todos los objetos en Python.
#36. Tipos de datos de tipo generador: como generator, que representan funciones generadoras que pueden ser iteradas.
#37. Tipos de datos de tipo corutina: como coroutine, que representan funciones que pueden ser pausadas y reanudadas.
#38. Tipos de datos de tipo contexto: como context manager, que representan objetos que gestionan recursos de manera eficiente.
#39. Tipos de datos de tipo iterador: como iterator, que representan objetos que implementan el protocolo de iteración.
#40. Tipos de datos de tipo descriptor: como descriptor, que representan objetos que controlan el acceso a los atributos de una clase.
#41. Tipos de datos de tipo enumeración: como enum, que representan conjuntos de constantes con nombre.
#42. Tipos de datos de tipo namedtuple: como namedtuple, que representan tuplas con campos nombrados.


prueba=int('este es un 32')
print ('El tipo de variable es: ' , type(prueba))  # Añadido para mostrar el tipo de dato de la variable 'prueba'