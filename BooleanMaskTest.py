# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 15:15:09 2020

@author: Steven Johnson
"""

## Boolean Test
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


x = np.arange(-5, 5, 0.1)
y = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x, y)
R = np.sqrt(x**2 + y**2)
z = np.sin(R)

valid = z>0
Z = z[valid]
X = x[valid]
Y = y[valid]

ax.scatter(X,Y,Z)
ax.set_xlabel('X Axes')
ax.set_ylabel('Y Axes')
ax.set_zlabel('Z Axes')



plt.show()