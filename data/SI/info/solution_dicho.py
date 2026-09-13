# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

@author: Goncalves David
"""

def zero_dicho(f,a,b,epsi):
    assert f(a)*f(b) <= 0 and epsi>0
    g,d=a,b #permet de conserver les bornes initiales
        
    while d-g>2*epsi:
        m=(g+d)/2.
        if f(g)*f(m) <= 0:
            d=m # on decale la borne de droite
        else:
            g=m # on decale la borne de gauche
    return m
        

            
    