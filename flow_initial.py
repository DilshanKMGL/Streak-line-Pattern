# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 16:40:15 2019

@author: Lahiru Dilshan
"""
import sympy as sp

import freestream_initial
import vortex_initial

def create_freestream(vel, aoa, r, center, a, y_val, flow_init): # create freestream object
    print 'create_freestream'
    fs = freestream_initial.Freestream(vel, aoa)
    fs.set_freestream()
    fs.set_image(r, center)
    fs.subxyval(a,0)
    #fs.subxyval(sp.sqrt(r**2-y_val**2), y_val)
    flow_init.append([0,fs])
    return flow_init

def create_vortex(x_cor, y_cor, r, a, y_val, flow_init): # create vortex object
    print 'create_vortex'
    vt = vortex_initial.Vortex(x_cor, y_cor) 
    vt.set_vortex()
    vt.subxyval(a, 0)
    #vt.subxyval(sp.sqrt(r**2-y_val**2), y_val)
    flow_init.append([1,vt])
    return flow_init

def get_strength(flow_init):
    com_potential = 0
    for i in range(len(flow_init)):
        if flow_init[i][0]==0:
            com_potential += flow_init[i][1].deriv_temp + flow_init[i][1].deriv_im_temp
        else:
            com_potential += flow_init[i][1].deriv_temp
    answer = list(sp.solveset(com_potential).evalf())[0]
    return answer
