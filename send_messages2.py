import telegram
import time
import datetime

bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

#print(bot.get_me())
time_now = datetime.datetime.now()
time_message = 'Kamera 2: \nMotion detected at: '+ str(time_now)
bot.sendMessage(chat_id=-318152844, text=time_message)

