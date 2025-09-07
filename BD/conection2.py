import sqlite3 

##Crear Base de Datos##
miConexion=sqlite3.connect("GestionProductos")
miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE PRODUCTOS(
    CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
    NOMBRE_ARTICUILO VARCHAR(50),
    PRECIO INTEGER,
    SECCION VARCHAR(20))
''')

productos=[

    ("AR01", "pelota", 20, "juguetería"),
    ("AR02", "pantalon", 15, "confeccion")

]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)
miConexion.commit()
miConexion.close()