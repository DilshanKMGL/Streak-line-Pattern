# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 09:07:47 2019

@author: Lahiru Dilshan
"""
import flow_initial
import joukowiski
import plot_fun
import flow


import numpy as np
import time

# calculate time
start = time.time()

# define circle center
a = 2.0                                 # transfoormation constant
x_cir, y_cir = -0.2, 0.2                # circle center x and y 
cor_cir = complex(x_cir, y_cir)         # convert center into complex number
r = np.sqrt(y_cir**2 + (a - x_cir)**2)  # calculate the corresponding r

flow_init = []
vel = 5.0   # freestream
aoa = -6.0   # freestream
x_vor, y_vor = x_cir, y_cir # vortex
end_condition = -2.00

while aoa<= end_condition:
    cir_com_cor = joukowiski.circle(cor_cir, a)
    jou = joukowiski.get_z(cir_com_cor, a)
    
    flow_initial.create_freestream(vel, aoa, r, cor_cir, a, y_cir, flow_init) # define freestream
    flow_initial.create_vortex(x_vor, y_vor, r, a, y_cir, flow_init) # define vortex
    stren_req = flow_initial.get_strength(flow_init)
    print stren_req
    flow_m = []
    
    delt = 0.025                # time step
    n_strline = 20           # number of streamlines
    x_start, x_end = -6.0, 8.0  # limit of the x axis
    y_start, y_end = -5.0, 5.0  # limit of the y axis
    
    flow.create_freestream(vel, aoa, r, a, cor_cir, flow_m)
    flow.create_vortex(stren_req, x_vor, y_vor, r, a, flow_m)
    x_z, y_z = flow.create_plot_val(x_start, x_end, y_start, y_end, n_strline, delt, flow_m, a, cor_cir, r, jou, aoa)
    # plotting values are in flow.create_plot_val
    #plot_fun.plot_jou(jou, x_z, y_z, x_start, x_end, y_start, y_end)

    aoa += 2
    
    
# calculate time
end = time.time()
print 'time:', (end-start), 's'
