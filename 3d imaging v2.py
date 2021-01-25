import cv2
import numpy as np
import matplotlib.pyplot as plt
import time
import tkinter as tk
from PIL import Image, ImageTk
import time


cam = cv2.VideoCapture(0)

def sinewave(resX,resY,period,phase):
    x = np.arange(0, resX)
  
    ons  = np.ones([resY,1])
    x_2 = np.matmul(ons,[x])

    angfreq = 2*np.pi/period
    y  = np.cos(angfreq*x_2 + phase)
    return y



phase = [0, 2*np.pi/3, 4*np.pi/3]
period = 50 #Sinewave period
resX = 1920 #Size in x direction
resY = 1080 #Size in y direction




root = tk.Tk()

root.geometry("1920x1080+1910+0") 

canvas = tk.Canvas(root,width=1920,height=1080)
canvas.pack()

frame = {}


for a,phs in enumerate(phase):
    array = sinewave(resX, resY,period,phs)
    array = array*128 + 127 
    
    img =  ImageTk.PhotoImage(Image.fromarray(array))
    canvas.create_image(0, 0, anchor="nw", image=img)
    
    root.update() # Show plot
    ret,frameOut = cam.read()
    frame[a] = np.sum(frameOut,axis=2)
    time.sleep(1.0)    # Pause 

root.destroy()



depth = np.arctan2(np.sqrt(3)*(frame.get(0)-frame.get(2)),2*frame.get(1)-frame.get(0)-frame.get(2))
depth_uw = np.unwrap(depth)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
y = np.arange(0,480,1)
x = np.arange(0,640,1)
X, Y = np.meshgrid(x, y)
Z = depth_uw.reshape(X.shape)

ax.plot_surface(X, Y, Z)
    
   
   

   
    
#%%

#%%
