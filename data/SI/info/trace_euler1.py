# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 14:43:03 2023

@author: Goncalves David
"""
def euler_1(f,k,tau,a,h,omega=1):
    n=int(a/h)
    s=0
    for i in range(n):
        s=(k*h*f(i*h*omega)+tau*s)/(h+tau)
    return s
 
import numpy as np
import matplotlib.pyplot as plt

k=float(input('k='))
tau=float(input('tau='))
n=int(input('n='))
t=float(input('t='))
f=eval(input('f='))
omega=float(input('omega='))
h=t/n

X=[h*i for i in range(n+1)]
Y=[euler_1(f,k,tau,i,h,omega) for i in X]
Y2=[f(omega*i) for i in X]

plt.clf()
plt.plot(X,Y,label='approchée',color='r')
plt.plot(X,Y2,label='entrée',color='b')
plt.legend()
plt.show()
