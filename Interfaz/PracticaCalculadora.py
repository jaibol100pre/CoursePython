#Python
from tkinter import *
#from tkinter import ttk
#-----Raiz------------
raiz = Tk()
raiz.title("Calculadora")
raiz.resizable(True,True) #raiz
#----Frame------------
miFrame=Frame(raiz) #declarando nuestro Frame
##EMPAQUETADO
miFrame.pack()
#---Pantalla----------------------------------------------------

numeroPantalla=StringVar()
pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1,column=1, padx=10,pady=10, columnspan=4)
pantalla.config(background="black" , fg="green", justify="right")


#---------Pulsaciones teclado------------------------------------

def numeroPulsado(num):
    numeroPantalla.set(numeroPantalla.get()+ num)

#--------------Fila 01 -----------------------------------------
boton7=Button(miFrame,text="7", width=3, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=1)
boton8=Button(miFrame,text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=2)
boton9=Button(miFrame,text="9", width=3, command=lambda:numeroPulsado("9")) 
boton9.grid(row=2,column=3)
botonDiv=Button(miFrame,text="/", width=3)
botonDiv.grid(row=2,column=4)
#--------------Fila 02 -----------------------------------------
boton4=Button(miFrame,text="4", width=3, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=1)
boton5=Button(miFrame,text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=2)
boton6=Button(miFrame,text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=3)
botonMult=Button(miFrame,text="x", width=3)
botonMult.grid(row=3,column=4)
#--------------Fila 03 -----------------------------------------
boton1=Button(miFrame,text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=4,column=1)
boton2=Button(miFrame,text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=4,column=2)
boton3=Button(miFrame,text="3", width=3, command=lambda:numeroPulsado("3")) 
boton3.grid(row=4,column=3)
botonRest=Button(miFrame,text="-", width=3)
botonRest.grid(row=4,column=4)
#--------------Fila 04 -----------------------------------------
boton0=Button(miFrame,text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=5,column=1)
botonComa=Button(miFrame,text=",", width=3, command=lambda:numeroPulsado("."))
botonComa.grid(row=5,column=2)
botonIgual=Button(miFrame,text="=", width=3)
botonIgual.grid(row=5,column=3)
botonSum=Button(miFrame,text="+", width=3)
botonSum.grid(row=5,column=4)
'''
raiz.title("Calculadora")
raiz.resizable(True,True) #raiz
try:
    #raiz.iconbitmap("/home/jaibol/CoursePython-original/Interfaz/img/myicon.ico")
    miImagen=PhotoImage(file="/home/jaibol/CoursePython-original/Interfaz/img/myicon.png")
    Label(miFrame, image=miImagen).place(x=200, y=200)


except:
    print("Error al cargar la imagen. Verifica la ruta.")
    raiz.destroy()
    exit()

#aiz.geometry("650x350")
raiz.config(bg="blue")
raiz.config(cursor="hand2") #Tipo Border
'''
raiz.mainloop()#Siempre esta instrucción irá al final.