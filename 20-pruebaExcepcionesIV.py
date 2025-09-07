#Python
#Excepcion III
#Lanzamientos de excepciones
##Instrucción Raise

import math

def calculaRaiz(num1):
    if num1 <0:
        raise ValueError ("Número no puede ser negativo") #raise permite personalizar un mensaje
    else:
        return math.sqrt(num1)
    

op1=int((input("Introduce un número: ")))

try:
    print(calculaRaiz(op1))

except ValueError as ErroDeNumeroNegativo: # as permitye crear un alisa del error
    
    print(ErroDeNumeroNegativo)

print("Programa Terminado ")



