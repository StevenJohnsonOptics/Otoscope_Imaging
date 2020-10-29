# Otoscope_Imaging
Student project to develop a 3D imaging system for an otoscope
# Evolved code that now displays webcam, then an editted version and then saves a recording of the original frame

import cv2

cam = cv2.VideoCapture(1)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(True) :
    ret, frame = cam.read()
    out.write(frame)
    cv2.imshow('Single Frame',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break
    
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('grey',grey)
cam.release()
out.release()
cv2.destroyAllWindows

#Code for displaying video which is easily adapted for images but i presume the easiest way to display a series of phase maps is to create and show a video haven't yet managed to get fullscreen but thats due to the resizing seeming to create the window to be larger than the actual screens resolution
import numpy as np
import cv2

vid = cv2.VideoCapture(r'C:\users\user\Desktop\PHYS4028.mp4')
 
if (vid.isOpened()== False):
  print("Error opening video stream or file")
 

while (vid.isOpened()):
    ret, frame = vid.read()
    if ret == True:
 
        frame2 = cv2.resize(frame,(1600,900))
        cv2.imshow('Frame', frame2)
  
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

vid.release()
cv2.destroyAllWindows()

#Ive created 3 phase maps sinusoidally varying from 0 to 255 but when i plot them they arent in gray scale and im not sure how to do that but these are the current 3 phase maps

w=(2*np.pi)/50
Px1 = []
for i in range(801):
    Px1.append(127.5*np.sin(w*i)+127.5)
repetitions = 600
px1 = np.tile(Px1,(repetitions,1))


Px2 = []
for i in range(801):
    Px2.append(127.5*np.sin(w*i+(2*np.pi/3))+127.5)
repetitions = 600
px2 = np.tile(Px2,(repetitions,1))


Px3 = []
for i in range(801):
    Px3.append(127.5*np.sin(w*i+(4*np.pi/3))+127.5)
repetitions = 600
px3 = np.tile(Px3,(repetitions,1))
