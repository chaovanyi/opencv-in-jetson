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

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    roi=frame[50:250,200:400].copy() #[row,column] .copy() is used when we want the roi remain the same when the original frame is changed
    roiGray = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY)
    roiGray = cv2.cvtColor(roiGray,cv2.COLOR_GRAY2BGR)
    #frame[50:250,200:400]=[255,255,255]
    frame[50:250,200:400]=roiGray

    cv2.imshow('ROI',roi)
    cv2.imshow('WebCam',frame)
    cv2.imshow('GRAY',roiGray)
    cv2.moveWindow('GRAY',705,250)
    cv2.moveWindow('ROI',705,0)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()