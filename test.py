# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 10:20:01 2019

@author: Lahiru Dilshan
"""
import numpy as np
from matplotlib import pyplot as plt
import joukowiski


a = 2.0                                 # transfoormation constant
x_cir, y_cir = -0.2, 0.2                # circle center x and y 
cor_cir = complex(x_cir, y_cir)         # convert center into complex number
r = np.sqrt(y_cir**2 + (a - x_cir)**2)  # calculate the corresponding r

x_min = x_cir-r

print 'radius',r
print 'x_min',x_min
x, y = -4.1, 0.0

'''

#x1, y1 = joukowiski.maptozeta(x,y,a)
#x1 =float(x1)
#y1 =float(y1)
#print 'x1',x1,'y1',y1
'''
z1, z2 = joukowiski.maptozeta(x,y,a)
z1 = complex(z1)
z2 = complex(z2)
print 'z1 - green',z1
print 'z2 - red',z2

title = '(x, y) = ('+str(x)+' , '+str(y)+')\n'+ 'z1 - green' + str(z1)+' & '+'z2 - red' + str(z2)+'\n'+'x_min = '+str(x_min)

r = np.sqrt(cor_cir.imag**2 + (a - cor_cir.real)**2)
theta = np.linspace(0, 2.0*np.pi, 200000)
cir = cor_cir + r*np.exp(1j * theta)
cir = np.array(cir)
cir_x = cir.real
cir_y = cir.imag
width = 10.0
height = width
plt.figure(figsize= (width, height))
plt.grid(False)
plt.title(title)
plt.xlabel('x', fontsize = 16)
plt.ylabel('y', fontsize = 16)
plt.gca().set_aspect('equal', adjustable='box')
plt.plot(cir_x, cir_y)

plt.scatter(z1.real, z1.imag, color= 'g')
plt.scatter(z2.real, z2.imag, color= 'r')
'''
def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

z1 = 4+5j
z2 = 5+5j
p = 5+6j
print find_nearest([z1, z2], p)
'''