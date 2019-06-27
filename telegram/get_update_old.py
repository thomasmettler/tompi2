#!/usr/bin/python

import pyjokes
import telegram
import time
import datetime
import subprocess

def split_message( str ):
	firstpart = 'hello'
	secondpart = 'world'
	firstpart, secondpart = str[:len(str)/2], str[len(str)/2:]
	try:
		bot.sendMessage(chat_id=-318152844, text=firstpart)
	except telegram.error.BadRequest:
		split_message(firstpart)
	try:
		bot.sendMessage(chat_id=-318152844, text=secondpart)
	except telegram.error.BadRequest:
		split_message(secondpart)
	return;

bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

#print(bot.get_me())
#time_now = datetime.datetime.now()
#time_message = 'Kamera 1: \nMotion detected at: '+ str(time_now)
#bot.sendMessage(chat_id=-318152844, text=time_message)
old_updateid = 0
updateid = 0
while( 1 ): 
    
    try:
        update = bot.getUpdates(offset=-1, timeout = 4)
        updateid = update[0].update_id
    except telegram.error.TimedOut:
        print("time out error...")
        time.sleep(1)
    except telegram.error.NetworkError:
        print("NetworkError...")
        time.sleep(1)
        #bot.sendMessage(chat_id=-318152844,text="I am still alaive")
        updateid = old_updateid
        time.sleep(1)
    except IndexError:
        print("no valid input...")
        time.sleep(1)
        
    if(updateid != old_updateid):
        update_nr = len(update)
        message = update[0].message
        try:
            text = message.text
        except OSError:
            text="Invalid input command"
            bot.sendMessage(chat_id=-318152844,text="Invalid input command")
        except AttributeError:
            text="No text input command"
            bot.sendMessage(chat_id=-318152844,text="No text input command")
            
        #bashCommand = text
        #args = ['echo','somethiong']
        #subprocess.call(text.split())

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
                try:
                    output = """Write \"Pi bash command\"
Fixed commands:
start daq: Start data taking from gas sensors
stop daq: Stop data taking from gas sensors
start camera: Start cameras + motion detection
stop camera daq: Stop cameras + stop motion detection
status camera: Shows status of the motioneye server
joke: Tells a joke, option: chuck, all
Fortune: Tells random fortune with random emojicon
upload n: upload the n newest videos from the cameras
"""
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")
                    
            elif(rest == 'start daq'):

                rest = './../start_daq.sh'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "start daq"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")

            elif(rest == 'stop daq'):
                rest = '/bin/bash /home/pi/Tom_Stuff/stop_daq.sh'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "stop daq"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")

            elif(rest == 'start camera'):
                rest = 'sudo systemctl start motioneye'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "start camera"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")

            elif(rest == 'stop camera'):
                rest = 'sudo systemctl stop motioneye'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "stop camera"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")

            elif(rest == 'status camera'):
                rest = 'sudo systemctl status motioneye'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "status camera"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")
                except telegram.error.BadRequest:
	                split_message( output )

            elif(rest == 'joke'):
                bot.sendMessage(chat_id=-318152844,text=pyjokes.get_joke())
            elif(rest == 'joke chuck'):
                bot.sendMessage(chat_id=-318152844,
                text=pyjokes.get_joke(language='en',category='chuck'))
            elif(rest == 'joke all'):
                bot.sendMessage(chat_id=-318152844,
                text=pyjokes.get_joke(language='en',category='all'))
            elif(rest == 'Fortune'):
                rest = 'fortune | ./cowsay.sh'
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")
            elif(rest.startswith("upload")):
                if( len(rest.split()) > 1 ):
                    numbers = rest.split(' ', 1)[1]
                else:
                    numbers = '1'
                rest = './upload_file.sh /home/pi/Tom_Stuff/camera_data/ ' + numbers
                try:
                    bot.sendMessage(chat_id=-318152844, text='start uploading files...')
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")
                except telegram.error.BadRequest:
	                split_message( output )  
            elif(rest == 'temp'):
	            with open('/home/pi/Tom_Stuff/somefile.txt') as f:
					Tmp = f.readline().split()
					te = float(Tmp[0])
					hu = float(Tmp[1])
					output = "Temperature: " + "%.2f" % te + " Deg Celsius, Humidity: " + "%.2f" % hu + "%"
					bot.sendMessage(chat_id=-318152844, text=output)
            #if(rest == 'joke twister'):
            #    bot.sendMessage(chat_id=-318152844,
            #   text=pyjokes.get_joke(language='en',category='twister'))
            else:
                try:
                    p = subprocess.Popen(rest, stdout= subprocess.PIPE,
                    stderr=subprocess.PIPE, shell=True)
                    (output, err) = p.communicate()
                    output = output + "end of cmd norm output"
                    bot.sendMessage(chat_id=-318152844, text=output)
                except OSError:
                    bot.sendMessage(chat_id=-318152844,text="Invalid input command")
                except AttributeError:
                    bot.sendMessage(chat_id=-318152844,text="No text input command")
                except telegram.error.BadRequest:
	                split_message( output )
				#except telegram.error.BadRequest:
						#split_message( output )
										
        old_updateid = updateid
        #print output
    time.sleep(4)
