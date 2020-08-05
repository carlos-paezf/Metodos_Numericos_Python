#Implementacion del método de la secante y algunos casos de salida


from math import *


def trig(x):
	return sin(2/x)
	# retorna trig(x) = sen(2/x)


def pol(x):
	return x**3-2
	# retorna pol(x) = x^3 - 2


def secante(f, p0, p1, tol, n):
	i = 2
	while i <= n:
		p = p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
		print ("Iteracccion = ", "%03d" %i, "; p =", "%.14f" %p)
		if abs(p-p1) < tol:
			return print
		p0 = p1
		p1 = p
		i += 1
	print ("Iteracciones agotadas: Error!!!")
	return 


#	pol(x), p0=-3.0, p1=3.0, Tol=10^-10, No=100
print ("\n"+r"-- Secante función pol(x):"+"\n")
secante(pol, -3.0, 3.0, 1e-10, 100)


#	trig(x), p0=1.1, p1=0.8, Tol=10^-8, No=100
print ("\n"+r"-- Secante función trig(x):"+"\n")
secante(trig, 1.1, 0.8, 10e-8, 100)



#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.