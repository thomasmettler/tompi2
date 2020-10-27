
import RPi.GPIO as GPIO
import time
 # Module sys has to be imported:
import sys           

if len(sys.argv) > 1:
    print 'Turns on all Pins in use'
    print 'Pins in use: 16,20,21,26'
    print 'No input needed'
    exit()
    
GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers


GPIO.setup(16, GPIO.OUT) # GPIO Assign mode
GPIO.output(16, GPIO.LOW) # out

GPIO.setup(20, GPIO.OUT) # GPIO Assign mode
GPIO.output(20, GPIO.LOW) # out

GPIO.setup(21, GPIO.OUT) # GPIO Assign mode
GPIO.output(21, GPIO.LOW) # out

GPIO.setup(26, GPIO.OUT) # GPIO Assign mode
GPIO.output(26, GPIO.LOW) # out


