#Implementación del Método Euler y algunos casos de salida


from math import *


def test1(t, y):
	return y-t**2+1


def test2(t, y):
	return 2.0-exp(-4*t)-2*y


def Euler(a, b, y0, f, N):
	h = (b-a)/float(N)
	t = a
	w = y0
	print (t, "-->", w)
	for i in range(1, N+1):
		w = w+h*f(t, w)
		t = a+i*h
		print (t, "-->", w)


#	dy/dt = y - t^2 + 1,	a=0, b=2, y0=0.5, N=10
print ("\n"+r"--Método de Euler"+"\n")
Euler(0, 2, 0.5, test1, 10)


#	dy/dt = 2 - e^-4t -2y, 	a=0, b=1, y0=1, N=20
print ("\n"+r"--Método de Euler"+"\n")
Euler(0, 1, 1, test2, 20)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.