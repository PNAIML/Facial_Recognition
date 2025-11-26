import picamera
import time

camera = picamera.PiCamera()

for x in range(1,101):
    camera.capture('/home/pi/test/dataset/BPTEO.8.%s.jpg' % x)
    time.sleep(0.5)
    
print('Done')
