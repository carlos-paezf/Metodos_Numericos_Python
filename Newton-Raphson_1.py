# Implementación del método Newton-Raphson y algunos casos de salida


import numpy as np
import matplotlib.pyplot as plt


# Hallar la raiz de la función f(x) = x^3 - cos(x)


def f(x):
	return x**3 - np.cos(x)


def Df(x):
	return 3*x**2 + np.sin(x)


x0 = 1
i = 1
'''
for iteracion in range(1, 6):
	x1 = x0 - f(x0) / Df(x0)
	x0 = x1
	print('Iteración', i , 'raiz aproximada:', x0)
	i += 1
'''

error = 10
while error > 1e-10:
	x1 = x0 - f(x0) / Df(x0)
	error = abs(x1 - x0)
	x0 = x1
	print('Iteración', i , 'raiz aproximada:', x0)
	i += 1


x = np.linspace(-1, 1, 100)
plt.plot(x, x**3 - np.cos(x))
plt.plot(x0, f(x0), 'or')
plt.grid()
plt.show()




#Método de Newton-Rhapson con Python. (2015, 9 diciembre). [Vídeo]. 
#YouTube. https://www.youtube.com/watch?v=hP2lgeGmN-0