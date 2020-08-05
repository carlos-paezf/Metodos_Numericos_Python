#	Implementacion del método Regula Falsi y algunos casos de salida


from math import *


def pol(x):
	return x**3+4*x**2-10
	# retorna pol(x) = x^3 + 4x^2 - 10


def trig(x):
	return x*cos(x-1)-sin(x)
	# retorna trig(x) = xcos(x-1) - sin(x)


def pote(x):
	return pow(7.0, x)-13
	# retorna pote(x) = 7^x -13


def regula(f, p0, p1, tol, n):
	i = 2
	while i <= n:
		q0 = f(p0)
		q1 = f(p1)
		p = p1-(q1*(p1-p0))/(q1-q0)
		print ("Iteraccion = ", "%3d" %i, "; p =", "%.14f" % p)
		if abs(p-p1) < tol:
			return p
		i += 1
		q = f(p)
		if q*q1 < 0:
			p0 = p1
			q0 = q1
		p1 = p
		q1 = q
	print ("Iteracciones agotadas: Error!!!")
	return

#	pol(x), a=10, b=20, Tol=10^-8, No=100
print ("\n"+r"-- Regula falsi función pol(x):"+"\n")
regula(pol, 1.0, 2.0, 1e-8, 100)


#	trig(x), a=4.0, b=6.0, Tol=10^-8, No=100
print ("\n"+r"-- Regula falsi función trig(x):"+"\n")
regula(trig, 4.0, 6.0, 10e-8, 100)


#	pote(x), a=0, b=2.0, Tol=10^-8, No=100
print ("\n"+r"-- Regula falsi función pote(x):"+"\n")
regula(pote, 0, 2.0, 10e-8, 100)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.