""" Plotting a series of sinewaves for Angus

Steven Johnson UofGlasgow Nov 2020
"""

import numpy as np
import matplotlib.pyplot as plt

# Variables
phase = [0, 2*np.pi/3, 4*np.pi/3]
period = 50 #Sinewave period
szX = 320 #Size in x direction
szY = 240 #Size in y direction
height = 6 #Obj height

obj = np.zeros([szY,szX]);
obj[100:200,150:200] = height;


# Get x values and the sine wave
def sinewave(szX,period,phase,obj):
    x = np.arange(0, szX)
    ons  = np.ones([szY,1])
    x_2 = np.matmul(ons,[x])

    angfreq = 2*np.pi/period
    #I1 = Ixy +(IIxy(cos(phi(x)+phsae))) 
    y  = np.cos(angfreq*x_2+ obj +phase)
    return y

# Plot for each value of phase
I = {}
axes  = []
fig=plt.figure()
for a,phs in enumerate(phase):
    # Create 2D array from sinewave
    I[a] = sinewave(szX, period, phs,obj)
    
    # Image the pattern
    axes.append(fig.add_subplot(1, 3, a+1) )
    plt.imshow(I.get(a), cmap='gray', vmin=-1, vmax=1)
#fig.tight_layout()
plt.show()

#%%    
depth = np.arctan2(np.sqrt(3)*(I.get(0)-I.get(2)),2*I.get(1)-I.get(0)-I.get(2))
depth_uw = np.unwrap(depth)
plt.imshow(depth_uw)
plt.show()