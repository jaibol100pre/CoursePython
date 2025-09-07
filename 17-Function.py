#Python#Python
#Autor: Jaibol
##Sintaxis de una Función en Python
#def nombre_function(parametros):
    #Código
    #return Valor 
##Invocar una funcción
#nombre_function(parametro)

#Ejemplo:

def mi_nombre(a):
  print('Mi nombre es:' , a )
  
mi_nombre('Jaibol')#i


def suma (num1:float, num2:float):
  resultado=num1+num2 
  return resultado
 
mi_resultado=suma(5.2,10.1)
print(mi_resultado)


def multiplicacion (num1:int, num2:int):
   producto=num1*num2
   return producto

print( multiplicacion (5,4) )


def saludo ( nombre):
    print (f'Hola Cómo estas {nombre}?')

saludo(  nombre=input('escribe tu nombre: ') )

def genera_identidad (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido , alias='Sin alias' ):
   identidad = primer_nombre + segundo_nombre + primer_apellido + segundo_apellido + alias
   return identidad

individuo=genera_identidad ('Jaibol ', 'Jose ', 'Santaella ', 'Millan ' , 'Tatito' )
individuo=genera_identidad ('Jose ', 'Ramon ', 'Santaella ', 'Salas '  )

print(individuo)

def genera_identidad2 (primer_nombre, segundo_nombre, primer_apellido, segundo_apellido):
   identidad2 =  (f"Primer_nombre: {primer_nombre} segundo_nombre:  {segundo_nombre} Primer_apellido:  {primer_apellido} Segundo_apellido: {segundo_apellido}")
   return identidad2

individuo2=genera_identidad2 ('Gilbert ', 'Jose ', 'Santaella ', 'Millan ')

print(individuo2)


def bucleando ( num_inicio, num_fin, incremento ):
   mylist= list(range (num_inicio,num_fin,incremento)) #Incicia en 0, Finaliza en 20 y se incrementa de 2 en 2
   return mylist
num_inicio=int(input('Escribe el número de inicio: '))
num_fin=int(input('Escribe el número de Finalización:' ))
incremento=int(input('Escribe el valon de incremento: '))

list_print=bucleando (num_inicio, num_fin, incremento )
print(list_print)

def whilenado ( a, b, c ):
   mydict={ 'autor':a, 'libro':b, 'fecha_publicacion':c }
   return mydict
a=input('Escribe el Autor del Libro: ')
b=input('Escribe el nombre del libro: ')
c=input('Escribe la fecha de publicación: ' )

libro=whilenado( a,b,c )

print(libro)



