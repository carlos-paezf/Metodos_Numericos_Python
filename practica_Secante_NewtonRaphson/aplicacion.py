'''
Para ver algunos otros codigos, visitar el sigiente repositorio:
https://github.com/carlos-paezf/Metodos_Numericos_Python
'''

from math import *
import numpy as np
import matplotlib.pyplot as plt
from metodos import *
from funciones import *


#------------------------------Graficas individuales-----------------------------------------------
#   f(x) = x^3-3x-4, p0=2.0, p1=3.0, Tol=10^-10, No=100
print ("\n\n\n"+r"-- Secante función f(x)= x^3-3x-4 (6 cifras significativas):"+"\n")
secante(pol1, 2.0, 3.0, 1e-10, 100)
print ("\n"+r"-- Newton Raphson función f(x)= x^3-3x-4 (6 cifras significativas):"+"\n")
newton_raphson(pol1, pol1d, 2, 10, 1e-4)
x = np.linspace(2, 2.4, 1000)             #Determinar los limites para el eje x
plt.plot(x, (x**3) - (3*x) -4, 'r')       #Graficar la funcion con la configuracion de x, la funcion y el color
plt.title('f(x)= x^3-3x-4')               #Titulo de la grafica
plt.xlabel("Coordenada X")                
plt.ylabel('Coordenada Y')
plt.grid()
px = 2.1958233454456                      #Punto en x
py = 0                                    #Punto en y
plt.plot([px], [py], 'bo')
nota = plt.annotate('Raiz=(2.19582 , 0)', #Label
  xy=(px,py),                             #Ubicacion del punto
  xycoords='data',                        
  xytext=(2.22, -0.5),                    #Ubicacion del label
  fontsize=12, 
  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))            #Forma de la flecha
plt.show()



#   f(x) = x^3+2x^2+10x-20, p0=1.0, p1=2.0, Tol=10^-3, No=100
print ("\n\n\n"+r"-- Secante función f(x)= x^3+2x^2+10x-20 (6 cifras significativas):"+"\n")
secante(pol2, 1.0, 2.0, 1e-3, 100)
print ("\n\n\n"+r"-- Newton Raphson función f(x)= x^3+2x^2+10x-20 (6 cifras significativas):"+"\n")
newton_raphson(pol2, pol2d, 1, 10, 1e-3)
x = np.linspace(1, 2, 1000)             #Determinar los limites para el eje x
plt.plot(x, pol2(x), 'c')       #Graficar la funcion con la configuracion de x, la funcion y el color
plt.title('f(x)= x^3+2x^2+10x-20')               #Titulo de la grafica
plt.xlabel("Coordenada X")                
plt.ylabel('Coordenada Y')
plt.grid()
px = 1.3688081072140                      #Punto en x
py = 0                                    #Punto en y
plt.plot([px], [py], 'bo')
nota = plt.annotate('Raiz=(1.36880 , 0)', #Label
  xy=(px,py),                             #Ubicacion del punto
  xycoords='data',                        
  xytext=(1.5, 0.5),                      #Ubicacion del label
  fontsize=12, 
  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))            #Forma de la flecha
plt.show()



#   f(x) = ln(x-1) + 2cos(x-1), p0=4.0, p1=6.0, Tol=10^-3, No=100
print ("\n\n\n"+r"-- Secante función f(x)= ln(x-1) + 2cos(x-1) (6 cifras significativas):"+"\n")
secante(ln1, 4.0, 6.0, 1e-3, 100)
print ("\n\n\n"+r"-- Newton Raphson función f(x)= ln(x-1) + 2cos(x-1) (6 cifras significativas):"+"\n")
newton_raphson(ln1, ln1d, 4, 10, 1e-3)
x = np.linspace(4, 6, 1000)
plt.plot(x, np.log(x-1) + 2*np.cos(x-1), 'm')
plt.title('f(x)= ln(x-1) + 2cos(x-1)')
plt.xlabel("Coordenada X")
plt.ylabel('Coordenada Y')
plt.grid()
px = 4.9544561103061                      #Punto en x
py = 0                                    #Punto en y
plt.plot([px], [py], 'bo')
nota = plt.annotate('Raiz=(4.95445 , 0)', #Label
  xy=(px,py),                             #Ubicacion del punto
  xycoords='data',                        
  xytext=(4.25, 1.2),                     #Ubicacion del label
  fontsize=12, 
  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))            #Forma de la flecha
plt.show()



#   f(x) = sin(x), p0=2π/3, p1=4π/3, Tol=10^-3, No=100
print ("\n\n\n"+r"-- Secante función f(x)= sin(x) (6 cifras significativas):"+"\n")
secante(trig, (2*np.pi)/3, (4*np.pi)/3, 1e-3, 100)
print ("\n\n\n"+r"-- Newton Raphson función f(x)= sin(x) (6 cifras significativas):"+"\n")
newton_raphson(trig, trigd, (2*np.pi)/3, 10, 1e-3)
x = np.linspace(3, 3.30, 1000)
plt.plot(x, np.sin(x), 'm')
plt.title('f(x)= sin(x)')
plt.xlabel("Coordenada X")
plt.ylabel('Coordenada Y')
plt.grid()
px = np.pi                     			  #Punto en x
py = 0                                    #Punto en y
plt.plot([px], [py], 'bo')
nota = plt.annotate('Raiz=(π , 0)', #Label
  xy=(px,py),                             #Ubicacion del punto
  xycoords='data',                        
  xytext=(3.14, 0.04),                    #Ubicacion del label
  fontsize=12, 
  arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))            #Forma de la flecha
plt.show()
