#Clases02.py 02
#Variables en Python
#Declarar una variable y asignarle un valor
#Autor: Jaibol
nombre = 'Jaibol'
print('Hola', nombre)
print('Bienvenido a la clase de Python')  # Añadido para mayor claridad
print('')  # Añadido para mantener el formato de salida limpio  
numero = 42
print('El número es:', numero)  # Añadido para mostrar el uso de variables
decimal = 3.14
print('El valor decimal es:', decimal)  # Añadido para mostrar el uso de variables
booleano = True
print('El valor booleano es:', booleano)  # Añadido para mostrar el uso de variables
print('')  # Añadido para mantener el formato de salida limpio  

primerNumero = 10
segundoNumero = 20
# Añadido para mostrar la suma de dos variables
resultado = (primerNumero + segundoNumero)  
print('La suma de', primerNumero, 'y', segundoNumero, 'es:', resultado)

primeracifra = 5
segundacifra =15.2025252
# Añadido para mostrar la suma de dos variables con diferentes tipos
resultado2 = (primeracifra + segundacifra)
print('La suma de', primeracifra, 'y', segundacifra, 'es', resultado2) 


print (id(nombre))  # Añadido para mostrar el ID de la variable 'nombre' La función id() devuelve la dirección de memoria del objeto
print (id(numero))  # Añadido para mostrar el ID de la variable 'numero'
print (id(decimal))  # Añadido para mostrar el ID de la variable 'decimal
print (id(booleano))  # Añadido para mostrar el ID de la variable 'booleano' #El valor es aleatorio y varía en cada ejecución    


age = int(input('Ingrese su edad'))  # Añadido para mostrar la conversión de un número a entero
print('El tipo de dato de la variable age es:', type(age))  # Añadido para mostrar el tipo de dato de la variable 'age'
anio= str(input('Ingrese el año de nacimiento:')) # Añadido para mostrar la conversión de un número a cadena de caracteres
print('El tipo de dato de la variable anio es:', type(anio))  # Añadido para mostrar el tipo de dato de la variable 'age'

print('La edad es: ', age)  # Añadido para mostrar el uso de una variable de tipo entero, esto imprime 44 porque la conversión a entero descarta la parte decimal

print('Mi edad es: ' + str(age) + ' y nací en el año ' + anio)  # Añadido para mostrar el uso de una variable de tipo entero

# Añadido para mostrar la asignación múltiple de variables
primer_nombre, segundo_nombre, edad, alias = 'Jaibol', "jose", 44, 'jaibolito'  

# Añadido para mostrar el uso de variables múltiples
print('Mi nombre es:', primer_nombre, segundo_nombre, 'tengo', edad, 'años y mi alias es', alias)  

lorem = '''Lorem Ipsum es simplemente texto de relleno de la industria de la impresión y la composición tipográfica. 
        Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, 
        cuando un impresor desconocido tomó una galera de tipos y los mezcló para hacer un libro de muestras de tipos. 
        Ha sobrevivido no solo cinco siglos, sino también el salto a la composición electrónica,     
       Lorem Ipsum is simply dummy text of the printing and typesetting industry.  
        Lorem Ipsum has been the industrys standard dummy text ever since the 1500s,  
        when an unknown printer took a galley of type and scrambled it to make a type specimen book.  
        It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged.  \
        It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages,  
        and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. '''

print(lorem)  # Añadido para mostrar el texto de Lorem Ipsum


#Desempaquetado de variables
frutas = ['manzana', 'banana', 'cereza']
x, y, z = frutas  # Desempaquetado de la lista en variables
print(x)  # Añadido para mostrar el valor de la variable 'x'
print(y)  # Añadido para mostrar el valor de la variable 'y'
print(z)  # Añadido para mostrar el valor de la variable 'z'
print()  # Añadido para mantener el formato de salida limpio



print(lorem[1:200])  # Añadido para mostrar los primeros 200 caracteres del texto de Lorem Ipsum;

print(lorem[200:-1])  # Añadido para mostrar los últimos 200 caracteres del texto de Lorem Ipsum;


nombre = 'Jaibol'

print(nombre[::1])  # Añadido para mostrar el texto de 'nombre' con un paso de 1, es decir, muestra todo el texto
print(nombre[::2])  # Añadido para mostrar el texto de 'nombre' con un paso de 2, es decir, muestra los caracteres 0,1,2

