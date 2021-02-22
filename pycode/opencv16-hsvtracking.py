import cv2
import numpy as np
print(cv2.__version__)

def nothing(x):
    pass

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars',1320,0)

cv2.createTrackbar('hueLower','Trackbars',50,179,nothing)
cv2.createTrackbar('hueUpper','Trackbars',100,179,nothing)
cv2.createTrackbar('hue2Lower','Trackbars',50,179,nothing)
cv2.createTrackbar('hue2Upper','Trackbars',100,179,nothing)
cv2.createTrackbar('satLow','Trackbars',100,255,nothing)
cv2.createTrackbar('satHigh','Trackbars',255,255,nothing)
cv2.createTrackbar('valLow','Trackbars',100,255,nothing)
cv2.createTrackbar('valHigh','Trackbars',255,255,nothing)


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
    #frame = cv2.imread('smarties.png')

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #creating track value from trackbar
    hueLow = cv2.getTrackbarPos('hueLower','Trackbars')
    hueUp = cv2.getTrackbarPos('hueUpper','Trackbars')
    hue2Low = cv2.getTrackbarPos('hue2Lower','Trackbars')
    hue2Up = cv2.getTrackbarPos('hue2Upper','Trackbars')

    Ls = cv2.getTrackbarPos('satLow','Trackbars')
    Us = cv2.getTrackbarPos('satHigh','Trackbars')

    Lv = cv2.getTrackbarPos('valLow','Trackbars')
    Uv = cv2.getTrackbarPos('valHigh','Trackbars')

    #creating an array for the track value
    l_b = np.array([hueLow,Ls,Lv])
    u_b = np.array([hueUp,Us,Uv])
    l_b2 = np.array([hue2Low,Ls,Lv])
    u_b2 = np.array([hue2Up,Us,Uv])

    #creating FG mask
    FGmask = cv2.inRange(hsv,l_b,u_b) #if that pixel in range, it gonna turn white, if not, black
    FGmask2 = cv2.inRange(hsv,l_b2,u_b2)
    FGmaskComp = cv2.add(FGmask,FGmask2)
    cv2.imshow('FGmaskComp',FGmaskComp)
    cv2.moveWindow('FGmaskComp',0,410)

    #creating FG by using FGmask
    FG = cv2.bitwise_and(frame,frame,mask=FGmask)
    cv2.imshow('FG',FG)
    cv2.moveWindow('FG',480,0)

    #creating BGmask that is a reverse of FGmask
    BGmask = cv2.bitwise_not(FGmask)
    cv2.imshow('BGmask',BGmask)
    cv2.moveWindow('BGmask',480,410)

    #creating BG by using BGmask
    BG = cv2.cvtColor(BGmask,cv2.COLOR_GRAY2BGR) #we wont get color from this, just make the matrix into the right size
    
    final = cv2.add(FG,BG)
    cv2.imshow('final',final)
    cv2.moveWindow('final',900,0)


    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()