
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
 
RELAIS_1_GPIO = 4
wait_time = 3

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode
print 'Turn off and wait ', wait_time,' seconds'
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # out
time.sleep(wait_time)
print 'Turn on and wait ', wait_time,' seconds'
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on
time.sleep(wait_time)
print 'Turn off and wait ', wait_time,' seconds'
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # out
time.sleep(wait_time)
print 'Turn on and wait ', wait_time,' seconds'
GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # on
time.sleep(wait_time)
print 'Turn off and finish'
GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # out
