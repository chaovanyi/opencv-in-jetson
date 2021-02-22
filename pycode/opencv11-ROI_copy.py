import cv2
print(cv2.__version__)
goFlag = 0

def mouse_click(event,x,y,flags,params):
    global x1,y1,x2,y2
    global goFlag
    if event == cv2.EVENT_LBUTTONDOWN:
        x1 = x
        y1 = y
        goFlag = 0
    if event == cv2.EVENT_LBUTTONUP:
        x2 = x
        y2 = y
        goFlag = 1


#dispW = 320
#dispH = 240 #60fps

dispW = 640
dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps
flip = 2

cv2.namedWindow('WebCam')
cv2.setMouseCallback('WebCam', mouse_click)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    if goFlag == 1:
        frame = cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),3)
        roi = frame[y1:y2,x1:x2]
        cv2.imshow('Copy ROI',roi)
        cv2.moveWindow('Copy ROI',705,0)

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()