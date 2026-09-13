# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:56:02 2025

@author: Goncalves David
"""

def sol_newton(f,g,u0,epsi):
    u=u0
       
    while f(u)>=abs(epsi):
        u=u-f(u)/g(u)
    return u


