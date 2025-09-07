#Python
#Interfaz Gráficas
#URL: https://www.youtube.com/watch?v=hTUJC8HsC2I&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=46
'''
Tambien denominadas GUI, son intermediarios entre el programa y el usuario. Formadas por un conjunto de gráficos como ventanas, botones, menús, casillas de verificación etc.
Tkinter
WxPython
PyQT
PyGTK

aptitude install python3-tk

#Tkinter es un "Puente" entre Python y la librería TCL/TK

Documentación: https://docs.python.org/es/3.13/library/tkinter.html

'''

import tkinter as tk   

def saludar():
    etiqueta_saludo.config(text="¡Hola, mundo!")


##Inicializar la librería
raiz = tk.Tk()

#Título de la Ventana
raiz.title("Ventana de Pruebas")

#Ajuste del Tamaño de la Ventana
raiz.resizable (True,True)  #Permite redireccionar en ambas direcciones (Ancho y Alto)
#raiz.resizable (Ancho,Alto) 
#raiz.resizable (False,False)    #Para no redireccionar en ninguna dirección
#raiz.resizable (True,False)     #Permite redireccionar el ancho más no el alto)
#raiz.resizable (False,True)     #Permite redireccionar el Alto pero no el Ancho

#Iconos en formato .ico
# Cargar la imagen (asegúrate de que la ruta sea correcta)
'''
try:
    raiz.iconbitmap("/home/jaibol/CoursePython-original/myicon.ico")
except:
    print("Error al cargar la imagen. Verifica la ruta.")
    raiz.destroy()
    exit()
'''

#raiz.geometry(Ancho,Alto)
raiz.geometry("400x200")


#Color de Fondo
raiz.config(bg="blue")



boton_saludo = tk.Button(raiz, text="Saludar", command=saludar)
boton_saludo.pack()
boton_saludo.config(bg="red")


etiqueta_saludo = tk.Label(raiz, text="Haz Clic")
etiqueta_saludo.config(bg="yellow")
etiqueta_saludo.pack()


raiz.mainloop() #Siempre esta instrucción irá al final.