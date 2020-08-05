#Implementacion del metodo de Newton y algunos casos de salida


from math import *


def expo(x):
	return x**2+exp(-2*x)-2*x*exp(-x)
	# retorna expo(x)= x^2 + e^-2x - 2xe^-x


def expoprima(x):
	return 2*x-2*exp(-2*x)-2*exp(-x)+2*x*exp(-x)
	# retorna expoprima(x) = d/dx(expo(x))


def trig(x):
	return cos(x)-x
	# retorna trig(x) = cos(x) - x


def trigprima(x):
	return -sin(x)-1
	# retorna trigoprima(x) = d/dx(trig(x))


def newton(f, fprima, p0, tol, n):
	i = 1
	while i <= n:
		p = p0-f(p0)/fprima(p0)
		print("Iteraccion = ", "%03d" %i , "; p = ", "%.14f" %p)
		if abs(p-p0) < tol:
			return p
		p0 = p
		i += 1
		print ("Iteracciones agotadas: Error!!!")
		return 


#	trig(x), trigprima(x), p0=pi/4, Tol=10^-10, No=100
print ("\n"+r"-- Newton función trig(x):"+"\n")
newton(trig, trigprima, pi/4, 1e-10, 100)


#	expo(x), expoprima(x), p0 = 4.0, Tol=10^-8, No=100
print ("\n"+r"-- Newton función expo(x):"+"\n")
newton(expo, expoprima, 4.0, 1e-8, 100)



#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.