import cv2
import numpy as np
import os


path = '/home/pi/test/dataset'

#Pls mask off according to the old/new raspbian
#recognizer = cv2.face.createLBPHFaceRecognizer() #Use in Old Raspbian
recognizer = cv2.face.LBPHFaceRecognizer_create() #Use in New Raspbian
recognizer.read('/home/pi/test/recognizer.xml')

face_dectector = cv2.CascadeClassifier("/home/pi/test/haarcascade_frontalface_default.xml");
font =cv2.FONT_HERSHEY_SIMPLEX

#Names related to ids in dataset folder
names={}
for f in os.listdir(path):
    name=f.split('.')[0]     #name
    id=int(f.split('.')[1])  #id
    names[id]=name

img = cv2.imread('/home/pi/test/test.jpg',0)
faces = face_detector.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(10,10))

for(x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
    predicted_Id, confidence = recognizer.predict(img[y:y+h,x:x+w])

    #Check if confidence is less than 100 ==> "0" is perfect match  
    if (confidence < 100):
        chosen = names[predicted_Id]
        confidence = "{0}%".format(round(100 - confidence))
        
    else:   #confidence level exceeds 100%
        id = "unknown"
        confidence = "{0}%".format(round(100 - confidence))
            
    cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
    cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)
        
cv2.imshow('camera',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
