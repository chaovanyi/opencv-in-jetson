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
#Uncomment These next Two Line for Pi Camera
#camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#cam= cv2.VideoCapture(camSet)

#Or, if you have a WEB cam, uncomment the next line
#(If it does not work, try setting to '1' instead of '0')
cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)
#disW =int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
#disW =int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))
BW = int(0.25*dispW)
BH = int(0.20*dispH)
print('disW:',dispW,'disH:',dispH)

posX = 0
posY = 0
dx = 2
dy = 2

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)
    frame = cv2.rectangle(frame,(posX,posY),(posX+BW,posY+BH),(255,0,0),-1) #-1 to fill the box!

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