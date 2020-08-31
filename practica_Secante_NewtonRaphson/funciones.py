'''
Para ver algunos otros codigos, visitar el sigiente repositorio:
https://github.com/carlos-paezf/Metodos_Numericos_Python
'''

from math import *
import numpy as np
import matplotlib.pyplot as plt


def pol1(x):
  return (x**3) - (3*x) - 4


def pol1d(x):
  return 3*x**2 - 3


def pol2(x):
  return (x**3) + (2*x**2) + (10*x) - 20


def pol2d(x):
  return 3*x**2 + 4*x + 10


def ln1(x):
  return np.log(x-1) + 2*np.cos(x-1)


def ln1d(x):
  return 1/(x-1) - 2*np.sin(x-1)


def trig(x):
  return np.sin(x)


def trigd(x):
  return np.cos(x)


def exp(x):
  return np.exp(x) + 2*np.cos(x) -6


def expd(x):
  return np.exp(x) -2*np.sin(x)
