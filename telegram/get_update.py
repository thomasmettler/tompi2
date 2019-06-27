#!/usr/bin/python

import pyjokes
import telegram
import time
import datetime
import subprocess
from send_photo import *
from influxdb import InfluxDBClient


bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')
CHAT_ID = -318152844
old_updateid = 0
updateid = 0
FNULL = open(os.devnull, 'w')

TEMP_PATH = '/home/pi/Tom_Stuff/DAQ/somefile.txt'
SNAP_PATH = '/home/pi/Tom_Stuff/camera_data/daily_motion/snapshot/'

def getChatUpdate():
    try:
        update = bot.getUpdates(offset=-1, timeout = 4)
        updateid = update[0].update_id
    except telegram.error.TimedOut:
        print("time out error...")
        time.sleep(1)
    except telegram.error.NetworkError:
        print("NetworkError...")
        time.sleep(1)
        #bot.sendMessage(chat_id=CHAT_ID,text="I am still alaive")
        updateid = old_updateid
        time.sleep(1)
    except IndexError:
        print("no valid input...")
        time.sleep(1)
    return
    
def split_message( str ):
	firstpart = 'hello'
	secondpart = 'world'
	firstpart, secondpart = str[:len(str)/2], str[len(str)/2:]
	try:
		bot.sendMessage(chat_id=CHAT_ID, text=firstpart)
	except telegram.error.BadRequest:
		split_message(firstpart)
	try:
		bot.sendMessage(chat_id=CHAT_ID, text=secondpart)
	except telegram.error.BadRequest:
		split_message(secondpart)
	return;

def help_message():
    try:
        output = """Write \"Pi bash command\"
Fixed commands:
start daq: Start data taking from gas sensors
stop daq: Stop data taking from gas sensors
start camera: Start cameras + motion detection
stop camera daq: Stop cameras + stop motion detection
status camera: Shows status of the motioneye server
check camera: Shows if camera is active
joke: Tells a joke, option: chuck, all
Fortune: Tells random fortune with random emojicon
upload n: upload the n newest videos from the cameras
take n: takes n pictures with delay of one sec
send type number: send newest number of files taken of type
"""
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return

def start_daq():
    rest = '/bin/bash /home/pi/Tom_Stuff/start_daq.sh'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "start daq"
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return  

def stop_daq():
    rest = '/bin/bash /home/pi/Tom_Stuff/stop_daq.sh'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "stop daq"
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")   
    return

def start_camera( verbose ):
    rest = 'sudo systemctl start motioneye'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "start camera"
        if(verbose ==1):
            bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return

def stop_camera(verbose):
    rest = 'sudo systemctl stop motioneye'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "stop camera"
        if(verbose == 1):
            bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return

def status_camera():
    rest = 'sudo systemctl status motioneye'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "status camera"
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    except telegram.error.BadRequest:
        split_message( output )
    return

def fortune():
    rest = 'fortune | ./cowsay.sh'
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return
    
def dropbox_upload( rest ):
    if( len(rest.split()) > 1 ):
        numbers = rest.split(' ', 1)[1]
    else:
        numbers = '1'
    rest = './upload_file.sh /home/pi/Tom_Stuff/camera_data/ ' + numbers
    try:
        bot.sendMessage(chat_id=CHAT_ID, text='start uploading files...')
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    except telegram.error.BadRequest:
        split_message( output )  
    return
    
def temp():
    with open(TEMP_PATH) as f:
		Tmp = f.readline().split()
		te = float(Tmp[0])
		hu = float(Tmp[1])
		output = "Temperature: " + "%.2f" % te + " Deg Celsius, Humidity: " + "%.2f" % hu + "%"
		bot.sendMessage(chat_id=CHAT_ID, text=output)
    return

def send_cam( rest ):
    file_path = '/home/pi/Tom_Stuff/camera_data/daily_motion/'
    typ = ""
    #number = ""
    print len(rest.split())
    if( len(rest.split()) == 2 ):
        typ = rest.split(' ', 1)[1]
        numbers = 1
    elif( len(rest.split()) == 3 ):
        typ = rest.split(' ', 1)[1].split(' ', 1)[0]
        numbers = int(rest.split(' ', 1)[1].split(' ', 1)[1])
    else:
        numbers = 1
        typ = "thumb"
    #print "typ: " + typ
    #print " numbers: ", numbers
    send_files( typ , numbers, file_path)
    return
