
import RPi.GPIO as GPIO # controls the GPIO pins
import telepot         # send message if interaction
import time             # not used now
import datetime         # get actual time
import sys              # for take parameters
         
# helper output ###
if sys.argv[1] == 'help':
    print('Usage: python switch_pin.py [16,20,21,26] [on,off]')
    print('Pin 16: 12V power supply')
    print('Pin 20: grey power line')
    print('Pin 21: blue power line')
    print('Pin 26: not used')
    exit()

GPIO.setwarnings(False)
  
print(sys.argv[1], sys.argv[2]) # print given parameters 
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = int(sys.argv[1])    # assign pin
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

if sys.argv[2] == 'on':
    print('Turn on')
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH) # turn on
else:
    print('Turn off')
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # trun off
    
bot = telepot.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')
time_now = datetime.datetime.now()
date_time = time_now.strftime("%H:%M:%S, %d/%m/%Y")
message = 'Turned switch *' + sys.argv[2] + '* at pin ' + sys.argv[1]+'\n'
message += 'At: ' + date_time
bot.sendMessage(chat_id=-318152844, text=message , parse_mode='markdown') # my chat
