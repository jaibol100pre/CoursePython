from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Mi Ventana con Favicon")

# Cargar la imagen del favicon (asegúrate de que la ruta sea correcta)
try:
    photo = PhotoImage(file = "/home/jaibol/CoursePython-original/myicon.png")
    root.iconphoto(False, photo)
    #raiz.geometry(Ancho,Alto)
    root.geometry("600x200")
except FileNotFoundError:
    print("Error: Archivo de icono no encontrado.")
except Exception as e:
    print(f"Error al cargar el icono: {e}")

b = Button(root, text = 'Click me !')
b.pack(side = TOP)

root.mainloop()