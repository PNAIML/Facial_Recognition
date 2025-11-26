import cv2
import numpy as np
import os


path = '/home/pi/test/dataset'
recognizer = cv2.face.createLBPHFaceRecognizer()
face_detector = cv2.CascadeClassifier("/home/pi/test/haarcascade_frontalface_default.xml");
roiList=[]
idList=[]

for f in os.listdir(path):
    img = cv2.imread(path+'/'+f,0)
    id=int(f.split('.')[1])
    faces = face_detector.detectMultiScale(img, scaleFactor=1.06, minNeighbors=5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0),2)
        roiList.append(img[y:y+h, x:x+w])
        idList.append(id)
        
#    cv2.imshow("Image",img)
#    ch = cv2.waitKey(0)
#    if chr(ch & 0xff) == 'q':
#        break
    
recognizer.train(roiList, np.array(idList))
recognizer.save('/home/pi/test/recognizer.xml')


print("[INFO] {} faces trained. Exiting Program".format(len(np.unique(idList))))
cv2.destroyAllWindows()
