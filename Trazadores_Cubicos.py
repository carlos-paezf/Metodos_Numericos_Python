#Implementación de trazadores cúbicos naturales y algunos casos de salida


from math import *


def CubicSplines(datos):
	n = len(datos)-1
	#Inicializar vectores auxiliares
	A = [x[1] for x in datos]
	X = [x[0] for x in datos]
	H = [0.0 for x in range(n)]
	B = [0.0 for x in range(n+1)]
	C = [0.0 for x in range(n+1)]
	D = [0.0 for x in range(n+1)]
	alpha = [0.0 for x in range(n)]
	mu = [0.0 for x in range(n+1)]
	l = [1.0 for x in range(n+1)]
	z = [0.0 for x in range(n+1)]

	#Crear vector H
	for i in range(n):
		H[i] = X[i+1]-X[i]

	#Crear vector alpha
	for i in range(1, n):
		alpha[i] = (3.0/H[i])*(A[i+1]-A[i])-(3.0/H[i-1])*(A[i]-A[i-1])

	#Solucionar sistema tridiagonal
	for i in range(1, n):
		l[i] = 2.0*(X[i+1]-X[i-1])-H[i-1]*mu[i-1]
		mu[i] = float(H[i])/l[i]
		z[i] = (alpha[i]-H[i-1]*z[1-1])/float(l[i])

	#Solucionar sistema tridiagonal
	for  j in range(n-1, -1, -1):
		C[j] = z[j]-mu[j]*C[j+1]
		B[j] = (A[j+1]-A[j])/float(H[j])-H[j]*(C[j+1]+2*C[j])/3.0
		D[j] = (C[j+1]-C[j])/(3.0*H[j])

	#Retornar vectores A, B, C, D
	return A[:-1], B[:-1], C[:-1], D[:-1]


#Datos de prueba (1,2), (2,3), (3,5)
datosPrueba = [(1.0, 2.0), (2.0, 3.0), (3.0, 5.0)]
a, b, c, d = CubicSplines(datosPrueba)
print ("\nVectores de coeficientes:")
print ("A =", a)
print ("B =", b)
print ("C =", c)
print ("D =", d)


#Datos de prueba (0,1), (1,e), (2,e^2) y (3,e^3)
datosPrueba = [(0.0, exp(0.0)), (1.0, exp(1.0)), (2.0, exp(2.0)), (3.0, exp(3.0))]
a, b, c, d = CubicSplines(datosPrueba)
print ("\nVectores de coeficientes:")
print ("A =", a)
print ("B =", b)
print ("C =", c)
print ("D =", d)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.