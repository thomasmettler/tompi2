################################################################################
# DHT22 on viperized Photon (V2)
#
# Created: 2015-12-04
#
# This software provides data readout from a DHT22 temperature+humidity sensor on any digital pin of an MCU running VIPER python.
# This code was developed and tested on a viperized Photon board (Particle Photon).
# It follows closely the Arduino code by Adafruit (https://github.com/adafruit/DHT-sensor-library).
#
# Copyright (c) 2015 A.C. Betz.  All right reserved. Developed using the VIPER IDE. 
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
#
#############################################################################################################################


############
#########
# DO THESE THINGS IN THE MAIN PROGRAM
#########
############
# import the streams module for USB serial port.
import stream as streams

# open the default serial port
streams.serial()

#import ICU library
import icu

import timers

############
#########
# end of things to do in main program
#########
############


#########
# functions
#########

def getDHT22data(_receivepin,_receivepinShort): #expects input like (D3.ICU,D3) [TODO: do some nifty string manipulation to get "D3" from D3.ICU]
    
    ### don't execute this more than once every 2s!
    
    timer1 = timers.timer()
    timer1.start()
    foo = 0
    
    DHT22_temp = 0
    DHT22_hum = 0
    BinListDHT22 = []
    timeListDHT22 = []
    
    #Go into high impedence state to let pull-up raise data line level andstart the reading process.
    pinMode(_receivepinShort,OUTPUT)
    digitalWrite(_receivepinShort, HIGH)
    timer1.reset()
    while timer1.get()<10:
        foo+=1
    #First set data line low for 10 milliseconds.
    digitalWrite(_receivepinShort, LOW)
    timer1.reset()
    while timer1.get()<10:
        foo+=1 # maybe change this while to one_shot?
    tmpICU = icu.capture(_receivepin,LOW,86,10000,time_unit=MICROS)#call to ICU seems to take some time, thus call *before* initiation is finished
    # End the start signal by setting data line high for [40 microseconds].
    digitalWrite(_receivepinShort, HIGH)
    pinMode(_receivepinShort,INPUT_PULLUP)
    
    # remove all even entries, they're just "start bits", discard 1st two entries
    for i in range(3,len(tmpICU),1):
        if i%2!=0: #these are the odd entries
            timeListDHT22.append(tmpICU[i])
    # convert to list of binaries
    for i in range(len(timeListDHT22)):
        if timeListDHT22[i] < 35:    # shouldn't be longer than 28us, but allow some wiggle room here
            BinListDHT22.append(0)
        else:
            BinListDHT22.append(1)    
    # extract hum, temp parts (16bits each)
    tmp_hum = BinListDHT22[0:16]    #1st 16 bits are humidity, 2nd 16 bits are temperature
    tmp_temp = BinListDHT22[16:32]
    tmp_tempSign = 1
    if tmp_temp[0] == 1:
        tmp_tempSign = -1 # neg temperatures are encoded most significant bit = 1
        tmp_temp[0] = 0
    tmp_temp = tmp_temp[::-1] #invert the list for conversion to decimal
    tmp_hum = tmp_hum[::-1]
    
    for i in range(16):
        DHT22_temp += tmp_temp[i]*(2**i)
        DHT22_hum += tmp_hum[i]*(2**i)
    DHT22_temp = DHT22_temp/10
    DHT22_hum = DHT22_hum/10
    
    digitalWrite(_receivepinShort, HIGH)
    
    timer1.clear()
    
    return (DHT22_hum, DHT22_temp)



############################################################################################
############################################################################################
#test the code

sleep(1000)
print("starting")
sleep(500)


global DHT22_temp
global DHT22_hum

timer2 = timers.timer()
timer2.start()

while True:
    if timer2.get()>2500:
        DHT22_hum, DHT22_temp = getDHT22data(D3.ICU,D3)
        print(DHT22_temp,DHT22_hum)
        timer2.reset()
