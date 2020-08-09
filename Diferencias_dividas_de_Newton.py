#Implementación del interpolador de Newton y algunos casos de salida


from math import *
from pprint import pprint


def NewtonPol(datos):
	n = len(datos)-1
	F = [[0 for x in datos] for x in datos]			#Crear tabla nula

	for i, p in enumerate(datos):					#Condiciones iniciales
		F[i][0] = p[1]

	for i in range(1, n+1):							#Tabla de diferencias dividida
		for j in range(1, i+1):
			F[i][j] = (F[i][j-1]-F[i-1][j-1]) / (datos[i][0]-datos[i-j][0])

	def L(k, x):									#Polinomio L~k(x) = Π~i<=k	(x - x~i)
		out = 1.0
		for i, p in enumerate(datos):
			if i <= k:
				out *= (x-p[0])
		return out

	def P(x):										#P(x) = f|x~0| + Σ(^n)(~k=1) f[x~0, x~1, ..., x~k] L(~k-1)(x)
		newt = 0.0
		for i in range(1, n+1):
			newt += F[i][j]*L(i-1, x)
		return newt + F[0][0]

	return F, P


datost = [(-1.0, 3.0), (0.0, -4.0), (1.0, 5.0), (2.0, -6.0)]
T, P = NewtonPol(datost)
print ("\nTabla de diferencias divididas:")
pprint(T)
print ("\nEvaluar el pol en x=0")
print (P(0.0))


datosf = [(2.0, 1.0/2.0), (11.0/4.0, 4.0/11.0), (4.0, 1.0/4.0)]
T, P = NewtonPol(datosf)
print ("\nTabla de diferencias divididas:")
pprint(T)
print ("\nEvaluar el polinomio en x=3")
print (P(3.0))




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.