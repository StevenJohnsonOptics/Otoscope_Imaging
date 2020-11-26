import cv2
import numpy as np
import matplotlib.pyplot as plt
import time

cam = cv2.VideoCapture(0)




phase = [0, 2*np.pi/3, 4*np.pi/3]
period = 50 #Sinewave period
#setting x and y values for the fringe patterns according to the resolution of the projector
Xres = 854 
Yres = 480 


# Get x values and the sine wave
def sinewave(Xres,period,phase):
    x = np.arange(0, Xres)
    ons  = np.ones([Yres,1])
    x_2 = np.matmul(ons,[x])

    angfreq = 2*np.pi/period
    #I1 = Ixy +(IIxy(cos(phi(x)+phsae))) 
    y  = np.cos(angfreq*x_2+phase)
    return y

frame = {}
for i,phs in enumerate(phase):
    frame[i] = sinewave(Xres,period,phs)
fig=plt.figure()
fig.canvas.manager.full_screen_toggle()
 # toggle fullscreen mode
k = cv2.waitKey(1)
#displaying the fringe patterns in a loop with time set by plt.pause however the usual command to close this loop with a keystroke does not seem to be working
while True:
    for i in range(3):
        
        plt.imshow(frame[i],cmap='gray', vmin=-1, vmax=1)
        plt.yticks([])
        plt.xticks([])
        plt.tight_layout(pad=0, w_pad=0, h_pad=0)
        plt.pause(1)
    if k == ord('q'):
        break
   
    
   
   

   
    
#%%

#%%
