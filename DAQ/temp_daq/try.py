#!/usr/bin/python
# -*- coding: iso-8859-15 -*-

# Google Spreadsheet DHT Sensor Data-logging Example

import sys
import time
import datetime

import glob
import os
import subprocess

import board
import adafruit_dht
import busio
i2c = busio.I2C(board.SCL, board.SDA)
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1015(i2c)

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

ads.gain = 1
chan = AnalogIn(ads, ADS.P2) #, ADS.P1)
print (format(chan.voltage, '05.2f').replace(".",",")) #chan.voltage)

# Type of sensor, can be `adafruit_dht.DHT11` or `adafruit_dht.DHT22`.
# For the AM2302, use the `adafruit_dht.DHT22` class.
DHT_TYPE = adafruit_dht.DHT22

# Example of sensor connected to Raspberry Pi Pin 17
DHT_PIN  = board.D17

# Initialize the dht device, with data pin connected to:
dhtDevice = DHT_TYPE(DHT_PIN)

## Wachttijd om internet verbinding te laten opstarten.
print ('20 seconden geduld om wifi-verbinding op te starten.')
time.sleep (20)

while True:
        # Probeer sensors uit te lezen.
        temp = dhtDevice.temperature
        humidity = dhtDevice.humidity

        # Skip to the next reading if a valid measurement couldn't be taken.
        # This might happen if the CPU is under a lot of load and the sensor
        # can't be reliably read (timing is critical to read the sensor).
        if humidity is None or temp is None:
                time.sleep(2)
                continue

        volt = format(chan.voltage, '05.2f').replace(".",",") #0.0157463*chan.voltage
        tijd = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        Buitemp = format(read_temp(), '04.1f').replace(".",",")
        Bintemp = format(temp, '0.1f').replace(".",",")
        Vocht = format(humidity, '0.1f').replace(".",",")

        print ('Temperatuur: {0:0.1f} ?C'.format(temp))
        print ('Vochtigheid: {0:0.1f} %'.format(humidity))
        print ('Buitentemp : ' + Buitemp + '?C')
        print ('Voltage    : ' + volt + ' V'), volt
        print ('Tijd: ' + tijd)

        sys.exit(1)
