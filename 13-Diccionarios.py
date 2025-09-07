#Diccionarios en Python
#Autor: Jaibol  
#Clases13.py 13
#Un diccionario es una colección no ordenada de pares clave-valor, donde cada clave es única y se utiliza para acceder a su valor asociado.
#Se definen usando llaves {}    
my_dict = dict()  # Crear un diccionario vacío
other_dict = {}  # Crear otro diccionario vacío
# syntax
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key5'] = 'value5'


person_info = {
    'firstname':'Jaibol', 
    "lastname":"Santaella", 
    'country':'Miranda',
    'city':'Charallave',
    }
print(person_info)  # Añadido para mostrar el uso de un diccionario
print('El tipo de dato de la variable person_info es:', type(person_info))  # Añadido para mostrar el tipo de dato de la variable 'person_info'
print('La longitud el diccionario es:' , len(person_info)) #Muestra la cantidad de elementos que tiene el diccionario
# Añadido para mostrar cómo acceder a un valor usando su clave
print('Nombre:', person_info['firstname'])  # Añadido para mostrar el valor asociado
print('Apellido:', person_info['lastname'])  # Añadido para mostrar el valor asociado
print('País:', person_info['country'])  # Añadido para mostrar el valor asociado
print('Ciudad:', person_info['city'])  # Añadido para mostrar el valor asociado
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo agregar un nuevo par clave-valor al diccionario
person_info['age']='44'   # Añadido para agregar la clave 'age' con el valor 30
print('Información de la persona después de agregar la edad:', person_info)  # Añadido para mostrar el diccionario después de agregar la edad
print('')  # Añadido para mantener el formato de salida limpio
person_info['is_single']='True'   # Añadido para agregar la clave 'age' con el valor 30
print('Información de la persona después de agregar la clave is single:', person_info)  # Añadido para mostrar el diccionario después de agregar is single
# Añadido para mostrar cómo actualizar un valor existente en el diccionario
person_info['city'] = 'Caracas'  # Añadido para actualizar el valor de la clave 'city'
print('Información de la    persona después de actualizar la ciudad:', person_info)  # Añadido para mostrar el diccionario después de actualizar la ciudad
other_dict = {
    'firstname':'Gilbert', 
    'lastname':'Santaella', 
    'country':'Barinas',
    'city':{'Caroni', 'Charallave', 'Caracas'},  #se puede agregar un conjunto como valor
}
print('Información de otra persona:', other_dict)  # Añadido para mostrar otro diccionario
print('')  # Añadido para mantener el formato de salida limpio
# Añadido para mostrar cómo acceder a un valor dentro de un conjunto en el diccionario
print('Ciudad de otra persona:', other_dict['city'])  # Añadido para mostrar    
print('el nombre es:' , other_dict['firstname'])  # Añadido para mostrar el nombre de otra persona
print('Apellido de otra persona:', other_dict['lastname'])  # Añadido para mostrar el apellido de otra persona
print('País de otra persona:', other_dict['country'])  # Añadido para mostrar el país de otra persona
print('')  # Añadido para mantener el formato de salida limpio
del person_info ['firstname'] # Añadido para eliminar la clave 'firstname' del diccionario
del person_info ['lastname']  # Añadido para eliminar la clave 'lastname' del  diccionario
print('Información de la persona después de eliminar el nombre y apellido:', person_info)  # Añadido para mostrar el diccionario después de eliminar el nombre y apellido
print('')  # Añadido para mantener el formato de salida limpio
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
#Agregar un valor a una clave definida como un conjunto de tipo "Lista"
person['job_title'] = 'Instructor'
person['skills'].append('HTML') #permite append porque Skills es un conjunto "Lista" no un "Set" no una "Tupla"
print(person)
##Actualizar el valor de una clave
print('Nombre es: ' , person['first_name'])
person['first_name'] = 'Jaibol'
print('Ahora nombre es:' , person['first_name']) 
##Eliminar una clave y valor del diccionario
person.pop('country')
print(person)
alumno={ 
'nombres':['Pedro', 'Jose'],
'apellidos':['Perez','Medina'],
'edad':'22',
'Nota':'18'
}
print ( alumno )
#Cambiar de Lista a tuplas
print ( alumno.items () )
#eliminar un diccionario
del alumno
dic1 = {
'serial':'0001',
'Descripcion':'Arroz',
'Precio': '5 bs'
}
print(dic1)
#Copiar un diccionario
dic1_copia = dic1.copy() 
print(dic1_copia)
#Listar las Claves de un diccionario
print (dic1.keys())
#Listar los Valores de un diccionario
print (dic1.values())

##Buscar una Clave (Key) en un diccionario
print('Primer_nombre' in person ) #Imprime False
print("first_name" in person ) #Imprime True

print(person)# Imprime {'first_name': 'Jaibol', 'last_name': 'Yetayeh', 'age': 250, 'is_marred': True, 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python', 'HTML'], 'address': {'street': 'Space street', 'zipcode': '02210'}, 'job_title': 'Instructor'}

#Limpiar un diccionario
person.clear()
print(person)

#Eliminar un diccionario
del person
#print(person)


animales = {
'nombre': 'gato',
'tipo': 'mamifero'
}

print(animales.items()) #imprime Claves y Valores
print(animales.values()) #imprime Valores
print(animales.keys()) #imprime Claves

print(animales.popitem()) #imprime el ultimo valor y la ultima Clave
print(animales.__len__()) #imprime un entero con el número de   
print(animales.clear())#Limpia el diccionario


