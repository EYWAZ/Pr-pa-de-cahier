# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 15:59:28 2025

@author: david.goncalves
"""
def euler_2(f,k,xsi,w0,h,a,omega=1):
    n=int(a/h)
    s2=0
    s1=0
    for i in range(n):
        s0=s1
        s1=s2
        s2=(k*w0**2*h**2*f(omega*i*h)+2*s1*(xsi*h*w0+1)-s0)/(w0**2*h**2+2*xsi*h*w0+1)
    return s1

import numpy as np
import matplotlib.pyplot as plt

f=eval(input('e(t)='))
k=float(input('k='))
xsi=float(input('xsi='))
n=int(input('n='))
t=float(input('t='))
w0=float(input('w0='))
omega=float(input('omega='))

h=t/n
X=[i*h for i in range(n+1)]
Y=[euler_2(f,k,xsi,w0,h,i,omega) for i in X]
Y2=[f(omega*i) for i in X]

plt.clf()
plt.plot(X,Y,label='approchée',color='r')
plt.plot(X,Y2,label='entrée',color='b')
plt.legend()
plt.show()



