# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:40:15 2019

@author: Lahiru Dilshan
"""
import numpy as np
from matplotlib import pyplot as plt
import freestream
import vortex
import joukowiski
import plot_fun
import copy

def create_freestream(vel, aoa, r, a, center, flow_m): # create freestream object
    print 'create_freestream'
    fs = freestream.Freestream(vel, aoa)
    fs.derivwz(a)
    fs.set_freestream()
    fs.set_image(r, center)
    fs.subxy()
    flow_m.append([0,fs])
    return flow_m

def create_vortex(strength, x_cor, y_cor, r, a, flow_m): # create vortex object
    print 'create_vortex'
    vt = vortex.Vortex(strength, x_cor, y_cor) 
    vt.derivwz(a)
    vt.set_vortex()
    vt.subxy()
    flow_m.append([1,vt])
    return flow_m

def substitute(x_val, y_val, flow_m): # get velocity values
    #print 'substitute'
    u_com = 0
    v_com = 0
    for i in range(len(flow_m)):
        flow_m[i][1].subxyval(x_val, y_val)
    
    for i in range(len(flow_m)):
        if flow_m[i][0] == 0:
            u_com += (flow_m[i][1].u_temp + flow_m[i][1].u_im_temp)
            v_com += (flow_m[i][1].v_temp + flow_m[i][1].v_im_temp)
        else:
            u_com += (flow_m[i][1].u_temp)
            v_com += (flow_m[i][1].v_temp)
    return [u_com, v_com]

def find_nearest(array, value):
    array = np.asarray(array)
    idx = (np.abs(array - value)).argmin()
    return array[idx]

def checkzeta(c, r, z1, z2, x_last, y_last):
    finalize = False
    z = 0
    z1 = complex(z1)
    z2 = complex(z2)
    z_last = complex(x_last, y_last)
    
    d1 = np.sqrt((np.real(c) - np.real(z1))**2 + (np.imag(c) - np.imag(z1))**2)
    d2 = np.sqrt((np.real(c) - np.real(z2))**2 + (np.imag(c) - np.imag(z2))**2)
    
    if d1 >= r and d2 >= r and finalize == False:
        z = find_nearest([z1, z2], z_last)
        finalize = True
    elif d1 >= r and d2 < r and finalize == False:
        z = z1
        finalize = True
    elif d1 < r and d2 >= r and finalize == False:
        z = z2
        finalize = True
    return np.real(z), np.imag(z)

def xy_arraylist(x_start_array, y_start_array, x_start, x_end, y_start, y_end, delt, flow_m, a, c, r, jou, aoa): # calculate new x,y values to plot streaklines
    #print 'xy_arraylist'
    x_array = [x_start_array]
    y_array = [y_start_array]
    con = x_array[-1][-1]
    
    t = 0.0
    plot = 1
    while con < x_end:
        print 'calculating aoa:',aoa,'at t=', t, 'and x value:', con
        u_com = []
        v_com = []
        for i in range(len(x_start_array)):
            z1, z2 = joukowiski.maptozeta(x_start_array[i], y_start_array[i], a)
            x_temp, y_temp = checkzeta(c, r, z1, z2, x_start_array[-1], y_start_array[-1]) #x_start[i], y_start[i]
            velocity = substitute(x_temp, y_temp, flow_m)
            u_com.append(float(velocity[0]))
            v_com.append(float(velocity[1]))
            
        u_com = np.array(u_com)
        v_com = np.array(v_com)
        
        new_x = x_start_array + delt * u_com
        new_y = y_start_array + delt * v_com
        x_start_array, y_start_array = new_x, new_y
        x_array.append(new_x)
        y_array.append(new_y)
        
        jou_new = plot_fun.transpose_airfoil(jou, aoa)
        x_vortex_z_rotate, y_vortex_z_rotate = plot_fun.transpose_array(x_array, y_array, aoa)    
    
        #plot_fun.plot_jou(jou, x_array, y_array, x_start, x_end, y_start, y_end, plot, aoa)
        plot_fun.plot_jou(jou_new, x_vortex_z_rotate, y_vortex_z_rotate, x_start, x_end, y_start, y_end, plot, aoa)
        plot += 1
        
        con = min(x_array[-1])        
        t += delt
        
    return x_array, y_array

def create_plot_val(x_start, x_end, y_start, y_end, n_strline, delt, flow_m, a, c, r, jou, aoa): # create x,y values to plot streaklines
    print 'create_plot_val'
    y_start_array = np.linspace(y_start, y_end, n_strline)
    x_start_array = (x_start-1) * np.ones(len(y_start_array))
    
    x_val, y_val = xy_arraylist(x_start_array, y_start_array, x_start, x_end, y_start, y_end, delt, flow_m, a, c, r, jou, aoa)
    return x_val, y_val

def plot_value(x, y, x_start, x_end, y_start, y_end): # plot x, y values
    print 'plot_value'
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
    
    for i in range(len(x)):
        plt.plot(x[i], y[i], color = 'b', linewidth = 0.5)
    
def plot_cyl(x_circle, y_circle, r, vortex_x, vortex_y): # plot cylinders and vortex centers
    plt.scatter(vortex_x, vortex_y, color='g')
    circle = plt.Circle((x_circle, y_circle), radius=r, color='#CD2305', alpha=0.5)
    plt.gca().add_patch(circle)

    