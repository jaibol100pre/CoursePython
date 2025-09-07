import sqlite3 

##Crear Base de Datos##
miConexion=sqlite3.connect("PrimeraBD")
miCursor=miConexion.cursor()
#Crear TABLA
##miCursor.execute("CREATE TABLE PRODUCTOS(NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")
#INSERTAR UN SOLO REGISTRO
#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALÓN' , '15', 'DEPORTES')")
#miConexion.commit()
#INSERTAR VARIOS REGISTROS:
'''
variosProductos=[
("CAMISETA", 10, "DEPORTES"),
("JARRON", 10, "CERÁMICA"),
("CAMIÓN", 10, "JUGUETERÍA")
]
miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?, ?, ?)", variosProductos )
miConexion.commit()
'''
#HACER UNA CONSULTA

miCursor.execute("SELECT * FROM PRODUCTOS")
variosProductos=miCursor.fetchall() #fetchall muestra una lista de valores
print(variosProductos)

for producto in variosProductos:
    print("Nombre del Producto: " , producto[0], "Sección: " , producto[2])

miConexion.commit()
miConexion.close()