#Operadores en Python
#Autor: Jaibol
#Clases12.py 12
#Operadores en Python
#Python tiene varios tipos de operadores que se pueden clasificar en diferentes categorías:     
#1. Operadores Aritméticos: Realizan operaciones matemáticas básicas.
a = 10
b = 5
print(a + b)# Suma
resultado=a+b
print(f'Suma: {a} + {b} es {resultado}')      # Suma
print('Resta:', a - b)         # Resta
print('Multiplicación:', a * b)  # Multiplicación   
print('División:', a / b)      # División
var=11/5
print('el resultadoes ' , var)
print('División Entera:', a // b)  # División entera
var=11//5
print('el resultadoes ' , var)
print('Módulo:', a % b)        # Módulo
print('Exponente:', a ** b)    # Exponente
#2. Operadores de Comparación: Comparan dos valores y devuelven un valor booleano.
print('Igual a:', a == b)      # Igual a
print('No igual a:', a != b)   # No igual a
print('Mayor que:', a > b)      # Mayor que 
#3.Operadores de Asignación: Asignan valores a variables.
a = 10
b = 5
a += b  # Equivalente a a = a + b
print('Asignación con suma:', a)  # Asignación con suma
a -= b  # Equivalente a a = a - b
print('Asignación con resta:', a)  # Asignación con resta
a *= b  # Equivalente a a = a * b
print('Asignación con multiplicación:', a)  # Asignación con multiplicación
a /= b  # Equivalente a a = a / b
print('Asignación con división:', a)  # Asignación con división
a //= b  # Equivalente a a = a // b
print('Asignación con división entera:', a)  # Asignación con división entera
a %= b  # Equivalente a a = a % b
print('Asignación con módulo:', a)  # Asignación con módulo
a **= b  # Equivalente a a = a ** b
print('Asignación con exponente:', a)  # Asignación con exponente
#4. Operadores Lógicos: Realizan operaciones lógicas.
print('AND:', a > 5 and b < 10)  # AND lógico
print('OR:', a > 5 or b < 10)    # OR lógico
print('NOT:', not (a > 5))        # NOT lógico
#5. Operadores de Identidad: Comprueban si dos variables apuntan al mismo objeto.
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print('x es y:', x is y)          # x es y
print('x es z:', x is z)          # x es z
print('x no es z:', x is not z)   # x no es z
#6. Operadores de Pertenencia: Comprueban si un valor está presente en         una secuencia.   
print('1 en x:', 1 in x)          # 1 en x
print('4 en x:', 4 not in x)      # 4 no en x
#7. Operadores Bit a Bit: Realizan operaciones a nivel de bits.
a = 10  # 1010 en binario
b = 4   # 0100 en binario       
print('AND Bit a Bit:', a & b)    # AND bit a bit
print('OR Bit a Bit:', a | b)     # OR bit a bit
print('XOR Bit a Bit:', a ^ b)    # XOR bit a bit
print('Desplazamiento Izquierda:', a << 1)  # Desplazamiento a la izquierda
print('Desplazamiento Derecha:', a >> 1)  # Desplazamiento a la derecha
#8. Operadores de Membresía:    
# Comprueban si un valor es miembro de una secuencia.
lista = [1, 2, 3, 4, 5]
print('3 en lista:', 3 in lista)  # 3 en lista
print('6 no en lista:', 6 not in lista)  # 6 no en      lista
#9. Operadores de Prioridad: Determinan el orden en que se evalúan las expresiones.
# Los operadores aritméticos tienen una prioridad más alta que los operadores de comparación,           
# que a su vez tienen una prioridad más alta que los operadores lógicos.
# Por ejemplo, en la expresión 3 + 4 * 2, la multiplicación se evalúa antes que la suma, por lo que el resultado es 11, no 14
#10. Operadores de Asignación Compuesta: Combinan una operación con una asignación.
# Por ejemplo, a += b es equivalente a a = a + b.   
#11. Operadores de Desempaquetado: Permiten desempaquetar valores de una colección.
# Por ejemplo, a, b = [1, 2] asigna 1 a a y 2 a b.
#12. Operadores de Identidad de Clase: Permiten verificar si un objeto es una instancia de una clase específica.
# Por ejemplo, isinstance(objeto, Clase) devuelve True si objeto es una instancia de Clase.
#13. Operadores de Comparación de Clases: Permiten comparar objetos de clases personalizadas.
# Por ejemplo, puedes definir los métodos __eq__, __lt__, __gt__ en tu clase para personalizar la comparación.
#14. Operadores de Asignación de Clases: Permiten asignar valores a atributos de una clase.
# Por ejemplo, puedes usar self.atributo = valor dentro de un método de una clase para asignar un valor a un atributo de instancia.
#15. Operadores de Iteración: Permiten iterar sobre colecciones.
# Por ejemplo, puedes usar un bucle for para iterar sobre una lista o un diccionario.
for i in range(5):
    print('Iteración:', i)  # Iteración de 0 a 4    
#16. Operadores de Excepción: Permiten manejar excepciones en Python.
# Por ejemplo, puedes usar try y except para manejar errores en tu código.
try:
    resultado = 10 / 0  # Esto generará una excepción de división por cero
except ZeroDivisionError:
    print('Error: División por cero')
#17. Operadores de Contexto: Permiten manejar recursos de manera eficiente.
# Por ejemplo, puedes usar with para abrir un archivo y asegurarte de que se cierre correctamente.
with open('archivo.txt', 'w') as f:
    f.write('Hola, mundo!')  # Escribe en el archivo y se cierra automáticamente al salir del bloque with   
#18. Operadores de Generación: Permiten crear generadores en Python.
# Por ejemplo, puedes usar yield para crear una función generadora.
def generador():
    for i in range(5):
        yield i  # Genera valores de 0 a 4  
for valor in generador():
    print('Generador:', valor)  # Imprime los valores generados
#19. Operadores de Corutina: Permiten crear corutinas en Python.
# Por ejemplo, puedes usar async def para definir una corutina.
import asyncio  
async def corutina():
    await asyncio.sleep(1)  # Espera 1 segundo
    print('Corutina ejecutada')  # Imprime un mensaje al finalizar la espera
asyncio.run(corutina())  # Ejecuta la corutina  
#20. Operadores de Contexto de Administrador: Permiten gestionar recursos de manera eficiente.
# Por ejemplo, puedes usar with para manejar recursos como archivos o conexiones de red.
class ContextoAdministrador:
    def __enter__(self):
        print('Entrando en el contexto')
        return self  # Devuelve el objeto del contexto

    def __exit__(self, exc_type, exc_value, traceback):
        print('Saliendo del contexto')  # Limpieza al salir del contexto 
with ContextoAdministrador() as contexto:
    print('Dentro del contexto')  # Código dentro del contexto  
#21. Operadores de Iterador: Permiten iterar sobre colecciones.
# Por ejemplo, puedes usar iter() y next() para iterar sobre una lista.
lista = [1, 2, 3]
iterador = iter(lista)  # Crea un iterador de la lista
print('Primer elemento:', next(iterador))  # Imprime el primer elemento
print('Segundo elemento:', next(iterador))  # Imprime el segundo elemento
print('Tercer elemento:', next(iterador))  # Imprime el tercer elemento
#22. Operadores de Descriptor: Permiten controlar el acceso a los atributos de una clase.
class Descriptor:   
    def __get__(self, instance, owner):
        return 'Valor del descriptor'  # Devuelve un valor al acceder al atributo

    def __set__(self, instance, value):
        print('Asignando valor:', value)  # Imprime un mensaje al asignar un valor
class MiClase:
    atributo = Descriptor()  # Define un descriptor como atributo de la clase
mi_objeto = MiClase()
print('Atributo:', mi_objeto.atributo)  # Accede al atributo
mi_objeto.atributo = 'Nuevo valor'  # Asigna un nuevo valor al atributo
#23. Operadores de Tipo: Permiten verificar el tipo de un objeto.
print('Tipo de a:', type(a))  # Imprime el tipo de la variable a
print('Tipo de b:', type(b))  # Imprime el tipo de la variable b
print('Es instancia de int:', isinstance(a, int))  # Verifica si a es una instancia de int
print('Es instancia de str:', isinstance(a, str))  # Verifica si a es una instancia de str
#24. Operadores de Conversión de Tipo:
# Permiten convertir un tipo de dato a otro.
print('Conversión a str:', str(a))  # Convierte a a a una cadena
print('Conversión a float:', float(b))  # Convierte b a un número de punto flotante
print('Conversión a int:', int(3.14))  # Convierte 3.14 a un entero
print('Conversión a lista:', list((1, 2, 3)))  # Convierte una tupla a una lista
print('Conversión a tupla:', tuple([1, 2, 3]))  # Convierte una lista a una tupla
print('Conversión a conjunto:', set([1, 2, 3, 3]))  # Convierte una lista a un conjunto (elimina duplicados)
print('Conversión a diccionario:', dict([(1, 'uno'), (2, 'dos')]))  # Convierte una lista de tuplas a un diccionario
print('Conversión a bytes:', bytes('Hola', 'utf-8'))  # Convierte una cadena a bytes
print('Conversión a bytearray:', bytearray('Hola', 'utf-8'))    
#25. Operadores de Formateo: Permiten formatear cadenas de texto.
nombre = 'Jaibol'
edad = 30
print('Hola, mi nombre es {} y tengo {} años.'.format(nombre, edad))
print(f'Hola, mi nombre es {nombre} y tengo {edad} años.')
#26. Operadores de Fusión: Permiten combinar diccionarios en Python 3.9 y versiones posteriores.
diccionario1 = {'a': 1, 'b': 2}
diccionario2 = {'b': 3, 'c': 4}
diccionario_fusionado = {**diccionario1, **diccionario2}  # Combina los diccionarios
print('Diccionario fusionado:', diccionario_fusionado)  
#27. Operadores de Desempaquetado de Argumentos: Permiten pasar argumentos a funciones de manera flexible.
def funcion(*args, **kwargs):
    print('Argumentos posicionales:', args)  # Imprime los argumentos posicionales
    print('Argumentos con nombre:', kwargs)  # Imprime los argumentos con nombre
funcion(1, 2, 3, nombre='Jaibol', edad=30)  # Llama a la función con argumentos posicionales y con nombre       
#28. Operadores de Desempaquetado de Colecciones: Permiten desempaquetar elementos de colecciones.
lista = [1, 2, 3]
a, b, c = lista  # Desempaqueta los elementos de la lista
print('a:', a, 'b:', b, 'c:', c)  # Imprime los valores desempaquetados
#29. Operadores de Desempaquetado de    Diccionarios: Permiten desempaquetar claves y valores de diccionarios.
diccionario = {'a': 1, 'b': 2, 'c': 3}
a, b, c = diccionario.values()  # Desempaqueta los valores del diccionario
print('a:', a, 'b:', b, 'c:', c)  # Imprime los valores desempaquetados
#30. Operadores de Desempaquetado de Argumentos de Función: Permiten pasar argumentos a funciones de manera flexible.   
def funcion_con_argumentos(a, b, c):
    print('a:', a, 'b:', b, 'c:', c)  # Imprime los argumentos
funcion_con_argumentos(*lista)  # Pasa los elementos de la lista como argumentos    
#Tipos de datos en Python
#1. Números: enteros (int), de punto flotante (float) y complejos (complex).
numero_entero = 10  # Entero
print('El tipo de variable es:', type(numero_entero))  # Añadido para mostrar el tipo de dato de la variable 'numero_entero'
numero_flotante = 10.5  # Punto flotante
print('El tipo de variable es:', type(numero_flotante))  # Añadido para mostrar el tipo de dato de la variable 'numero_flotante'
print('El tipo de variable es:', type(numero_entero))  # Añadido para