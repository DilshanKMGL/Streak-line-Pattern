# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:50:49 2019

@author: Lahiru Dilshan
"""
import sympy as sp

class Freestream:
    def __init__(self, vel, aoa):
        self.vel, self.aoa = vel, sp.rad(aoa)
        self.z = sp.symbols('z', real = False)
        self.x, self.y = sp.symbols('x, y', real = True)
                
    def derivwz(self, a):
        self.a = a
        self.mapfun = 1 - (self.a**2 / self.z**2)
        
    def set_freestream(self):
        self.fun = self.vel * self.z * (sp.cos(self.aoa) - 1j * sp.sin(self.aoa))
        self.fun = self.fun.evalf()
        
        self.deriv = sp.diff(self.fun, self.z)/self.mapfun      
        self.u = sp.re(self.deriv)
        self.v = - sp.im(self.deriv)
        
    def set_image(self, r, center):
        self.r = r
        self.center = center
        self.fun_im = self.vel * self.r**2 / (self.z - self.center) * (sp.cos(self.aoa) + 1j * sp.sin(self.aoa))
        self.fun_im = self.fun_im.evalf()
        
        self.deriv_im = sp.diff(self.fun_im, self.z)/self.mapfun
        self.u_im = sp.re(self.deriv_im)
        self.v_im = -sp.im(self.deriv_im)
    
    def subxy(self):
        self.fun = self.fun.subs(self.z, self.x+1j*self.y)
        self.fun_im = self.fun_im.subs(self.z, self.x+1j*self.y)
        
        self.deriv = self.deriv.subs(self.z, self.x+1j*self.y)
        self.deriv_im = self.deriv_im.subs(self.z, self.x+1j*self.y)
        
        self.u = self.u.subs(self.z, self.x+1j*self.y)
        self.v = self.v.subs(self.z, self.x+1j*self.y)
        
        self.u_im = self.u_im.subs(self.z, self.x+1j*self.y)
        self.v_im = self.v_im.subs(self.z, self.x+1j*self.y)        
       
    def subxyval(self, x_val, y_val):
        self.u_temp = self.u.subs([(self.x, x_val),(self.y, y_val)])
        self.v_temp = self.v.subs([(self.x, x_val),(self.y, y_val)])
        self.u_im_temp = self.u_im.subs([(self.x, x_val),(self.y, y_val)])
        self.v_im_temp = self.v_im.subs([(self.x, x_val),(self.y, y_val)])
        
    