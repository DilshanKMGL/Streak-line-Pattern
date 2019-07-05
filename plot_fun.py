# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 08:44:13 2019

@author: Lahiru Dilshan
"""
from matplotlib import pyplot as plt
import numpy as np

def plot_jou(jou, x_z, y_z, x_start, x_end, y_start, y_end, plot, aoa):
    x_z = np.array(x_z).transpose()                                                         # make x transpose
    y_z = np.array(y_z).transpose()                                                         # make y transpose
    
    jou_x = jou.real
    jou_y = jou.imag
    
    heading = 'Joukowiski airfoil aoa ' +str(aoa) + ' #' + str(plot)+'.png'
    
    #f = plt.figure()
    width = 10.0
    height = width
    plt.figure(figsize= (width, height))
    plt.grid(False)
    plt.xlabel('x', fontsize = 16)
    plt.ylabel('y', fontsize = 16)
    
    # different methods to get equalized scale
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.plot(jou_x, jou_y, color = 'b')
    
    for i in range(len(x_z)):
        plt.plot(x_z[i], y_z[i], color = 'b', linewidth = 0.5)
    
    plt.savefig(heading)
    plt.close()
    #f.show()

def airfoil(jou):
    #heading = str(i)
    jou_x = jou.real
    jou_y = jou.imag
    
    plt.figure()
    plt.plot(jou_x, jou_y, color = 'b')
    plt.gca().set_aspect('equal', adjustable='box')
    #plt.scatter(vortex_cor_x, vortex_cor_y, s=5, color = 'g')
    #plt.savefig(heading)
    #plt.close()
    
def transpose_airfoil(jou, aoa): # rotate only airfoil. if use for heaving modify this
    aoa = np.deg2rad(aoa)# sp.rad(aoa)
    jou_new = np.exp(- 1j * aoa) * jou
    return jou_new

def transpose_array(x_array, y_array, aoa):
    x_array_new = []
    y_array_new = []
    aoa = np.deg2rad(aoa)
    for i in range(len(x_array)):
        temp_x = []
        temp_y = []
        for j in range(len(x_array[i])):
            #print x_array[i][j], y_array[i][j]
            com = complex(x_array[i][j], y_array[i][j])
            new = np.exp(- 1j * aoa) * com
            
            temp_x.append(new.real)
            temp_y.append(new.imag)
            
        x_array_new.append(temp_x)
        y_array_new.append(temp_y)
        
    return x_array_new, y_array_new

def plot_cir(cir, cir_center, a, x_zeta, y_zeta, x_start, x_end, y_start, y_end):
    print 'plot_value'
    
    #f = plt.figure()
    width = 10.0
    height = width
    plt.figure(figsize= (width, height))
    plt.grid(False)
    plt.xlabel('x', fontsize = 16)
    plt.ylabel('y', fontsize = 16)
    
    # different methods to get equalized scale
    plt.xlim(x_start, x_end)
    plt.ylim(y_start, y_end)
    plt.gca().set_aspect('equal', adjustable='box')
    
    
    for i in range(len(x_zeta)):
        plt.plot(x_zeta[i], y_zeta[i], color = 'b', linewidth = 0.5)
    
        
    cir_x = cir.real
    cir_y = cir.imag
    x_array = [cir_center.real, -a, +a]
    y_array = [cir_center.imag, 0, 0]
    
    heading = 'mapped circle.png.png'
    plt.gca().set_aspect('equal', adjustable='box')
    plt.plot(cir_x, cir_y)
    plt.scatter(x_array, y_array, s=10, color = 'g')
    #plt.savefig(heading)
    #plt.close(f)
    #f.show()