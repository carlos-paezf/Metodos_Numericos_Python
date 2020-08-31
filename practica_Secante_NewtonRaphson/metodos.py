'''
Para ver algunos otros codigos, visitar el sigiente repositorio:
https://github.com/carlos-paezf/Metodos_Numericos_Python
'''

from math import *
import numpy as np
import matplotlib.pyplot as plt


#----------------------------Metodo de la secante---------------------------------
def secante(f, p0, p1, tol, n):
  i = 0
  while i <= n:
      p = p1-(f(p1)*(p1-p0))/(f(p1)-f(p0))
      print ("Iteracccion= ", "%01d" %i, 
               " Xi=", "%.5f" %p1, 
               " Xi-1=", "%.5f" %p0, 
               " F(Xi)= ", "%.5f" %f(p1),
               " F(Xi-1)= ", "%.5f" %f(p0),
               " Xi+1= ", "%.5f" %p,
               " |Xi+1 - Xi|=", "%.5f" %abs(p-p1),
               " SIGA"
            )
      if abs(p-p1) < tol:
          return print
      p0 = p1
      p1 = p
      i += 1
  print ("Iteracciones agotadas: Error!!! Amplie el numero de iteracciones")
  return



#---------------------------Metodo de Newton Raphson--------------------------------
def newton_raphson(f, fd, p0, error, tol):
  i = 1
  while error > tol:
    p1 = p0 - f(p0) / fd(p0)
    error = abs(p1 - p0)
    p0 = p1
    print ("Iteraccion= ", "%01d" %i,
            " Xi=", "%0.5f" %p0,
            " F(Xi)= ", "%.5f" %f(p0),
            " F´(xi)=", "%.5f" %fd(p0),
            " Xi+1= ", "%.5f" %p1,
            " E. Rel= ", "%.5f" %error,
            " Raiz aprox= ", "%.5f" %p0,
            " SIGA"
          )
    i += 1
  return
  