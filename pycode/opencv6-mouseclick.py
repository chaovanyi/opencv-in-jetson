import cv2
import numpy as np
print(cv2.__version__)
evt = -1
evt1= -1
coord = []
#coord1 = []
img = np.zeros((250,250,3),np.uint8)
def click(event,x,y,flags,params):
    global pnt
    global evt
    if event == cv2.EVENT_LBUTTONDOWN: #left click
        print('Mouse Event was:',event)
        print(x,',',y)
        pnt = (x,y)
        coord.append(pnt)
        print(coord)
        evt = event
    if event == cv2.EVENT_RBUTTONDOWN: #right click
        global pnt1
        global tp
        global evt1
    

        pnt1 = (x,y)
        #coord1.append(pnt1)
        evt1 = event
        print(evt1)
        #print(x,y)
        blue = frame[y,x,0]
        green = frame[y,x,1]
        red = frame[y,x,2] #(b,g,r) = (0,1,2)
        #print(blue,green,red)
        colorString=str(blue)+','+str(green)+','+str(red)
        img[:]=[blue,green,red]
        fnt=cv2.FONT_HERSHEY_PLAIN
        r = 255-int(red)
        g = 255-int(green)
        b = 255-int(blue)
        tp = (b,g,r)
        cv2.putText(img,colorString,(10,25),fnt,1,tp,2)
        cv2.imshow('myColor',img)

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

cv2.namedWindow('WebCam')
cv2.setMouseCallback('WebCam',click)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)
    if evt1 == 2:
        cv2.circle(frame,pnt1,5,tp,-1)
        font = cv2.FONT_HERSHEY_PLAIN
        myStr1 = str(pnt1)
        cv2.putText(frame,myStr1,pnt1,font,1,tp,2)
    for pnts in coord:
        cv2.circle(frame,pnts,5,(0,255,0),-1)
        font = cv2.FONT_HERSHEY_PLAIN
        myStr = str(pnts)
        cv2.putText(frame,myStr,pnts,font,1.5,(255,0,0),2)
    #for pnt1s in coord1:
        #cv2.circle(frame,pnt1s,5,tp,-1)
        #font = cv2.FONT_HERSHEY_PLAIN
        #myStr1 = str(pnt1s)
        #cv2.putText(frame,myStr1,pnt1s,font,1.5,tp,2)
    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)

    keyEvent = cv2.waitKey(1)
    if keyEvent==ord('q'):
        break
    if keyEvent==ord('c'):
        coord=[]
cam.release()
cv2.destroyAllWindows()