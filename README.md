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
