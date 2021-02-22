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