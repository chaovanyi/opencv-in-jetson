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

#read img
PL = cv2.imread('pl.jpg')
PL = cv2.resize(PL,(75,75))
cv2.imshow('LogoWindow',PL)
cv2.moveWindow('LogoWindow',705,0)

#cvt to gray
PLGray = cv2.cvtColor(PL,cv2.COLOR_BGR2GRAY)
cv2.imshow('PLGray',PLGray)
cv2.moveWindow('PLGray',800,0)

#creating a mask
_,BGMask = cv2.threshold(PLGray,240,255,cv2.THRESH_BINARY) #if that pixel>245 it's white, if not, black
cv2.imshow('BGMask',BGMask)
cv2.moveWindow('BGMask',900,0)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask',FGMask)
cv2.moveWindow('FGMask',1000,0)

FG = cv2.bitwise_and(PL,PL, mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG',1100,0)

#assign variable for ROI
BW = 75
BH = 75
Xpos = 10
Ypos = 10
dX = 1
dY = 1

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    #get region of interest of video frame
    ROI = frame[Ypos:Ypos+BH,Xpos:Xpos+BW]
    ROIBG = cv2.bitwise_and(ROI,ROI,mask=BGMask)
    cv2.imshow('ROIBG',ROIBG)
    cv2.moveWindow('ROIBG',1200,0)

    #adding FG with ROIBG
    ROInew = cv2.add(FG,ROIBG)
    cv2.imshow('ROInew',ROInew)
    cv2.moveWindow('ROInew',1300,0)

    #put ROI new into our webcam
    frame[Ypos:Ypos+BH,Xpos:Xpos+BW] =  ROInew

    #moving the logo
    Xpos = Xpos + dX
    Ypos = Ypos + dY

    #make it bounce! not going out of range
    if Xpos <= 0 or Xpos+BW >= dispW:
        dX= dX *-1
    if Ypos <= 0 or Ypos+BH >= dispH:
        dY= dY *-1

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()