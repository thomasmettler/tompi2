import RPi.GPIO as GPIO
import sys              # for take parameters

#GPIO.setup(26, 'output')

# Switch on
#GPIO.output(26, GPIO.HIGH)

# To read the state
pin = int(sys.argv[1])    # assign pin

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setup(pin, GPIO.OUT) # GPIO Assign mode

state = GPIO.input(pin)
if state:
   print('on')
else:
   print('off')
