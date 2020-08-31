'''
Para ver algunos otros codigos, visitar el sigiente repositorio:
https://github.com/carlos-paezf/Metodos_Numericos_Python
'''

from math import *
import numpy as np
import matplotlib.pyplot as plt
from funciones import *


#-----------------------------Cuadro de subgraficas-----------------------------------------------
plt.subplot(221)  #Graficar varios graficos, 2 filas 2 columnas posicion 1
x = np.linspace(-100, 100, 1000)
plt.plot(x, pol1(x), 'r')
plt.title('f(x)= x^3-3x-4')
plt.grid()

plt.subplot(222)  #Graficar varios graficos, 2 filas 2 columnas posicion 2
x = np.linspace(-5, 5, 1000)
plt.plot(x, pol2(x), 'r')
plt.title('f(x)= x^3+2x^2+10x-20')
plt.grid()

plt.subplot(223)  #Graficar varios graficos, 2 fila 2 columnas posicion 3
x = np.linspace(2, 100, 1000)
plt.plot(x, ln1(x), 'm')
plt.title('f(x)= ln(x-1) + 2cos(x-1)')
plt.grid()

plt.subplot(224)  #Graficar varios graficos, 2 fila 2 columnas posicion 3
x = np.linspace(-20, 20, 1000)
plt.plot(x, trig(x), 'm')
plt.title('f(x)= sin(x)')
plt.grid()

plt.show()


