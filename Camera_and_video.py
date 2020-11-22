
import cv2

cam = cv2.VideoCapture(1) 
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480)) 
while(True) : 
    ret,frame = cam.read() 
    out.write(frame) 
    cv2.imshow('Single Frame',frame)

    if cv2.waitKey(1) == ord('q'):
        break

grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
cv2.imshow('grey',grey)

cam.release() 
out.release() 
cv2.destroyAllWindows

"""Code for displaying video which is easily adapted for images but i presume 
the easiest way to display a series of phase maps is to create and show a video 
haven't yet managed to get fullscreen but thats due to the resizing seeming to 
create the window to be larger than the actual screens resolution """

vid = cv2.VideoCapture(r'C:\users\user\Desktop\PHYS4028.mp4')

if (vid.isOpened()== False): print("Error opening video stream or file")

while (vid.isOpened()): 
    ret,frame = vid.read()
    if ret == True:
        frame2 = cv2.resize(frame,(1600,900))
        cv2.imshow('Frame', frame2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    else:
        break

vid.release() 
cv2.destroyAllWindows()

#new code for camera, this allows for a snapshot to be taken when the space bar is hit and saves them which could probably be rewritten to automatically take them and analyse them
cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 0
#captures and displays video which allows alignment before taking image
while True:
    ret, frame = cam.read()
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", frame)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # closes it if ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # takes and saves and image if SPACE pressed
        img_name = "Fringe_pattern_{}.png".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
