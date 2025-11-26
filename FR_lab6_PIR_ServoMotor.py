#Lab6 PIR and Servo Motor

import RPi.GPIO as GPIO	#import GPIO library to use GPIO pins for RPi
import time	#import time library

GPIO.setwarnings(False)	#To disable warnings

servo_pin = 18	#Set pin 18 for servo motor
pir_pin = 24	#Set pin 24 for servo motor

GPIO.setmode(GPIO.BCM)	#Inform library which pin numbering system in use
GPIO.setup(servo_pin, GPIO.OUT)	#initialize pin 18 as output pin
GPIO.etup(pir_pin, GPIO.IN)	#initize pin 24 as input pin

pwm = GPIO.PWM(servo_pin, 50)	#Set PWM channel at 50 Hz
pwm.start(2)	#Begin PWM at 0% duty cycle

try:
    while True:	#forever loop
        input_state = GPIO.input(pir_pin)	#Read pir sensor state
        
        if input_state == True:	#check if state = 1
            pwm.ChangeDutyCycle(2)	#Rotate handle to 0 degrees
            
            time.sleep(2)	#wait for 2 sec
        
        else:
            pwm.ChangeDutyCycle(12)	#Rotate handle to 0 degrees
            
            time.sleep(2)	#wait for 2 sec
            
except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()