import RPi.GPIO as GPIO	#import GPIO library to use GPIO pins for RPi
import time	#import time library to use time delay

GPIO.setwarnings(False)	#To disable warnings

TRIG_pin = 23	#Set pin 23 for TRIG
ECHO_pin = 24	#Set pin 24 for ECHO
led_1 = 22	#Set pin 22 for led 1
led_2 = 25	#Set pin 25 for led 2

GPIO.setmode(GPIO.BCM)	#Inform library which pin numbering system in use
GPIO.setup(TRIG_pin, GPIO.OUT)	#initialize pin 23 as output pin
GPIO.setup(ECHO_pin, GPIO.IN)	#initialize pin 24 as input pin
GPIO.setup(led_1, GPIO.OUT)	#initialize pin 22 as output pin
GPIO.setup(led_2, GPIO.OUT)	#initialize pin 25 as output pin

try:
    while True:	#forever loop
        GPIO.output(TRIG_pin, False)
        print("initializing the sensor")
        
        time.sleep(2)
        
        GPIO.output(TRIG_pin, True)	#set TRIG pulse as high for 1 sec
        time.sleep(1)
        GPIO.output(TRIG_pin, False)
        
        while GPIO.input(ECHO_pin) == 0:	#wait till echo pin is low
            pulse_start = time.time()	#record pulse start time
            
        while GPIO.input(ECHO_pin) == 1:	#wait till echo pin is high
            pulse_end = time.time()	#record pulse end time
            
        pulse_duration = pulse_end - pulse_start	#compute pulse duration
        distance = round(pulse_duration*17150,2)	#round to 2 decimal places
        
        if(distance > 2 and distance < 400):	#check if distance is within 2 to 400cm
            print("Distance:", distance - 0.5, "cm")	#print out the calibrated distance value
            GPIO.output(led_1, True)	#turn on led_1
            GPIO.output(led_2, False) 	#turn off led_2
            
        else:
            print("Out of Range")	#if distance not within 2 to 400cm range
                
            GPIO.output(led_1, False)	#turn off led_1
            GPIO.output(led_2, True)	#turn on led_2
                
except KeybordInterrupt:
    pass

finally:
    GPIO.cleanup()
        
        