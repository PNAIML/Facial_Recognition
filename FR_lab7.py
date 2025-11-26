import cv2

img = cv2.imread("faces.jpg",1)
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces=face_cascade.detectMultiScale(img, scaleFactor=1.06, minNeighbors=5)
#Haar Cascade Face Detection
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
    
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows