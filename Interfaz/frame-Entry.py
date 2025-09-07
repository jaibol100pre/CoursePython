from tkinter import *
root=Tk()
miFrame=Frame(root,width=1200, height=600)
miFrame.pack()

#GRILLAS   (Columnas y Filas)
cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=0, column=1 , padx=10  , pady=10)
cuadroNombre.config(fg="red", justify="right") 

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1 , padx=10  , pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1 , padx=10  , pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10  , pady=10)

nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e" , padx=10  , pady=10)

ApellidoLabel=Label(miFrame,text="Apellido:")
ApellidoLabel.grid(row=3, column=0, sticky="e" , padx=10  , pady=10)

direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=2, column=0, sticky="e" , padx=10  , pady=10)

passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=1, column=0, sticky="e" , padx=10  , pady=10)

root.mainloop()
