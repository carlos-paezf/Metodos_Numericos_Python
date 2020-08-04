#Implementación del método de bisección y algunos casos de salida


from math import *


def pol(x):
	return x**3+4*x**2-10
	# retorna pol(x) = x^3 + 4x^2 -10


def trig(x):
	return x*cos(x-1)-sin(x)
	# retorna trig(x) = xcos(x-1) - sin(x)


def pote(x):
	return pow(7.0, x)-13
	# retorna pote(x) = 7^x - 13


def bisec(f, a, b, tol, n):
	i = 1
	while i <= n:
		p = a+(b-a)/2.0
		print ("Iteracción = ", "%03d" % i, "; p = ", "%.14f" % p)
		if abs(f(p)) <= 1e-15 or (b-a)/2.0 < tol:
			return p
		i += 1
		if f(a)*f(p) > 0:
			a = p
		else:
			b = p
	print ("Iteracciones agotadas: Error!!!")
	return 


#	pol(x), a=1.0, b=2.0, Tol=10^-8, No=100
print ("\n"+r"--Bisección función pol(x):"+"\n")
bisec(pol, 1.0, 2.0, 1e-8, 100)


#	trig(x), a=4.0, b=6.0, Tol=10^-8, No=100
print ("\n"+r"--Bisección función trig(x):"+"\n")
bisec(trig, 4.0, 6.0, 1e-8, 100)


#	pote(x), a=0, b=2.0, Tol=10^-8, No=100
print ("\n"+r"--Bisección función pote(x):"+"\n")
bisec(pote, 0.0, 2.0, 1e-8, 100)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.