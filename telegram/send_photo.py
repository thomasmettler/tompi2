


import telegram
import time
import datetime
import glob
import os
import requests
import subprocess

REQUEST_URL = 'https://api.telegram.org/bot694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
BOT_API = '694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
USER_ID = -318152844

def send_files( typ , number, path):
    send_para = ""
    send_typ = ""
    if(typ == 'mp4'):
        send_para = "/sendVideo"
        send_typ = 'video'
    else:
        send_para = '/sendPhoto'
        send_typ = 'photo'
    videopath = path + '*/*/*' + 'mp4'
    path = path + '*/*/*' + typ
    #time.sleep(1)
    list_of_videofiles = glob.glob(videopath)
    list_of_files = glob.glob(path)
    list_of_files.sort(key=os.path.getmtime)
    list_of_videofiles.sort(key=os.path.getmtime)
    number = number*-1
    list_files_send = list_of_files[number:]
    list_videofiles_send = list_of_videofiles[number:]
    bot = telegram.Bot(token=BOT_API)

    #print list_files_send
    
    #print(bot.get_me())
    #time_now = datetime.datetime.now()
    #print list_of_videofiles[-1]
    #videolength = getLength(list_of_videofiles[-1])
    #time_message = 'Latest video length: '+ str(videolength)
    #bot.sendMessage(chat_id=-318152844, text=time_message)

    #bot.sendPhoto(-318152844, latest_file)
    user_id = USER_ID
    #REQUEST_URL = 'https://api.telegram.org/bot694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk'
    data = {'chat_id': user_id}
    for index, item in enumerate(list_files_send):
        imagePath = item
        print item
        files = { send_typ: (imagePath, open(imagePath, "rb"))}
        requests.post(REQUEST_URL + send_para, data=data, files=files)
	
	videolength = getLength(list_videofiles_send[index])
	time_message = 'Video length: '+ str(videolength)
        print time_message
	bot.sendMessage(chat_id=-318152844, text=time_message)
    # print and send the duration of the last videofile
    #print list_of_videofiles[-1]
    #videolength = getLength(list_of_videofiles[-1])
    #time_message = 'Latest video length: '+ str(videolength)
    #bot.sendMessage(chat_id=-318152844, text=time_message)
    
def getLength( filename ):
    result = subprocess.Popen(["ffprobe", filename],
      stdout = subprocess.PIPE, stderr = subprocess.STDOUT)
    #print [x for x in result.stdout.readlines() if "Duration" in x]
    return [x for x in result.stdout.readlines() if "Duration" in x]


def send_snapshot( typ , number , path):
    send_para = ""
    send_typ = ""
    if(typ == 'mp4'):
        send_para = "/sendVideo"
        send_typ = 'video'
    else:
        send_para = '/sendPhoto'
        send_typ = 'photo'
    
    path = path + '*' + typ
    list_of_files = glob.glob(path)
    list_of_files.sort(key=os.path.getctime)
    number = number*-1
    list_files_send = list_of_files[number:]
    bot = telegram.Bot(token=BOT_API)


    
    #print(bot.get_me())
    #time_now = datetime.datetime.now()
    #time_message = 'Kamera 1: \nMotion detected at: '+ str(time_now)
    #bot.sendMessage(chat_id=-318152844, text=time_message)

    #bot.sendPhoto(-318152844, latest_file)
    user_id = USER_ID
    
    data = {'chat_id': user_id}
    for item in list_files_send:
        imagePath = item
        print item
        files = { send_typ: (imagePath, open(imagePath, "rb"))}
        requests.post(REQUEST_URL + send_para, data=data, files=files)
    
    '''
    data = {'chat_id': user_id}
    files = {'video': (imagePath, open(imagePath, "rb"))}
    requests.post(REQUEST_URL + '/sendVideo',text=time_message, data=data, files=files)
    '''

#send_files( 'mp4' , 2)

