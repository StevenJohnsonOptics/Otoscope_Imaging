# Otoscope_Imaging
Student project to develop a 3D imaging system for an otoscope
# Code that is now finally working for webcam viewing
import cv2

cam = cv2.VideoCapture(1)
while(True) :
    tf, frame = cam.read()
    cv2.imshow('Single Frame',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord('x') :
        print
cam.release()
cv2.destroyAllWindows
