import sys
import RPi.GPIO as GPIO
import Adafruit_DHT

RH, T =  Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 17) 
#  23  in the last line of code referring to GPIO 23 which is pin 16 I believe

# Make sure to comment out the print line that does not apply to the version your testing
# for Python 2
print str(RH), str(T)
# for Python 3
print(str(RH), str(T))
