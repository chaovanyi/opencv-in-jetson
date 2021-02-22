import face_recognition
import cv2
print(cv2.__version__)

#read known image
donFace = face_recognition.load_image_file('/home/jetbot/pycode/demoImages/known/Donald Trump.jpg')

#encode the face (learn it)
donEncode = face_recognition.face_encodings(donFace)[0] #take the first one of return array

#learn another face
nancyFace = face_recognition.load_image_file('/home/jetbot/pycode/demoImages/known/Nancy Pelosi.jpg')
nancyEncode = face_recognition.face_encodings(nancyFace)[0] #take the first one of return array

penceFace = face_recognition.load_image_file('/home/jetbot/pycode/demoImages/known/Mike Pence.jpg')
penceEncode = face_recognition.face_encodings(penceFace)[0]

#creating an array for our encodings
Encodings = [donEncode, nancyEncode, penceEncode]
Names = ['The Donald','Nancy pelosi','Mike Pence']

font = cv2.FONT_HERSHEY_DUPLEX
testImage = face_recognition.load_image_file('/home/jetbot/pycode/demoImages/unknown/u11.jpg')
facePositions = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage, facePositions)

testImage = cv2.cvtColor(testImage,cv2.COLOR_RGB2BGR)

for (top,right,bottom,left), face_encoding in zip(facePositions,allEncodings): #we go throught 2 set of variable, use zip
    name = 'Unknown Person'
    matches = face_recognition.compare_faces(Encodings,face_encoding) #compare all training data with particular face that we're at this time of the loop
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage,(left,top),(right,bottom),(0,0,255),2)
    cv2.putText(testImage,name,(left,top-6),font,0.75,(255,0,0),1)


cv2.imshow('WebCam',testImage)
cv2.moveWindow('WebCam',0,0)
if cv2.waitKey(0)==ord('q'):
    cv2.destroyAllWindows()