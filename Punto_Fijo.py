#Implementacion del método del punto fijo y algunos casos de salida


from math import *


def pote(x):
	return pow(2.0, -x)
	# retorna pote(x) = 2^-x


def pol(x):
	return (x**2-1)/3
	# retorna pol(x) = (x2^ - 1) / 3


def puntofijo(f, p0, tol, n):
	i = 1
	while i <= n:
		p = f(p0)
		print ("Iteraccion = ", "%03d" %i, "; p = ", "%.14f" %p)
		if abs(p-p0)<tol:
			return p
		p0 = p
		i += 1
	print ("Iteracciones agotadas:. Error!!!")
	return


#	pol(x), p0=0.9, Tol=10^-10, No=100
print ("\n",r"-- Punto fijo función pol(x):"+"\n")
puntofijo(pol, 0.9, 10e-10, 100)


#	pote(x), p0=0.5, Tol=10^-8, No=100
print ("\n",r"-- Punto fijo funcion pote(x):"+"\n")
puntofijo(pote, 0.5, 10e-10, 100)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.