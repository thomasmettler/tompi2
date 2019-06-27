


import telegram
import time
import datetime

bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

#print(bot.get_me())
time_now = datetime.datetime.now()
time_message = 'Kamera 1: \nMotion detected at: '+ str(time_now)
#bot.sendMessage(chat_id=-318152844, text=time_message)

bot.sendPhoto(-318152844, 'file://///tmettler@lhepla18.unibe.ch/home/tmettler/cernbox/Diverses/Raspberry/telegram/Selection_206.png')
#bot.sendPhoto(-318152844, 'http://microboone.fnal.gov/wp-content/uploads/2016/02/miniboone_excess-768x518.png')

#bot.sendPhoto(-318152844, 'https://drive.google.com/open?id=1hWb5ABgh0kEPbOGznkx-fX1wygujh6Cp')
#bot.sendPhoto(-318152844, 'https://cernbox.cern.ch/index.php/apps/gallery/preview/Diverses/Raspberry/telegram/Selection_206.png?width=2000&height=2000&c=514716230246989824%3Ae9d10b2f&requesttoken=AV9vfzMrRA8ucnUhJw0PIzQaWylsGng3BkgAHSUbXwQ%3D%3As%2F57Ig%2FFwY1lacxsvMlx%2FkMBE%2F1JsH8NH4c4LTszOzc%3D&x-access-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoidG1ldHRsZXIiLCJncm91cHMiOltdfQ.xesbu7Y9EOa56IaEGPQc4ToYQIje-pWa1ubRLSsvRQY')
#bot.sendPhoto(-318152844, 'https://cernbox.cern.ch/index.php/apps/gallery/preview/Diverses/Raspberry/telegram/Selection_204.png?width=2000&height=2000&c=514749724549447680%3A5edced48&requesttoken=PwlpehQcOTs6Hz4rLyofMyowbhwVQGIfCgJBbx4HUjk%3D%3AMy32nPRrc4zfiDhchgYMV1WjIep8HT5sNqSMhtqrcqA%3D&x-access-token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhY2NvdW50X2lkIjoidG1ldHRsZXIiLCJncm91cHMiOltdfQ.xesbu7Y9EOa56IaEGPQc4ToYQIje-pWa1ubRLSsvRQY')



