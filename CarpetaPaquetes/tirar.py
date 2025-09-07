##Calcula el tiempo de ejecución de una función

import timeit

nombre="Jaibol"
edad=30

#"Usando f-strings"
calculo_f_string = timeit.timeit('f"Hola {nombre} tienes {edad} años."' , globals=globals(), number=1000000 )  #Ejecuta un millon de veces para determinar el tiempo que demora

#Usando .format()

calculo_format =  timeit.timeit('"Hola {} tienes {} años.".format(nombre,edad)' , globals=globals(), number=1000000)

print(f"Tiempo usando f-string: {calculo_f_string} segundos")
print(f"Tiempo usando .format(): {calculo_format} segundos")


pi = 3.14159

print (f"El valor de pi es: {pi:.2f}")
print ("El valor de pi es: {:.2f}".format(pi))