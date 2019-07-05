# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:16:44 2019

@author: Lahiru Dilshan
"""
# negative signs were changed for both vortex and image of the vortex
import sympy as sp

class Vortex:
    def __init__(self, x_cor, y_cor):                         # initialy create vortex
        self.x_cor, self.y_cor = x_cor, y_cor  # create variables in object
        self.z, self.z_cor = sp.symbols('z, z_cor', real = False)
        self.x, self.y, self.strength = sp.symbols('x, y, strength', real = True)
                
    def set_vortex(self):
        self.fun = - 1j * self.strength / (2*sp.pi) * sp.log(self.z - self.z_cor)
        self.fun = self.fun.evalf()
        
        self.deriv = sp.diff(self.fun, self.z)        
        self.u = sp.re(self.deriv)
        self.v = - sp.im(self.deriv)
      
    def subxyval(self, x_val, y_val):
        self.deriv_temp = self.deriv.subs([(self.z, x_val+1j*y_val),(self.z_cor, self.x_cor+1j*self.y_cor)])
        