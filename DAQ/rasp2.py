import io
import subprocess
import time
import psutil
import os

FNULL = open(os.devnull, 'w')
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
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
     "--data-binary", post], stdout=FNULL, stderr=FNULL)
    post = "raspi_temp,host=1 value=" + str(temp)
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
     "--data-binary", post], stdout=FNULL, stderr=FNULL)
    time.sleep(5)
