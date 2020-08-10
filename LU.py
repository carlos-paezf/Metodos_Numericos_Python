#Sistemas de ecuaciones
#Implementación del método LU y algunos casos de salida


from math import *
from pprint import pprint


def lu(A):
	n = len(A)
	# Crear matrices nulas
	L = [[0.0 for x in range(n)] for x in range(n)]
	U = [[0.0 for x in range(n)] for x in range(n)]

	# Doolittle
	L[0][0] = 1.0
	U[0][0] = float(A[0][0])

	if abs(L[0][0]*U[0][0]) <= 1e-15:
		print ("Imposible descomponer")
		return

	for j in range(1, n):
		U[0][j] = A[0][j]/L[0][0]
		L[j][0] = A[j][0]/U[0][0]

	for i in range(1, n-1):
		L[i][i] = 1.0
		s = sum([L[i][k]*U[k][i] for k in range(i)])
		U[i][i] = float(A[i][i])-float(s)

		if abs(L[i][i]*U[i][i]) <= 1e-15:
			print ("Imposible descomponer")
			return

		for j in range(i+1, n):
			s1 = sum([L[i][k]*U[k][j] for k in range(i)])
			s2 = sum([L[i][k]*U[k][j] for k in range(i)])
			U[i][j] = float(A[i][j])-float(s1)
			L[j][i] = (float(A[j][i])-float(s2))/float(U[i][i])

	L[n-1][n-1] = 1.0
	s3 = sum([L[n-1][k]*U[k][n-1] for k in range(n)])
	U[n-1][n-1] = float(A[n-1][n-1])-float(s3)

	if abs(L[n-1][n-1]*U[n-1][n-1]) <= 1e-15:
		print ("Imposible descomponer")
		return

	print ("\nMatriz L:")
	pprint(L)
	print ("\nMatriz U:")
	pprint(U)


A = [[4, 3], [6, 3]]
print ("Matriz A:")
pprint(A)
print (lu(A))
print ("------------------")

A = [[0, 1], [1, 1]]
print ("Matriz A:")
pprint(A)
print (lu(A))
print ("------------------")

A = [[3, 1, 6], [-6, 0, -16], [0, 8, -17]]
print ("Matriz A:")
pprint(A)
print (lu(A))
print ("------------------")

A = [[1, 2, 3], [2, 4, 5], [1, 3, 4]]
print ("Matriz A:")
pprint(A)
print (lu(A))
print ("------------------")




#Ovalle, D. A., Yermanos, M. Á. B., & Restrepo, J. A. P. (2017). 
#Matemáticas para Ingeniería: Métodos numéricos con Python. 
#Institución Universitaria Politécnico Grancolombiano.