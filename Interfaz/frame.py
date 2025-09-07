#Python
#Manejo de Frames (contenedeor de widgets)
#URL: https://www.youtube.com/watch?v=M80CzDC1Crc&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=47
from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Ventana de Pruebas")
root.resizable(True,True) #raiz
#root.iconbitmap("myicon.ico")
#root.geometry("650x350")
root.config(bg="blue")
root.config(cursor="hand2") #Tipo Border
miFrame=Frame() #declarando nuestro Frame
##EMPAQUETADO
miFrame.pack()
#miFrame.pack(side="right")# Ubica el Frame en la parte derecha de la Raiz
#miFrame.pack(side="left")#  Ubica el Frame en la parte izquierda  de la Raiz
#miFrame.pack(side="top")# Ubica el Frame en la parte superior de la Raiz
#miFrame.pack(side="bottom")# Ubica el Frame en la parte inferior de la Raiz
#miFrame.pack(side="left", anchor=N)  #izquierad y Arriba
#miFrame.pack(side="left", anchor=S)  #Izquierda y Abajo
#miFrame.pack(side="left", anchor=E)  #Izquierda y a la este (Centro derecha)
#miFrame.pack(side="left", anchor=W)   #Izquierda y a la oeste (Centro izquierda)
miFrame.config(bg="red") #Frame Color de Fondo del Frame (no la raiz)
#miFrame.pack(fill='x', expand=True)      #100% a los lados pero arriba
#miFrame.pack(fill='y' , expand=True)      #x; y; both; none
#miFrame.pack(fill='both' ,expand=True)   #Arriba
#miFrame.pack(fill='none', expand=True)   #Centro
miFrame.config(width=650 , height=350)
#BORDER
miFrame.config(bd=35) #border Tamaño
#miFrame.config(relief="groove") #Tipo Border
miFrame.config(relief="sunken") #Tipo Border
#CURSOR
miFrame.config(cursor="pirate")
root.mainloop()#Siempre esta instrucción irá al final.







'''
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
'''
