import face_recognition
import cv2
import os
import numpy as np
import pickle
print(cv2.__version__)

#creating lists
Encodings = []
Names = []
j=0

image_dir = '/home/jetbot/pycode/demoImages/known'
#walk through everything in that dir
for root, dirs, files in os.walk(image_dir): 
    #print(files)
    for file in files:
        path = os.path.join(root,file) #give all the full path with the file name
        #print(path)
        name = os.path.splitext(file)[0] #print the only the name of the file without .jpg
        #print(name)
        person = face_recognition.load_image_file(path)
        encoding = face_recognition.face_encodings(person)[0]

        #put data to the array
        Encodings.append(encoding)
        Names.append(name)
#print(Names)

#write
with open('train.pkl','wb') as f: #write bytes
    pickle.dump(Names,f)
    pickle.dump(Encodings,f)

#erase data
Encodings = []
Names = []

#read
with open('train.pkl','rb') as f:
    Names = pickle.load(f)
    Encodings = pickle.load(f)

font = cv2.FONT_HERSHEY_SIMPLEX

image_dir = '/home/jetbot/pycode/demoImages/unknown'
for root, dirs, files in os.walk(image_dir):
    for file in files:
        path = os.path.join(root,file)
        testImage = face_recognition.load_image_file(path)

        facePositions = face_recognition.face_locations(testImage)
        allEncodings = face_recognition.face_encodings(testImage,facePositions)
        testImage = cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

        for (top,right,bottom,left),face_encoding in zip(facePositions,allEncodings):
            name = 'Unknow Person'
            matches = face_recognition.compare_faces(Encodings,face_encoding) #compare known faces (Encodings) and unknow faces (face_encoding)
            if True in matches:
                first_match_index = matches.index(True) #find the first true index.
                name = Names[first_match_index] #take 1 name from Names array by using index from first_match_index
            cv2.rectangle(testImage,(left,top),(right,bottom),(0,0,255),2)
            cv2.putText(testImage,name,(left,top-6),font,.75,(0,255,0),2)


        cv2.imshow('faceRec',testImage)
        cv2.moveWindow('faceRec',0,0)
        if cv2.waitKey(0)==ord('q'):
            cv2.destroyAllWindows()


