
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False) 
 
RELAIS_1_GPIO = 16

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
print 'Turn on the light power plug'
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
GPIO.cleanup()
