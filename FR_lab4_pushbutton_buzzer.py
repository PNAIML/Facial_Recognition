#Lab 4: Interfacing Buzzer_Push Button
import RPi.GPIO as GPIO	#import GPIO library to use GPIO pins for RPi

GPIO.setwarnings(False)	#To disable warnings

buzzer_pin = 24	#Set pin 24 for buzzer
button_pin = 25	#Set pin 25 for push button

GPIO.setmode(GPIO.BCM)	#Inform library which pin numbering sytem in use
GPIO.setup(buzzer_pin, GPIO.OUT)	#Initialize pin 24 as output pin
GPIO.setup(button_pin, GPIO.IN)	#Intialize pin 25 as input pin

try:
    while True:	#forever loop
        button_status = GPIO.input(button_pin)	#set button status to a variable
        if(button_status == 1):	#check button status if pressed
            GPIO.output(buzzer_pin, True)	#turn on buzzer
            
        else:
            GPIO.output(buzzer_pin, False)	#turn off buzzer
                
except keyboardInterrupt:
    pass

finally:
    GPIO.cleanup()