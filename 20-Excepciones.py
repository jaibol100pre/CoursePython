#Python
#Excepcion
'''
Las excepciones son errores que ocurren durante la ejecución del programa. La sintaxis del código es correcta pero durante la ejecución ha ocurrido "algo inesperado".
'''
def suma(num1,num2):
    return num1+num2

def resta (num1,num2):
    return num1-num2

def multiplica (num1,num2):
    return num1*num2

###Antes de agregar la excepción
'''
def divide(num1,num2):
    return num1/num2
'''
#############################################
##Agregando la excepción ZeroDivisionError###
#############################################
def divide(num1,num2):
    try:
        return num1/num2
    except ZeroDivisionError: # <----------------
        print("No se puede dividir entre cero")
        return "Operación errónea"
while True: 
######################################
##Agregando la excepción ValueError###
######################################  
        try:
            opt1=(int(input("Escribe un número entero: ")))
            opt2=(int(input("Escribe un segundo número entero: ")))
            break
        except ValueError:  #  <------------------------
            print("Los valores agregados no son número enreros")

operacion=input("Introduce la operación a realizar (suma, resta, multiplica, divide: ")

if operacion=="suma":
    print(suma(opt1,opt2))
elif operacion=="resta":
    print(resta(opt1,opt2))
elif operacion=="multiplica":
    print(multiplica(opt1,opt2))
elif operacion=="divide":
    print(divide(opt1,opt2))

else:
    print ("operacion no contemplada")
    #este sistema falla si se pretende dividir un entero entre cero "0"
    #Aplicamos captura o control de exepcion en la línea que genera el error, es decir, en las línea 16 

    '''       
          #############################
          ##ERROR ZeroDivisionError:###
          #############################
    Traceback (most recent call last):
    File "/home/jaibol/CoursePython-original/20-Excepciones.py", line 31, in <module>
        print(divide(opt1,opt2))
          ^^^^^^^^^^^^^^^^^
    File "/home/jaibol/CoursePython-original/20-Excepciones.py", line 16, in divide
        return num1/num2
           ~~~~^~~~~
        ZeroDivisionError: division by zero
    '''
    #Este sistema falla si se agrega una letra en vez de un número entero
    '''
    Traceback (most recent call last):
    File "/home/jaibol/CoursePython-original/20-Excepciones.py", line 31, in <module>
     opt2=(int(input("Escribe un segundo número entero: ")))
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        ValueError: invalid literal for int() with base 10: 'a'
    '''

print("Operación ejecutada. Continuación de ejecución del programa")