def check_camera(verbose):
    isrunning = 0
    try:
        todo = 'sudo systemctl status motioneye | grep dead'
        p = subprocess.Popen(todo, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        #output = output + "end of cmd norm output"
        print output
        if not output:
            print 'motioneye is running'
            try:
                todo = 'sudo systemctl status motioneye | grep active'
                p = subprocess.Popen(todo, stdout= subprocess.PIPE,
                stderr=subprocess.PIPE, shell=True)
                (output, err) = p.communicate()
                if(verbose == 1):
                    bot.sendMessage(chat_id=CHAT_ID, text=output)
                isrunning = 1
            except OSError:
                print 'OS error in take picture'
                #bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
            except AttributeError:
                print 'Attribute Error'
                #bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
        else:
            print 'motioneye is not running'
            if( verbose == 1):
                bot.sendMessage(chat_id=CHAT_ID, text=output)
        #print "this was it..."
        #bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        print 'OS error in rake picture'
        #bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        print 'Attribute Error'
        #bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    return isrunning
    
    
def take_picture( rest ):
    numbers = 1
    restart = 0
    camnumber = 0
    if( len(rest.split()) == 3 ):
        numbers = int((rest.split(' ', 1)[1]).split(' ', 1)[0] )
        camnumber = int((rest.split(' ', 1)[1]).split(' ', 1)[1] )
    if( len(rest.split()) == 2 ):
        numbers = int(rest.split(' ', 1)[1])
    if( check_camera(0) == 1):
        stop_camera(0)
        restart = 1
    #print camnumber
    for x in range(0,numbers):
        try:
            #snap_path = '/home/pi/Tom_Stuff/camera_data/daily_motion/snapshot/'
            todo = ('fswebcam --device /dev/video' + str(camnumber)
            + ' --frames 10 -r 640x480 --jpeg 100 -D 0 --banner-colour "#FF000000" --line-colour "#FF000000" '
            + SNAP_PATH + 'Cam01_$(date +%Y_%m_%d_%H-%M-%S).jpg')
            p = subprocess.Popen(todo, stdout= subprocess.PIPE,
            stderr=subprocess.PIPE, shell=True)
            (output, err) = p.communicate()
            #output = output + "end of cmd norm output"
            #bot.sendMessage(chat_id=CHAT_ID, text=output)
        except OSError:
            print 'OS error in rake picture'
            #bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
        except AttributeError:
            print 'Attribute Error'
            #bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
        time.sleep(1)
    if(restart == 1):
        start_camera(0)
    send_snapshot( 'jpg' , numbers, SNAP_PATH)
    return
    
def run_rest( rest ):
    try:
        p = subprocess.Popen(rest, stdout= subprocess.PIPE,
        stderr=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        output = output + "end of cmd norm output"
        bot.sendMessage(chat_id=CHAT_ID, text=output)
    except OSError:
        bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
    except AttributeError:
        bot.sendMessage(chat_id=CHAT_ID,text="No text input command")
    except telegram.error.BadRequest:
        split_message( output )
    return

def iamalive():
    post = "Telegram,no=1 value=" + "1"
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
     "--data-binary", post], stdout=FNULL, stderr=FNULL)
    return

def getTempInflux():
    this_temp = 0
    this_humid = 0
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('mydb')
    temp_results = client.query('SELECT last("value") FROM "Temperature"')
    temp_points = temp_results.get_points()
    for temp_point in temp_points:
	this_temp = temp_point['last']
        #print temp_point['last']
    humi_results = client.query('SELECT last("value") FROM "Humidity"')
    humi_points = humi_results.get_points()
    for humi_point in humi_points:
        this_humid = humi_point['last']
	#print humi_point['last']
    #output = "end of cmd norm output"
    #bot.sendMessage(chat_id=CHAT_ID, text=output)
    output = "Temperature: " + "%.2f" % this_temp + " Deg Celsius, Humidity: " + "%.2f" % this_humid + "%"
    bot.sendMessage(chat_id=CHAT_ID, text=output)
    return

while( True ): 
    
    #getChatUpdate()
    ### get update from chat ########################################
    
    try:
        update = bot.getUpdates(offset=-1, timeout = 4)
        updateid = update[0].update_id
    except telegram.error.TimedOut:
        print("time out error...")
        time.sleep(1)
    except telegram.error.NetworkError:
        print("NetworkError...")
        time.sleep(1)
        #bot.sendMessage(chat_id=CHAT_ID,text="I am still alaive")
        updateid = old_updateid
        time.sleep(1)
    except IndexError:
        print("no valid input...")
        time.sleep(1)
        
    #################################################################
    
    ### check if update is new and if yes take actions######################################
    if(updateid != old_updateid):
        update_nr = len(update)
        message = update[0].message
        try:
            text = message.text
        except OSError:
            text="Invalid input command"
            bot.sendMessage(chat_id=CHAT_ID,text="Invalid input command")
        except AttributeError:
            text="No text input command"
            bot.sendMessage(chat_id=CHAT_ID,text="No text input command")

        print "Anzahl updates: ", update_nr
        print "ID numbber: ", updateid
        print "Message: ", text

        print("Output of command: ")
        firstWord = 'zero'
        #(firstWord, rest) = text.split(maxsplit=1)
        if( len(text.split()) > 1 ): 
            firstWord = text.split(' ', 1)[0]
            rest = text.split(' ', 1)[1]
            print firstWord
            print rest
        if(firstWord == 'Pi'):
            if(rest == 'help'):
                help_message()
            elif(rest == 'start daq'):
                start_daq()
            elif(rest == 'stop daq'):
                stop_daq()
            elif(rest == 'start camera'):
                start_camera(1)
            elif(rest == 'stop camera'):
                stop_camera(1)
            elif(rest == 'status camera'):
                status_camera()
            elif(rest == 'check camera'):
                check_camera(1)
            elif(rest == 'joke'):
                bot.sendMessage(chat_id=CHAT_ID,text=pyjokes.get_joke())
            elif(rest == 'joke chuck'):
                bot.sendMessage(chat_id=CHAT_ID,
                text=pyjokes.get_joke(language='en',category='chuck'))
            elif(rest == 'joke all'):
                bot.sendMessage(chat_id=CHAT_ID,
                text=pyjokes.get_joke(language='en',category='all'))
            elif(rest == 'Fortune'):
                fortune()
            elif(rest.startswith("upload")):
                dropbox_upload(rest)   
            elif(rest == 'temp'):
                #temp()	
		getTempInflux()
            elif(rest.startswith("send")):
                send_cam(rest)
            elif(rest.startswith("take")):
                take_picture(rest)
            else:
                run_rest( rest )
										
        old_updateid = updateid
        #print output
    iamalive()
    time.sleep(4)
    

