import piplates.DAQCplate as DAQC
import subprocess
import time


adc = 0
while(1):
    adc = DAQC.getADC(4,3)
    print adc
    post = "MQ8_voltage,no=1 value=" + str(adc)
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb", "--data-binary", post])
    time.sleep(1)

