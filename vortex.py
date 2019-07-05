# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 10:16:44 2019

@author: Lahiru Dilshan
"""
# negative signs were changed for both vortex and image of the vortex
import sympy as sp

class Vortex:
    def __init__(self, strength, x_cor, y_cor):
        self.strength, self.x_cor, self.y_cor = strength, x_cor, y_cor
        self.z, self.z_cor = sp.symbols('z, z_cor', real = False)
        self.x, self.y = sp.symbols('x, y', real = True)
                
    def derivwz(self, a):
        self.a = a
        self.mapfun = 1 - (self.a**2 / self.z**2)
     
    def set_vortex(self):
        self.fun = - 1j * self.strength / (2*sp.pi) * sp.log(self.z - self.z_cor)
        self.fun = self.fun.evalf()
        
        self.deriv = sp.diff(self.fun, self.z)/self.mapfun       
        self.u = sp.re(self.deriv)
        self.v = - sp.im(self.deriv)
    
    def subxy(self):
        self.fun = self.fun.subs(self.z, self.x+1j*self.y)
        
        self.deriv = self.deriv.subs(self.z, self.x+1j*self.y)
        
        self.u = self.u.subs(self.z, self.x+1j*self.y)
        self.v = self.v.subs(self.z, self.x+1j*self.y)
        
    def subxyval(self, x_val, y_val):
        self.u_temp = self.u.subs([(self.x, x_val),(self.y, y_val),(self.z_cor, self.x_cor+1j*self.y_cor)])
        self.v_temp = self.v.subs([(self.x, x_val),(self.y, y_val),(self.z_cor, self.x_cor+1j*self.y_cor)])
        
        