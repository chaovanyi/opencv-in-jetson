import cv2
print(cv2.__version__)
from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)

pan = 90
tilt = 90
kit.servo[0].angle = pan
kit.servo[1].angle = tilt

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

face_cascade = cv2.CascadeClassifier('/home/jetbot/pycode/resources/face.xml')
eye_cascade = cv2.CascadeClassifier('/home/jetbot/pycode/resources/eye.xml')

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray,1.3,5)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

        centerX = x + w/2
        centerY = y + h/2

        errorPan = centerX - dispW/2
        errorTilt = centerY - dispH/2

        if abs(errorPan) > 15:
            pan = pan + errorPan/50
        if abs(errorTilt) > 15:
            tilt = tilt - errorTilt/50

        if pan > 180:
            pan = 180
            print('Pan is out of range!')
        if tilt > 180:
            tilt = 180
            print('tilt is out of range!')
        if pan < 0:
            pan = 0
            print('pan is out of range!')
        if tilt < 0:
            tilt = 0
            print('tilt is out of range!')

        kit.servo[0].angle = pan
        kit.servo[1].angle = tilt

        roi_gray = gray[y:y+h,x:x+w]
        roi_color = frame[y:y+h,x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (xE,yE,wE,hE) in eyes:
            cv2.rectangle(roi_color,(xE,yE),(xE+wE,yE+hE),(0,255,0),2)
        break
    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()