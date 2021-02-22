import cv2
print(cv2.__version__)
dispW = 640
dispH = 480
flip = 2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
picam = cv2.VideoCapture(camSet)
webcam = cv2.VideoCapture(1)
while True:
    ret, frame1 = picam.read()
    ret, frame2 = webcam.read()
    #frame = cv2.resize(frame, (dispW, dispH))
    frame1 = cv2.flip(frame1, flip)
    cv2.imshow('piCam', frame1)
    cv2.imshow('WebCam', frame2)
    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destoryAllWindows()
