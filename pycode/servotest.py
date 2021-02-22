import cv2
print(cv2.__version__)
from adafruit_servokit import ServoKit
from time import sleep

myKit = ServoKit(channels=16)

dispW = 320
dispH = 240 #60fps

#dispW = 640
#dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps
flip = 2

def nothing(x):
    pass
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

cv2.namedWindow('WebCam')
cv2.createTrackbar('xVal','WebCam',90,180,nothing) #nothing is a callback function
cv2.createTrackbar('yVal','WebCam',90,180,nothing)
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    xVal = cv2.getTrackbarPos('xVal','WebCam')
    yVal = cv2.getTrackbarPos('yVal','WebCam')
    
    myKit.servo[0].angle = xVal
    myKit.servo[1].angle = yVal

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()