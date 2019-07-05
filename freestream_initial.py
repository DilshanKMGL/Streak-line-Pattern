# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 19:50:49 2019

@author: Lahiru Dilshan
"""
import sympy as sp

class Freestream:
    def __init__(self, vel, aoa):                           # initially create freestream
        self.vel, self.aoa = vel, sp.rad(aoa)               # create variables, aoa is converted into radians
        self.z = sp.symbols('z', real = False)              # create z complex number
        self.x, self.y = sp.symbols('x, y', real = True)    # create x,y variables. real and imaginery parts of the z
                
    def set_freestream(self):                                                       # create freestream function
        self.fun = self.vel * self.z * (sp.cos(self.aoa) - 1j * sp.sin(self.aoa))   # generate freestream function
        self.fun = self.fun.evalf()                                                 # simplyfy the function
        self.deriv = sp.diff(self.fun, self.z)  # get derivative of the function
        
    def set_image(self, r, center):                                                                         # create image due to circle
        self.r = r                                                                                  # assign radius
        self.center = center
        self.fun_im = self.vel * self.r**2 / (self.z-self.center) * (sp.cos(self.aoa) + 1j * sp.sin(self.aoa))    # create complex potential of image of circle
        self.fun_im = self.fun_im.evalf()                                                           # simplyfy the function
        self.deriv_im = sp.diff(self.fun_im, self.z)    # get derivative of the image
              
    def subxyval(self, x_val, y_val):
        self.deriv_temp = self.deriv.subs([(self.z, x_val+1j*y_val)])
        self.deriv_im_temp = self.deriv_im.subs([(self.z, x_val+1j*y_val)])