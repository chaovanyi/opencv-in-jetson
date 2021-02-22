import cv2
import numpy as np
print(cv2.__version__)

#dispW = 320
#dispH = 240 #60fps

dispW = 640
dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps
flip = 2

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

blank = np.zeros([480,640,1],np.uint8)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    #b = cv2.split(frame)[0]
    #g = cv2.split(frame)[1] #we can write in one line
    #r = cv2.split(frame)[2]

    b,g,r = cv2.split(frame)

    blue = cv2.merge((b,blank,blank))
    green = cv2.merge((blank,g,blank))
    red = cv2.merge((blank,blank,r))

    cv2.imshow('blue',blue)
    cv2.moveWindow('blue',705,0)
    cv2.imshow('green',green)
    cv2.moveWindow('green',0,500)
    cv2.imshow('red',red)
    cv2.moveWindow('red',705,500)


    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()