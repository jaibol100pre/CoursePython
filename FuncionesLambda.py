'''
Funciones Lambda o funciones anónimas se utilizan en python para abreviar, hacer que la sintaxis
sea mas ligera y entendible.
Todo lo que se puede hacer con una función se puede hacer con una función Lambda 
No simpre una función normal se puede resumir  en lamda, por ejemplo cuando tinene bucle anidados 
pero no al revez
.'''

'''def area_triandulo (base,altura):
    return (base*altura)/2

triangulo1=area_triandulo(25,5)
triangulo2=area_triandulo(50,15)

'''''
'''
print(triangulo1)
print(triangulo2)
'''

area_triangulo=lambda base,altura: (base*altura)/2

#Una funciones lambda revuelve un resultado nunca podrá tener bucles
triangulo1=area_triangulo(25,5)
triangulo2=area_triangulo(50,15)
print(triangulo1)
print(triangulo2)

al_cubo=lambda num:pow(num,3)
print(al_cubo(3))


