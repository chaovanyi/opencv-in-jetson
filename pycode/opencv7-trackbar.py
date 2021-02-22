import cv2
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

def nothing(x):
    pass
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

cv2.namedWindow('WebCam')
cv2.createTrackbar('xVal','WebCam',25,dispW,nothing) #nothing is a callback function
cv2.createTrackbar('yVal','WebCam',25,dispH,nothing)
while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    xVal = cv2.getTrackbarPos('xVal','WebCam')
    yVal = cv2.getTrackbarPos('yVal','WebCam')
    #print(xVal,yVal)
    cv2.circle(frame,(xVal,yVal),5,(255,0,0),-1)

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()