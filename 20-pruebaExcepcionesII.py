#Python
#Excepcion II
#Multiples excepciones


def divide():
    try:
        op1=(float(input("Introduce el primer  número: ")))
        op2=(float(input("Introduce el segundo número: ")))
        print("La división es: " + str(op1/op2))
    except ValueError:
        print ("El valo introducido es erróneo")
    except ZeroDivisionError:
        print ("No se puede dividir entre cero")
    finally:  #Todo lo que se agregue dentro del finally se ejecutará siempre
         print("Calculo Finalizado")


divide()