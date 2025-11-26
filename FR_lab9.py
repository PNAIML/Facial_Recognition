import cv2

cap= cv2.VideoCapture(0)
face_cascade= cv2.CascadeClassifier("/home/pi/test/haarcascade_frontalface_default.xml")
eye_cascade= cv2.CascadeClassifier("/home/pi/test/haarcascade_eye.xml")

while True:
    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame)
    
    for(x, y, w, h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        roi= frame[y:y+h, x:x+w]
        eyes= eye_cascade.detectMultiScale(roi)
        
        for(ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    
    cv2.imshow("Frame",frame)
    ch = cv2.waitKey(1)
    if chr(ch&0xff)=='q': break
    
cv2.destroyAllWindows()
cap.release()
    
    
