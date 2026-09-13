# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 18:47:03 2016

@author: Goncalves David
"""
# s représente les bords

def trapezes(f,a,b,n):
    t=a
    p=(b-a)/n
    s=(f(a)+f(b))/2
    
    for i in range(1,n):
      t=t+p
      s=s+f(t)
    return(s*p)
