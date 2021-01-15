import tkinter as tk
import numpy as np
from PIL import Image, ImageTk
import time

# %% Get x values and the sine wave
def sinewave(szX,szY,period,phase):
    x = np.arange(0, szX)
  
    ons  = np.ones([szY,1])
    x_2 = np.matmul(ons,[x])

    angfreq = 2*np.pi/period
    y  = np.cos(angfreq*x_2 + phase)
    return y


# %% Variables
phase = [0, 2*np.pi/3, 4*np.pi/3]
period = 50 #Sinewave period
szX = 854 #Size in x direction
szY = 480 #Size in y direction



# %% Make canvas
root = tk.Tk()
#OPTOMA LV130 Mini Projector has screen size: WVGA (854 x 480)
#The 1920 is my screen width, 
root.geometry("854x480+1910+0") 

canvas = tk.Canvas(root,width=854,height=480)
canvas.pack()



# %% Run loop to show patterns
for a,phs in enumerate(phase):
    array = sinewave(szX, szY,period,phs)
    array = array*128 + 127 #Must scale between -1 to 1 and 0 to 255 
    
    img =  ImageTk.PhotoImage(Image.fromarray(array))
    canvas.create_image(0, 0, anchor="nw", image=img)
    
    root.update() # Show plot
    time.sleep(1.0)    # Pause 

root.destroy()


