##Clases04.py 04
#Cadena de caracteres en Python
Saludo='Hola, Como estas?'
Nombre= 'Jaibol'

print (Saludo, Nombre)

#Las cadenas se pueden concatenar (pegar juntas) con el operador + y se pueden repetir con *:

print('Adios' + ' ' + Nombre)

print(' ')

print(Nombre*3)  # Añadido para mostrar la repetición de cadenas

print(' ')

Saludo = 'Hola, Como estas?'
print(Saludo[0])  # Añadido para mostrar el primer carácter de la cadena, es decir, muetra la 'H'
print(Saludo[1])  # Añadido para mostrar el segundo carácter de la cadena, es decir, muetra la 'O'
print(Saludo[2])  # Añadido para mostrar el tercer carácter, es decir, muetra la 'L' 
print(Saludo[3])  # Añadido para mostrar el tercer carácter, es decir, muetra la 'A' 

print('Otro ejemplo de indexación:')
print(' ')

#Los índices también pueden ser números negativos, para empezar a contar desde la derecha:
lenguaje    = 'PASCAL'
print(lenguaje [-6])
print(lenguaje [-5])
print(lenguaje [-4])
print(lenguaje [-3])
print(lenguaje [-2])
print(lenguaje [-1]) #Último Caracter
print(lenguaje [0])

#Recorrer una cadena de caracteres con un bucle for
for letra in Saludo:
    print(letra)  # Añadido para mostrar cada letra del nombre en una nueva línea
print(' ')

#pruedo imprimir una parte de la cadena usando el slicing (rebanado):
Frase = 'La Vida es bella, disfrutala al maximo'
print (Frase [0:9])  #el cartcater 9 es excluido, es decir, solo se muestra hasta el 8vo caracter
print (Frase [3:12])  #el cartcater 12 es excluido, es decir, solo se muestra hasta el 11vo caracter

#LEN()
#El método len() devuelve la longitud de una cadena de caracteres
palabras = 'supercalifragilisticexpialidocious'

nro=len(palabras)
print ('La palabra ',   palabras  , ' tiene ', nro, ' caracteres ')  # Añadido para mostrar la longitud de la cadena


mensaje= 'Pedir permiso es de sabios'
print  (mensaje.upper())  # Convierte la cadena a mayúsculas
print  (mensaje.lower())  # Convierte la cadena a minúsculas
print  (mensaje.capitalize())  # Convierte el primer carácter a mayúscula y el resto a minúsculas
print  (mensaje.title())  # Convierte el primer carácter de cada palabra a mayúscula
print  (mensaje.replace('s', '$'))  # Reemplazar todas las 's' por '$'
print  (mensaje.replace('Pedir', 'Dar'))  # Reemplazar 'P


mensaje= '\t Pedir permiso es de sabios'
print  (mensaje) # Muestra la cadena con el tabulador al inicio
mensaje= 'Pedir permiso \n es de sabios'
print  (mensaje) # Muestra la cadena con salto de línea

mensaje= '\\t Pedir permiso \\n es de sabios'
print  (mensaje) # Muestra como escapar los caracteres especiales

##Formateo de cadenas 
nombre='Jaibol'
apellido= 'Santaella' 
edad_entera= 44 
edad_flotante=44.5

print('Mi nombre es %s ,mi apellido es %s y mi edad es %d o %f' %(nombre,apellido,edad_entera,edad_flotante)  )  # Añadido para mostrar el uso de formateo de cadenas con %s y %d

###Antes se utilizaba format
print('Mi nombre es {} , mi apellido es {} y mi edad es {} o {}'.format(nombre, apellido, edad_entera, edad_flotante))  # Añadido para mostrar el uso de formateo de cadenas con .format()

##"Ahora fstring"
print(f'Mi nombre es {nombre} , mi apellido es {apellido} y mi edad es {edad_entera} o {edad_flotante}')

