import io
import subprocess
import time
import psutil
import RPi.GPIO as GPIO
import os

FNULL = open(os.devnull, 'w')

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

GPIO.setup(16, GPIO.OUT) # GPIO Assign mode
GPIO.setup(20, GPIO.OUT) # GPIO Assign mode
GPIO.setup(21, GPIO.OUT) # GPIO Assign mode
GPIO.setup(26, GPIO.OUT) # GPIO Assign mode

temp = 0
cpu = 0
while(1):
    cpu = psutil.cpu_percent()
    print cpu
    f = open("/sys/class/thermal/thermal_zone0/temp", "r")
    t = f.readline ()
    temp = float(t) / 1000
    #cputemp = "CPU temp: "+t
    #print (cputemp)
    print (temp)
    #subprocess.call("/opt/vc/bin/vcgencmd","measure_temp")
    post = "raspi_cpu,host=1 value=" + str(cpu) 
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    post = "raspi_temp,host=1 value=" + str(temp)
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    
    state_16 = GPIO.input(16)
    state_20 = GPIO.input(20)
    state_21 = GPIO.input(21)
    state_26 = GPIO.input(26)
    
    post = "pin_status,host=16 value=" + str(state_16) 
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    post = "pin_status,host=20 value=" + str(state_20) 
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    post = "pin_status,host=21 value=" + str(state_21) 
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    post = "pin_status,host=26 value=" + str(state_26) 
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post], stdout=FNULL, stderr=FNULL)
    
    time.sleep(30)
