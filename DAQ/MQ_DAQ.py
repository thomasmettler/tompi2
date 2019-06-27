import time
import math
from MCP3008 import MCP3008
import subprocess
import os

import sys, time

#try:
while True:
    print("Press CTRL+C to abort.")
    READ_SAMPLE_INTERVAL         = 50       # of samples for mean building
    READ_SAMPLE_TIMES            = 0.005        # time in between [s]
    mq = MCP3008();
    FNULL = open(os.devnull, 'w')
    while True:
    
        adc_MQ2 = 0.0
        adc_MQ3 = 0.0
        adc_MQ7 = 0.0
        adc_MQ8 = 0.0
        adc_MQ135 = 0.0
        '''
        adc_MQ2 = mq.read(0)/1024.0*5.0
        adc_MQ3 = mq.read(0)/1024.0*3.3
        adc_MQ7 = mq.read(0)
        #adc_MQ8 = mq.read(3)/1024.0*5.0
        #adc_MQ135 = mq.read(4)/1024.0*5.0
        sys.stdout.write("N########################\n")
        sys.stdout.write("MQ2 5   Voltage: %g\n" % adc_MQ2)
        sys.stdout.write("MQ2 3.3  Voltage: %g\n" % adc_MQ3)
        sys.stdout.write("MQ2 raw  Voltage: %g\n" % adc_MQ7)
        #sys.stdout.write("MQ8   Voltage: %g\n" % adc_MQ8)
        #sys.stdout.write("MQ135 Voltage: %g\n" % adc_MQ135)
        sys.stdout.write("########################\n")
        
        adc_MQ2 = mq.read(0)
        adc_MQ3 = mq.read(1)
        adc_MQ7 = mq.read(2)
        adc_MQ8 = mq.read(3)
        adc_MQ135 = mq.read(4)
        sys.stdout.write("R########################\n")
        sys.stdout.write("MQ2   Voltage: %g\n" % adc_MQ2)
        sys.stdout.write("MQ3   Voltage: %g\n" % adc_MQ3)
        sys.stdout.write("MQ7   Voltage: %g\n" % adc_MQ7)
        sys.stdout.write("MQ8   Voltage: %g\n" % adc_MQ8)
        sys.stdout.write("MQ135 Voltage: %g\n" % adc_MQ135)
        sys.stdout.write("########################\n")
        sys.stdout.write("########################\n")
        adc_MQ2 = 0.0
        adc_MQ3 = 0.0
        adc_MQ7 = 0.0
        adc_MQ8 = 0.0
        adc_MQ135 = 0.0
        '''
        for i in range(READ_SAMPLE_INTERVAL):
            adc_MQ2 += mq.read(0)/1024.0*5.0
            adc_MQ3 += mq.read(1)/1024.0*5.0
            adc_MQ7 += mq.read(2)/1024.0*5.0
            adc_MQ8 += mq.read(3)/1024.0*5.0
            adc_MQ135 += mq.read(4)/1024.0*5.0
            time.sleep(READ_SAMPLE_TIMES)
            
        adc_MQ2 /= READ_SAMPLE_INTERVAL
        adc_MQ3 /= READ_SAMPLE_INTERVAL
        adc_MQ7 /= READ_SAMPLE_INTERVAL
        adc_MQ8 /= READ_SAMPLE_INTERVAL
        adc_MQ135 /= READ_SAMPLE_INTERVAL
           
        sys.stdout.write("MQ2   Voltage: %g\n" % adc_MQ2)
        sys.stdout.write("MQ3   Voltage: %g\n" % adc_MQ3)
        sys.stdout.write("MQ7   Voltage: %g\n" % adc_MQ7)
        sys.stdout.write("MQ8   Voltage: %g\n" % adc_MQ8)
        sys.stdout.write("MQ135 Voltage: %g\n" % adc_MQ135)
        sys.stdout.write("########################\n")

        post = "MQ2_voltage,no=1 value=" + str(adc_MQ2)
        subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
         "--data-binary", post], stdout=FNULL, stderr=FNULL)
        post = "MQ3_voltage,no=1 value=" + str(adc_MQ3)
        subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
         "--data-binary", post], stdout=FNULL, stderr=FNULL)
        post = "MQ7_voltage,no=1 value=" + str(adc_MQ7)
        subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
         "--data-binary", post], stdout=FNULL, stderr=FNULL)
        post = "MQ8_voltage,no=1 value=" + str(adc_MQ8)
        subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
         "--data-binary", post], stdout=FNULL, stderr=FNULL)
        post = "MQ135_voltage,no=1 value=" + str(adc_MQ135)
        subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb",
         "--data-binary", post], stdout=FNULL, stderr=FNULL)
        
        #sys.stdout.flush()
        time.sleep(1)

#except:
#    print("\nAbort by user")
