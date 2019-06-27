import time
import datetime
import subprocess
import Adafruit_DHT
import os

FNULL = open(os.devnull, 'w')

temp_old = -100
temperature = 20

humid_old = -100
humidity = 60

while (temp_old ==-100 or humid_old == -100):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    if(temperature != None):
        temp_old=temperature
    if(humidity != None):
        humid_old = humidity


while(1):
    humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.AM2302, 17)
    text = 'Temp= ' , temperature ,  ' Humidity: ' , humidity
    #text = 'Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity)
    print text
    text = str(temperature)+ " " +str(humidity)
    if( temperature != None):
        if( abs(temp_old - temperature)<2 ) :
            post = "Temperature,host=1 value=" + str(temperature) 
            subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
             "--data-binary", post], stdout=FNULL, stderr=FNULL)
            temp_old = temperature

    if( humidity != None):
        if( abs(humid_old - humidity)<5) :
            post = "Humidity,host=1 value=" + str(humidity)
            subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
             "--data-binary", post], stdout=FNULL, stderr=FNULL)
            humid_old = humidity
    if(temperature != None and humidity != None):
        with open('somefile.txt', 'w') as the_file:
                the_file.write(text)
        time.sleep(2)

