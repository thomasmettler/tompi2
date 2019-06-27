import telegram
import time
import datetime
from send_photo import send_files

time.sleep(2)
file_path = '/home/pi/Tom_Stuff/camera_data/daily_motion/'
#send_files( 'jpg' , 1, file_path)
send_files( 'thumb' , 1, file_path)
#bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

#print(bot.get_me())
#time_now = datetime.datetime.now()
#time_message = 'Stored file at: '+ str(time_now)
#bot.sendMessage(chat_id=-318152844, text=time_message)
