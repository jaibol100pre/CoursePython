#https://www.tutorialspoint.com/python/tk_text.htm


from tkinter import *
root=Tk()
miFrame=Frame(root,width=1200, height=600)
miFrame.pack()

minombre=StringVar()  #Variable de String de Caracateres

#GRILLAS   (Columnas y Filas)
cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1 , padx=10  , pady=10)
cuadroNombre.config(fg="red", justify="right") 


cuadroPass=Entry(miFrame)
cuadroPass.grid(row=1, column=1 , padx=10  , pady=10)
cuadroPass.config(show="*")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2, column=1 , padx=10  , pady=10)

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=3, column=1, padx=10  , pady=10)

##Text
textoComentario=Text(miFrame, width=16 , height=5)
textoComentario.grid(row=4, column=1, padx=10  , pady=10)

##Scroll del TEXT
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4,column=2, sticky="nsew")
textoComentario.config(yscrollcommand=scrollVert.set)
##Label
nombreLabel=Label(miFrame,text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e" , padx=10  , pady=10)
ApellidoLabel=Label(miFrame,text="Apellido:")
ApellidoLabel.grid(row=2, column=0, sticky="e" , padx=10  , pady=10)
direccionLabel=Label(miFrame,text="Dirección:")
direccionLabel.grid(row=3, column=0, sticky="e" , padx=10  , pady=10)
passLabel=Label(miFrame,text="Password:")
passLabel.grid(row=1, column=0, sticky="e" , padx=10  , pady=10)
comentarioLabel=Label(miFrame,text="Comentario:")
comentarioLabel.grid(row=4, column=0, sticky="e" , padx=10  , pady=10)



##Button

def codigoBoton():
    minombre.set("Jaibol")    


botonEvio=Button(root, text="Envíar", command=codigoBoton)
botonEvio.pack()

root.mainloop()
