import cv2
print(cv2.__version__)
dispW = 640
dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps

flip = 2

#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#picam = cv2.VideoCapture(camSet)
webcam = cv2.VideoCapture(2)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
while True:
    #ret, frame1 = picam.read()
    ret, frame2 = webcam.read()
    #frame2 = cv2.resize(frame2, (dispW, dispH))
    frame2 = cv2.flip(frame2, flip)
    #cv2.imshow('piCam', frame1)
    cv2.imshow('WebCam', frame2)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()