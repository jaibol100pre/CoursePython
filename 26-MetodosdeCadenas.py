
mi_text='Hola mundo cruel, estoy cansado pero debo seguir'

print(mi_text)

print(mi_text.upper())

print(mi_text.lower())

print(mi_text.capitalize())


nombre=input("Escribe tu nombre: ")

print("Hola ", nombre.upper(), " cómo estas?")


edad=input("Introduce tu edad: ")
while(edad.isdigit()==False):
    print("Por favor introduce un número")
    edad=input("Introduce tu edad: ")

if (int(edad)<18):
    print ("Eres menor de edad")
else:
    print("Eres mayor de edad")



