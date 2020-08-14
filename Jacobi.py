#Implementación del método de Jacobi y algunos casos de salida


from math import *
from pprint import pprint


def distinf(x, y):
	return max([abs(x[i]-y[i]) for i in range(len(x))])


def Jacobi(A, b, x0, TOL, MAX):
	n = len(A)
	x = [0.0 for x in range(n)]
	k = 1
	while k <= MAX:
		for i in range(n):
			if abs(A[i][i]) <= 1e-15:
				print ('Imposible iterar\n')
				return
			s = sum([A[i][j]*x0[j] for j in range(n) if j != i])
			x[i] = (b[i]-float(s))/float(A[i][i])
		pprint(x)
		if distinf(x, x0) < TOL:
			print ('Solución encontrada\n\n')
			return
		k += 1
		for i in range(n):
			x0[i] = x[i]
	print ('Iteraciones agotadas\n')
	return


A = [[2,1],[5,7]]
b = [11,13]
x0 = [1,1]
print ('Matriz A:')
pprint(A)
print ('\nVector b:')
pprint(b)
print ('\nSemilla x0:')
pprint(x0)
print ('\n'+r'Iteración de Jacobi')
#	TOL = 10^-5,	MAX = 50
Jacobi(A, b, x0, 1e-5, 50)


A = [[10,-1, 2], [-1,11,-1], [2,-1,10]]
b = [6,25,-11]
x0 = [0,0,0]
print ('Matriz A:')
pprint(A)
print ('\nVector b:')
pprint(b)
print ('\nSemilla x0:')
pprint(x0)
print ('\n'+r'Iteración de Jacobi')
#	TOL = 10^-10,	MAX = 50
Jacobi(A, b, x0, 1e-10, 50)




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.