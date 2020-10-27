
import RPi.GPIO as GPIO
import time
 # Module sys has to be imported:
import sys           

if sys.argv[1] == 'help':
    print 'Usage: python switch_pin.py [16,20,21,26] [on,off]'
    print 'Pin 16: 12V power supply'
    print 'Pin 20: grey power line'
    print 'Pin 21: blue power line'
    print 'Pin 26: not used'
    exit()
    
GPIO.setwarnings(False)

print sys.argv[1], sys.argv[2]
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = int(sys.argv[1])
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

if sys.argv[2] == 'on':
    print 'Turn on'
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # out
else:
    print 'Turn off'
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out

