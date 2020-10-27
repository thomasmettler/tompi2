
from gpiozero import LED
import time
 # Module sys has to be imported:
import sys                

print sys.argv[1], sys.argv[2]
pin = LED(int(sys.argv[1]))

if sys.argv[2] == 'on':
    print 'Turned on'
    pin.on()
else:
    'Turned off'
    pin.off()
    time.sleep(5)
