# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 14:32:06 2023

@author: david.goncalves
"""

import numpy as np
import matplotlib.pyplot as plt

def derive1_avant(f,a,h):
    d=(f(a+h)-f(a))/h
    return d

def derive2_avant(f,a,h):
    d=(f(a+h)-2*f(a)+f(a-h))/h**2
    return d

a=eval(input('borne a='))
b=eval(input('borne b='))
n=int(input('nombre de segments='))
h=(b-a)/n #on définit le pas h
f=eval(input('f='))

X=[a+i*h for i in range(n+1)] # on crée la liste des abscisses
Y=[f(X[i]) for i in range(n+1)] # on crée la liste des ordonnées y=f(x)
Y2=[derive1_avant(f,i,h) for i in X] # on crée la liste des des ordonnées y'(x)
Y3=[derive2_avant(f,i,h) for i in X] # on crée la liste des des ordonnées y''(x)

plt.clf()
plt.plot(X,Y,color='r',label='f')
plt.plot(X,Y2,color='b',label='fprime')
plt.plot(X,Y3,color='g',label='fseconde')

plt.legend()