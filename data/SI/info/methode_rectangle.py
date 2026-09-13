# -*- coding: utf-8 -*-
"""
Created on Thu Aug 11 12:36:26 2016

@author: Goncalves David
"""
def rectangleg(f,a,b,n):#approximation a gauche
    t=a
    p=(b-a)/n
    s=f(t)
    for i in range(n-1):#attention au nb d iteration !!!
      t=t+p
      s=s+f(t)
    return(s*p)

def rectangled(f,a,b,n):#approximation a droite
    p=(b-a)/n
    t=a+p
    s=f(t)
    for i in range(n-1):
      t=t+p
      s=s+f(t)
    return(s*p)
    
def rectanglem(f,a,b,n):#approximation au milieu
    p=(b-a)/n
    t=a+p/2.    
    s=f(t)
    for i in range(n-1):
      t=t+p
      s=s+f(t)
    return(s*p)