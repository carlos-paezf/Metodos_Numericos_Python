#Implementacion de la recta de mínimos cuadrados


from math import *


def RectaMinSq(datos):
	X = sum([p[0] for p in datos])
	Y = sum([p[1] for p in datos])
	XX = sum([(p[0])**2 for p in datos])
	XY = sum([p[0]*p[1] for p in datos])
	m = len(datos)

	def P(x):	# Recta de Mínimos Cuadrados
		a0 = float(Y*XX-X*XY)/float(m*XX-X**2)
		a1 = float(m*XY-X*Y)/float(m*XX-X**2)
		return a0+a1*x
	return P


def ErrorSq(f, datos):	# Error cuadrático
	E = sum([(p[1]-f(p[0]))**2 for p in datos])
	return E


#Datos de prueba
datos = [(-1.0, 2.0), (0.0, -1.0), (1.0, 1.0), (2.0, -2.0)]
f = RectaMinSq(datos)
print ("Evaluar en x=1:")
print (f(1.0))
print (r"Error cuadrático:")
print (ErrorSq(f, datos),"\n")


#Datos de prueba
datos = [(1.0, 1.3), (2.0, 3.5), (3.0, 4.2), (4.0, 5.0), (5.0, 7.0),
		(6.0, 8.8), (7.0, 10.1), (8.0, 12.5), (9.0, 13.0), (10.0, 15.6)]
print ("Evaluar en x=1:")
print (f(1.0))
print (r"Error cuadrático:")
print (ErrorSq(f, datos),"\n")




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.