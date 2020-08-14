#Implementación del método de Verlet y algunos casos de salida


from math import *


def test1(x):		#d^2x/dt^2 = x
	return x


def test2(x):		#d^2x/dt^2 = -x
	return -x


def Verlet(a, b, x0, v0, f, N):
	h = (b-a)/float(N)
	p0 = x0
	p1 = p0 + v0*h + (0.5*f(p0)*h**2)
	print (a, "--->", p0)
	for i in range(1, N+1):
		p = 2.0*p1-p0+f(p1)*h**2
		print (a+i*h, '--->', p1)
		p0 = p1
		p1 = p


#d^2x/dt^2 = x, 	a=0, b=1, x0=1, v0=1, N=20
print ('\n'+r'Método de Verlet'+'\n')
Verlet(0, 1.0, 1.0, 1.0, test1, 20)


#d^2x/dt^2 = -x, 	a=0, b=1, x0=1, v0=0, N=20
print ('\n'+r'Método de Verlet'+'\n')
Verlet(0, 1.0, 1.0, 0, test2, 20)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.