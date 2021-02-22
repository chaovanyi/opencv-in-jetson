import cv2
print(cv2.__version__)

dispW = 320
dispH = 240 #60fps

#dispW = 640
#dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps
flip = 2

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

face_cascade = cv2.CascadeClassifier('/home/jetbot/pycode/resources/face.xml')
eye_cascade = cv2.CascadeClassifier('/home/jetbot/pycode/resources/eye.xml')

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (xE,yE,wE,hE) in eyes:
            cv2.rectangle(roi_color,(xE,yE),(xE+wE,yE+hE),(0,255,0),2)


    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()