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

img1 = np.zeros((480,640,1),np.uint8) #black window
img1[0:480,0:320] = [255]

img2 = np.zeros((480,640,1),np.uint8)
img2[190:290,270:370]=[255]

bitAnd = cv2.bitwise_and(img1,img2)
bitOr = cv2.bitwise_or(img1,img2)
bitXor = cv2.bitwise_xor(img1,img2)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    frame = cv2.bitwise_and(frame,frame,mask = bitXor)


    cv2.imshow('WebCam',frame)
    cv2.imshow('img1',img1)
    cv2.imshow('img2',img2)
    cv2.imshow('AND',bitAnd)
    cv2.imshow('OR',bitOr)
    cv2.imshow('XOR',bitXor)
    cv2.moveWindow('WebCam',0,0)
    cv2.moveWindow('img1',0,530)
    cv2.moveWindow('img2',705,0)
    cv2.moveWindow('AND',705,530)
    cv2.moveWindow('OR',1340,0)
    cv2.moveWindow('XOR',1340,530)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()