#Python
#Autor: Jaibol
#Clases08.py 08
#Bucles y condicionales en Python

lenguajes  = ['Python', 'Java', 'C++', 'JavaScript']
print(' ')
print('Recorriendo la lista de lenguajes de programación:')
for palabra in lenguajes:
    print(palabra)  # Añadido para mostrar cada lenguaje en una nueva línea            

for i in range(len(lenguajes)):
    print(lenguajes[i])  # Añadido para mostrar cada lenguaje usando el índice

BucleWhile = True
while BucleWhile:
    print('Este es un bucle while que se ejecuta hasta que se detenga manualmente.')  # Añadido para mostrar el funcionamiento del bucle while
    break  # Añadido para evitar un bucle infinito, se puede eliminar si se desea que el bucle continúe indefinidamente 
#Bucle while con una condición
print(' ')
print('Bucle while con una condición:')
# Este bucle se ejecuta mientras 'a' sea menor que 10
a=1 
while a<10:
    print('El valor de a es:', a)  # Añadido para mostrar el valor de 'a' en cada iteración
    a += 1  # Incremento de 'a' para evitar un bucle infinito


#Bucle while
#  
a=1
b=10
while a < b:
  print ('Es menor porque vale: ', a)
  a+=1
else:
  print('Ya no es menor pues ahora vale ', a)



#Bucle while
# Sentencia continue 
a=1
b=10
while a < b:
  print ('Es menor porque vale: ', a)
  a+=1
  if a==5:
     a+=2
     continue
else:
  print('Ya no es menor pues ahora vale ', a)

#Bucle while
#  Sentencia break 
a=1
b=10
while a < b:
  print ('Es menor porque vale: ', a)
  a+=1
  if a==5:
     break
else:
  print('Ya no es menor pues ahora vale ', a)




#Bucle For con String
for a in 'Hola Mundo':
  print (a)

#Bucle For con una Variables
myVar = 'Bienenvenidos a Venezuela'
for text in myVar: 
  print (text)

#Bucle For con una Lista
myList=[1,2,2,4,5,6,7]
print() 
for num in myList:
  print (num)

#Bucle For con tuplas
mytuple=('a','b','c','d','e')
for letra in mytuple:
  print(letra)

#Bucle Fo con Diccionarios
myDict = {
  'nombre':'Jaibol',
  'apellido':'Santaella',
  'cedula':'15091893',
  'edad':'44'
}
for dato in myDict:
   print(dato) #Imprime solo las Claves no Valores

for dato in myDict.values(): 
   print(dato) #Imprime solo los Valores no las Claves

for dato in myDict.items(): 
   print(dato) #Imprime solo los Valores no las Claves  



words = ['Gato', 'Avion', 'Autobus', 'Perro', 'Casa']
for w in words:
    print(w ,'tiene una longitud de: ' , len(w))


categoria = ['Elaboración de Documentos', 'Asesoría', 'Consulta Médica' 'Diseño Web', 'Elaboracion de Planos' 'Desarrollo de Software']
profesion = 'Ingeniero de Sistemas' , 'Doctor', 'Nutricionista', 'Ginecólogo',  'Abogado', 'Arquitecto', 'ingeniero civil', 'Contador'

categoria = input('Ingrese una categoría: ')  # Añadido para solicitar una categoría al usuario
if categoria == 'Elaboración de Documentos':
    print('La categoría es Elaboración de Documentos está asignada a los profesionales:' , profesion[1:4] )
elif categoria == 'Consulta Médica':
    print('La categoría Consulta Médica está asignada a los profesionales:', profesion[1:4])
elif categoria == 'Diseño Web':
    print('La categoría Diseño Web está asignada a los profesionales:', profesion[0])
elif categoria == 'Elaboración de Planos':
    print('La categoría Elaboración de planos está asignada a los profesionales:', profesion[5], 'e', profesion[6])
else:
    print('La categoría no está asignada a ningún profesional')
