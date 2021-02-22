import cv2
print(cv2.__version__)

def nothing():
    pass
cv2.namedWindow('Blended')
cv2.createTrackbar('Blendvalue','Blended',50,100,nothing)

dispW = 320
dispH = 240 #60fps

#dispW = 640
#dispH = 480 #60fps

#dispW = 960
#dispH = 540 #60fps

#dispW = 1280
#dispH = 720 #30fps
flip = 2

cvLogo = cv2.imread('pl.jpg')
cvLogo = cv2.resize(cvLogo,(320,240))
cvLogoGray = cv2.cvtColor(cvLogo,cv2.COLOR_BGR2GRAY) #when doing thresholding we cannot do it on color image
cv2.imshow('cv Logo Gray',cvLogoGray)
cv2.moveWindow('cv Logo Gray',0,300)

_,BGMask = cv2.threshold(cvLogoGray,225,255,cv2.THRESH_BINARY)
cv2.imshow('BG Mask',BGMask)
cv2.moveWindow('BG Mask',385,0)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask',FGMask)
cv2.moveWindow('FG Mask', 385, 300)
FG = cv2.bitwise_and(cvLogo,cvLogo, mask=FGMask)
cv2.imshow('FG',FG)
cv2.moveWindow('FG', 703, 300)

cam=cv2.VideoCapture(2)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,dispW)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,dispH)

while True:
    ret, frame = cam.read()
    frame = cv2.flip(frame,flip)

    BG = cv2.bitwise_and(frame,frame, mask=BGMask)
    cv2.imshow('BG',BG)
    cv2.moveWindow('BG',703,0)

    compImage = cv2.add(BG,FG)
    cv2.imshow('compImage',compImage)
    cv2.moveWindow('compImage',1017,0)

    BW = cv2.getTrackbarPos('Blendvalue','Blended')/100
    BW2 = 1-BW
    print(BW,BW2)

    Blended = cv2.addWeighted(frame,BW,cvLogo,BW2,0)
    cv2.imshow('Blended',Blended)
    cv2.moveWindow('Blended',1017,300)

    FG2 = cv2.bitwise_and(Blended,Blended, mask=FGMask)
    cv2.imshow('FG2',FG2)
    cv2.moveWindow('FG2',1324,0)

    compFinal = cv2.add(BG,FG2)
    cv2.imshow('compFinal',compFinal)
    cv2.moveWindow('compFinal',1324,300)

    cv2.imshow('WebCam',frame)
    cv2.moveWindow('WebCam',0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()