import miPrimerModulo #Importa todo el módulo miPrimerModulo
miPrimerModulo.restar(7,5) #NameModul.NameFunction

from miPrimerModulo import sumar  #Importa unicamente la funcion sumar del módulo miPrimerModulo
sumar(7,5) 

#restar(10,9) Falla porque no se ha importado la funcion restar


from miPrimerModulo import * #Importa todas las funciones  del módulo miPrimerModulo  

multiplicar(10,5)

restar(10,9)