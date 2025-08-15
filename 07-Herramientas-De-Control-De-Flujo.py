#Listas en Python
#Autor: Jaibol
#Clases07.py 07
#Herramientas para control de flujos en python

x= int(input('Ingrese un número entero:'))
# Añadido para solicitar un número entero al usuario, debe incluir la conversión a entero (int) en la variable x para diferenciar entre números y string
# 
if x<0:
    print('El número es negativo')
elif x==0:
    print('El número es cero')
else:
    print('El número es positivo')  

#Ejercicio 01 
if x % 2 == 0:
    print('El número es par')
#Ejercicio 02 if else 
lenguaje='COBOL'
if lenguaje == 'Python':
    print('¡Hola Python!')
else:
    print('¡Hola, el lenguaje  no es Python!')
print('') 
#Ejercicio 03 el if elif else 
lenguaje='Java'
if lenguaje == 'Python':
    print('¡Hola Python!')
elif lenguaje == 'Java':   
    print('¡Hola, el lenguaje es Java, no Python!')
elif lenguaje == 'C++':     
    print('¡Hola, el lenguaje es C++, no Python!')
elif lenguaje == 'JavaScript':     
    print('¡Hola, el lenguaje es JavaScript, no Python!')
else:
    print('¡Hola, lenguaje no identificado!')