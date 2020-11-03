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


# Get x values and the sine wave
def sinewave(szX,period,phase):
    x = np.arange(0, szX)
    angfreq = 2*np.pi/period
    y  = np.sin(angfreq*x+phase)
    return y

# Plot for each value of phase
axes  = []
fig=plt.figure()
for a,phs in enumerate(phase):
    # Create 2D array from sinewave
    y = sinewave(szX, period, phs)
    ons  = np.ones([szY,1])
    pattern = np.matmul(ons,[y])

    # Image the pattern
    axes.append(fig.add_subplot(1, 3, a+1) )
    plt.imshow(pattern, cmap='gray', vmin=-1, vmax=1)
    
fig.tight_layout()
plt.show()