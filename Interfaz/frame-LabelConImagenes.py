import datetime
import time
from tkinter import *


def actualizar_hora():
    ahora = datetime.datetime.now()
    hora_str = ahora.strftime("%H:%M:%S")
    fecha_str = ahora.strftime("%Y-%m-%d")
    label_hora.config(text=hora_str)
    label_fecha.config(text=fecha_str)
    root.after(1000, actualizar_hora)  # Actualizar cada segundo


root=Tk()
root.title("ProfesioApp")
root.resizable(True,True) #raiz
root.config(bg="blue")
root.config(cursor="hand2") #Tipo Border

miFrame=Frame(root,width=500, height=400)
miFrame.pack()
miImagen=PhotoImage(file="myicon.png")
Label(miFrame, image=miImagen).place(x=200, y=200)
Label(miFrame,  text="Bienvenidos a \n", fg="#000" , font=("Comic Sans MS",22)  ).place(x=50, y=50)
Label(miFrame,  text="Profesionales de Venezuela", fg="#000" , font=("Comic Sans MS",22)  ).place(x=100, y=100)

miFrame2=Frame(root,width=250, height=200)
miFrame2.pack()
miFrame2.pack(side="left", anchor=W)   #Izquierda y a la oeste (Centro izquierda)
label_hora = Label(miFrame2, text="", font=("Helvetica", 48))
label_hora.pack()
label_fecha = Label(miFrame2, text="", font=("Helvetica", 24))
label_fecha.pack()
actualizar_hora()  # Iniciar la actualización de la hora


root.mainloop()