print(nombre.upper)  # Combierte el texto a mayúsculas, pero no lo imprime
print(nombre.upper())  # Añadido para mostrar el texto de 'nombre' convertido a mayúsculas
print(nombre.lower())  # Añadido para mostrar el texto de 'nombre' convertido a minúsculas
print(nombre.capitalize())  # Añadido para mostrar el texto de 'nombre' con la primera letra en mayúscula
print(nombre.title())  # Añadido para mostrar el texto de 'nombre' con la primera letra de cada palabra en mayúscula
print(nombre.replace('J', 'j'))  # Añadido para mostrar el texto de 'nombre' reemplazando 'J' por 'j'
print(nombre.replace('Jaibol', 'Jaibolito'))  # Añadido para mostrar el texto de 'nombre' reemplazando 'Jaibol' por 'Jaibolito' 
print(nombre.find('a'))  # Añadido para mostrar la posición de la primera aparición de 'a' en 'nombre'
print(nombre.find('z'))  # Añadido para mostrar la posición de la primera aparición de 'z' en 'nombre', que no existe, por lo que devuelve -1
print(nombre.index('a'))  # Añadido para mostrar la posición de la primera aparición de 'a' en 'nombre'
# print(nombre.index('z'))  # Añadido para mostrar la posición de la primera aparición de 'z' en 'nombre', que no existe, por lo que generaría un error si se descomenta
print(nombre.count('a'))  # Añadido para mostrar el número de veces que aparece 'a' en 'nombre'
print(nombre.count('z'))  # Añadido para mostrar el número de veces que aparece 'z' en 'nombre', que no existe, por lo que devuelve 0
print(nombre.startswith('J'))  # Añadido para mostrar si 'nombre' comienza con 'J', devuelve True
print(nombre.endswith('l'))  # Añadido para mostrar si 'nombre' termina con 'l
print(nombre.split('a'))  # Añadido para mostrar el texto de 'nombre' dividido en una lista por la letra 'a'
print(nombre.split())  # Añadido para mostrar el texto de 'nombre' dividido en una lista por los espacios en blanco
print(nombre.strip())  # Añadido para mostrar el texto de 'nombre' sin espacios en blanco al inicio y al final
print(nombre.lstrip())  # Añadido para mostrar el texto de 'nombre' sin espacios en blanco al inicio            
print(nombre.rstrip())  # Añadido para mostrar el texto de 'nombre' sin espacios en blanco al final 
print(nombre.isalpha())  # Añadido para mostrar si 'nombre' contiene solo letras, devuelve True
print(nombre.isdigit())  # Añadido para mostrar si 'nombre' contiene solo dígitos, devuelve False
print(nombre.isalnum())  # Añadido para mostrar si 'nombre' contiene solo letras y números, devuelve True
print(nombre.islower())  # Añadido para mostrar si 'nombre' está en minúsculas, devuelve False
print(nombre.isupper())  # Añadido para mostrar si 'nombre' está en mayúsculas, devuelve False
print(nombre.isspace())  # Añadido para mostrar si 'nombre' contiene solo espacios en blanco, devuelve False
print(nombre.isnumeric())  # Añadido para mostrar si 'nombre' contiene solo números, devuelve False
print(nombre.isdecimal())  # Añadido para mostrar si 'nombre' contiene solo números decimales, devuelve False
print(nombre.isidentifier())  # Añadido para mostrar si 'nombre' es un identificador válido en Python
print(nombre.isprintable())  # Añadido para mostrar si 'nombre' es imprimible, devuelve True
print(nombre.swapcase())  # Añadido para mostrar el texto de 'nombre' con mayúsculas y minúsculas intercambiadas
print(nombre.center(20))  # Añadido para mostrar el texto de 'nombre' centrado en un ancho de 20 caracteres
print(nombre.ljust(20))  # Añadido para mostrar el texto de 'nombre' alineado a la izquierda en un ancho de 20 caracteres
print(nombre.rjust(20))  # Añadido para mostrar el texto de 'nombre' alineado a la derecha en un ancho de 20 caracteres
print(nombre.zfill(20))  # Añadido para mostrar el texto de 'nombre' rellenado con ceros a la izquierda hasta un    ancho de 20 caracteres 