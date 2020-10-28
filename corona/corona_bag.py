import requests
import pandas as pd

# imports for telegram messaging
import telegram
import time
import datetime
import os


import sys
reload(sys)
sys.setdefaultencoding('utf-8')



url_addr = 'https://www.bag.admin.ch/bag/de/home/krankheiten/ausbrueche-epidemien-pandemien/aktuelle-ausbrueche-epidemien/novel-cov/situation-schweiz-und-international.html'

bot = telegram.Bot(token='694091311:AAF7PmMqhyB88LG1wMmYdIKmis7OqTGlYWk')

skip_initial = 0
time_message_global = 'dfkasjkdfs'

while True:
    html = requests.get(url_addr).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    time_message = 'Please hold phone horizontally:\n'
    time_message += '---------------------------------------------------------------------\n'
    precent = 0.0
    
    for i in range(len(df_list)):
        #print i
        
        df_ = df_list[i]
        #print type(df_)
        #print df_.dtypes
        #print df_.loc[0]
        #print ''
        #export_png(data_table, filename = path)
        #print df_.astype(str)
        df_ = df_.astype(str)
        #print df_.dtypes
        #print df_.axes
        #print df_.columns
        #print df_.shape
        if i == 0:
            pos =  df_.iat[0,1]
            tot =  df_.iat[3,1]
            pos = pos.replace(' ','')
            tot = tot.replace(' ','')
            precent =  int(pos)*1.0/int(tot)
        #print ''
        #df_ = df_.drop(df_.columns[[0]], axis = 1)
        #df_ = df_.applymap(str)
        #time_message += df_.to_string(index=False, justify='left')
        time_message += df_.to_string(index=False, col_space=10)+' \n'
        time_message += '---------------------------------------------------------------------\n'
        #time_message += df_.to_html(index=False)+' \n'

    #time_message += '</pre>'
    
    time_message =  time_message.replace('Total seit Beginn der Epidemie',' Total:')
    time_message =  time_message.replace('Uhr','Uhr:')
    time_message =  time_message.replace('Neu','Neu:')
    time_message =  time_message.replace('Hospitalisierungen','Hospitalisierungen:')
    time_message =  time_message.replace('Labor','')
    time_message =  time_message.replace('Total aktuell','Total')
    time_message =  time_message.replace('tigte Infektionen','tigte Infektionen:')
    time_message =  time_message.replace('lle ','lle: ')
    time_message =  time_message.replace('Covid-19-Test','Covid19 Test:')
    time_message =  time_message.replace('Contact Tracing','Contact Tracing:')
    time_message =  time_message.replace('Isolation','Isolation:')
    time_message =  time_message.replace('ne  ','ne:')
    time_message =  time_message.replace(' Personen in ','')
    time_message =  time_message.replace('tzliche','tzlich in ')
    time_message =  time_message.replace(' nach Einrei...',' (Einreise):')
    time_message =  time_message.replace('*','')
    time_message =  time_message.replace('Please hold phone horizontally:','*Please hold phone horizontally:*')
    #time_message =  time_message.replace('tzliche','tzlich in ')
    #time_message =  time_message.replace('tzliche','tzlich in ')
    
    time_message =  time_message.replace('    ',' ')
    #time_message =  time_message.replace('\d \d','')
    #time_message =  time_message.replace('Covid19Test','Covid-19-Test')
    #print '-----------------------------'
    time_message += 'Anteil positiver Tests: {:4.2f}%'.format(precent*100)+'\n'
    print(time_message)
    
    if time_message != time_message_global:
        time_message_global = time_message
        if skip_initial != 1:
            #bot.sendMessage(chat_id=-476694352, text=time_message, parse_mode='markdown') # BAG chat
            bot.sendMessage(chat_id=-318152844, text=time_message,parse_mode='markdown') # my chat
            print('Send notification')
        skip_initial = 0

    time_now = datetime.datetime.now()
    time.sleep(15*60)
    print('Checked for update at: ' + str(time_now), ' skip notifiaction: ', skip_initial)
    
    
    
    
