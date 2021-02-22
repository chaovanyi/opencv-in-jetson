import face_recognition
import cv2
import os
import pickle
print(cv2.__version__)

Encodings = []
Names = []

with open('train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

font = cv2.FONT_HERSHEY_SIMPLEX
cam = cv2.VideoCapture(2)

while True:
    _,frame = cam.read()
    frameRGB = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    facePositions = face_recognition.face_locations(frameRGB,model = 'cnn')
    allEncodings = face_recognition.face_encodings(frameRGB,facePositions)
    for (top,right,buttom,left), face_encoding in zip(facePositions,allEncodings):
        name = 'Unknown Person'
        matches = face_recognition.compare_faces(Encodings,face_encoding) #match return in array of false and true
        if True in matches:
            first_match_index = matches.index(True)
            name = Names[first_match_index]
        cv2.rectangle(frame,(left,top),(buttom,right),(0,0,255),2)
        cv2.putText(frame,name,(left,top-6),font,0.75,(255,0,0),2)
    
    cv2.imshow('faceRed',frame)
    cv2.moveWindow('faceRed',0,0)
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindow()


