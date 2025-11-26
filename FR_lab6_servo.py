#Lab6 Servo Motor

import RPi.GPIO as GPIO	#import GPIO library to use GPIO pins for RPi
import time	#import time library

GPIO.setwarnings(False)	#To disable warnings

servo_pin = 18	#Set pin 18 for servo motor

GPIO.setmode(GPIO.BCM)	#Inform library which pin numbering system in use
GPIO.setup(servo_pin, GPIO.OUT)	#initialize pin 18 as output pin
pwm = GPIO.PWM(servo_pin, 50)	#Set PWM channel at 50 Hz
pwm.start(2)	#Begin PWM at 0% duty cycle

try:
    while True:	#forever loop
        pwm.ChangeDutyCycle(2)	#Rotate handle to 0 degrees
        time.sleep(0.5)	#wait for 1 sex
        
        pwm.ChangeDutyCycle(12)	#Rotate handle to 180 degrees
        time.sleep(0.5)	#wait for 1 sec

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()