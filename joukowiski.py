# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:04:20 2019

@author: Lahiru Dilshan
"""
import numpy as np
import sympy as sp

def get_z(z, a):
    return z + a**2/z

def jou_trans(cir, a):
    jou = []
    for i in range(len(cir)):
        jou.append(get_z(cir[i], a))
    jou = np.array(jou)
    return jou

def circle(c, a):
    r = np.sqrt(c.imag**2 + (a - c.real)**2)
    theta = np.linspace(0, 2.0*np.pi, 200000)
    cir = c + r*np.exp(1j * theta)
    cir = np.array(cir)
    return cir

def maptoz(x_zeta, y_zeta, a):
    x_z = []
    y_z = []
    
    z = x_zeta + 1j * y_zeta
    z = get_z(z, a)
    x_z = z.real
    y_z = z.imag
    
    return x_z, y_z

def maptozeta(x_z, y_z, a):
    z_z = complex(x_z, y_z)
    zeta1 = ((z_z + sp.sqrt(z_z**2 - 4*a**2))/2).evalf()
    zeta2 = ((z_z - sp.sqrt(z_z**2 - 4*a**2))/2).evalf()
    #return sp.re(zeta2), sp.im(zeta2)
    return zeta1, zeta2