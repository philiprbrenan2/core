#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 18:28:22 2019

@author: Daniel.Ibanez
"""
import numpy as np
from matplotlib import pyplot as plt

from vita.modules.fiesta import FieldLine
#filepath = "T:\\USERS\\J_Wood\\STF1_equilibriums\\export_R200.mat"
#filepath = "/home/daniel.iglesias/Simulations/plasma_scenarios/ST-F1/ST200/python_responses/export_R200.mat"
filepath = '/home/jmbols/Postdoc/export_R200.mat'
field_line = FieldLine(filepath)
R = field_line.fiesta_equil.get_midplane_lcfs()
r0 = 0.6
rf = 1.
midplane_range = np.linspace(r0,rf,10)
points = []
lengths = []
for r in midplane_range:
    points.append( [r,0,0] )
    lengths.append( 120 )
print(lengths)
field_line_dict = []
for idx, val in enumerate(points):
    field_line_dict.append(field_line.follow_field_in_plane(val, lengths[idx], break_at_limiter=False))
#    p1 = [3.15,0,0]
#    field_line_dict.append( field_line.followFieldinPlane(p0=p1, maxl=40.0) )
f, ax = plt.subplots(1)
for i in field_line_dict:
    ax.plot(i['R'],i['Z'])
    ax.plot(i['R'],i['Z'])
f.gca().set_aspect('equal', adjustable='box')
f.gca().set_ylim([0,4])
plt.show(block=True)
print (len(field_line_dict))
