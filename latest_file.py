import glob
import os
import telegram
import time
import datetime

bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

list_of_files = glob.glob('/home/pi/Tom_Stuff/camera_data/daily_motion/*/*/*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
text_message = "The detected motion is stored: \n" + latest_file


bot.sendMessage(chat_id=-318152844, text=text_message)
