#Lab 4: Interfacing Push Button

import RPi.GPIO as GPIO	#import GPIO library to use GPIO pins for RPi
import time	#import time library to use time function for delay

GPIO.setwarnings(False)	#To disable warnings

buzzer_pin = 24	#Set pin 24 for buzzer

GPIO.setmode(GPIO.BCM)	#Inform library which pin numbering sytem in use
GPIO.setup(buzzer_pin, GPIO.OUT)	#Initialize pin 24 as output pin

try:
    while True:	#forever loop
        GPIO.output(buzzer_pin, True);	#turn on buzzer
        time.sleep(2)	#wait for 2 seconds    
        GPIO.output(buzzer_pin, False)	#turn off buzzer
        time.sleep(2)	#wait for 2 seconds
                
except keyboardInterrupt:
    pass

finally:
    GPIO.cleanup()