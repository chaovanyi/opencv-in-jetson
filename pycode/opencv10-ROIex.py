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

BW = int(0.20*dispW)
BH = int(0.20*dispH)

posX = 0
posY = 0
dx = 2
dy = 2

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    roi = frame[posY:posY+BH,posX:posX+BW].copy()
    frame1 = cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY) #change roi to frame if we want a color box
    frame1 = cv2.cvtColor(frame1,cv2.COLOR_GRAY2BGR) #change frame1 to frame if we want color box
    frame[posY:posY+BH,posX:posX+BW] = frame1 #change to roi if we want the color box

    cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),2) #-1 to fill the box!

    posX=posX +  dx
    posY= posY + dy
    if posX <=0 or posX+BW>=dispW:
        dx= dx *-1
    if posY <= 0 or posY+BH >= dispH:
        dy= dy *-1
    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()