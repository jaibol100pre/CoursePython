#Python
#Excepcion III
#Lanzamientos de excepciones
##Instrucción Raise

def evaluaEdad(edad):

    if edad < 0:
        raise  TypeError("No se permiten edades negativas") # raise permite personalizar una execpcion
    if edad<20:
        return "Eres muy joven"
    elif edad<40:
        return "Eres joven"
    elif edad<65:
        return "Eres maduro"
    elif edad<100:
        return "Eres anciano"


print(evaluaEdad(-70))

