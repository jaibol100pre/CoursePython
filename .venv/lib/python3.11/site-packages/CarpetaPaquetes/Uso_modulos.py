'''Sintaxis:
NombredelDirectorioDondeEstanLosModulos.NombredelModulo import NombreFuncion
NombredelDirectorioDondeEstanLosModulos.NombredelModulo import NombreClass
NombredelDirectorioDondeEstanLosModulos.NombredelModulo import *     <-----importa todo per consume más espacio en memoria
NombredelDirectorioDondeEstanLosModulos=Paquetes
'''

from CarpetaPaquetes.CalculosGenerales import dividir
dividir(4,6)


#from NombreCarpetaRaiz.Archivo-o-modulo import Nombre-Funcion
from CarpetaPaquetes.CalculosGenerales import redondear
redondear(4.5252525256)


#Importar desde un SubMódulo o Subdiurectorio

#from NombreCarpetaRaiz.NombreSubDirectorio.Archivo-o-modulo import Nombre-Funcion
from CarpetaPaquetes.SubModulos.redondeo import redondear 
redondear(6.66666666666666666666666666666666)


from CarpetaPaquetes.SubModulos.Calcular.CalculaEdad import calculaEdad

edad=calculaEdad()

print("Tu edad es: " , edad)
