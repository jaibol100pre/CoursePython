#Python
'''Módulos son archivos con escritos con extensiones .py pyc (Python compilado) o archivos escrito en C para Cpython, 
que posee su propio espacio de nombres y que puede contener variables, funciones, clases e incluso otros modulos
'''

#Python
# Ejemplo de importación de un módulo estándar

import math
from datetime import datetime


# Uso de una función del módulo math
print(math.sqrt(16))  # Imprime 4.0 o sea la raiz cuadrada de 16

# Ejemplo de importación de una función específica de un módulo

# Uso de la función importada
print(datetime.now())  # imprime la fecha 

print("Este es mi primer modulo")

def sumar (op1,op2):
    print ("\n El resultado de la suma es: " ,  op1+op2)

def restar (op1,op2):
    print ("\n El resultado de la resta es: " ,  op1-op2)


def multiplicar (op1,op2):
    print ("\n El resultado de la multiplicacion es: " ,  op1*op2)




