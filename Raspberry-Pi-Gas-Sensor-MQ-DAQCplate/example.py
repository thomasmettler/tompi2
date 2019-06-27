from mq import *
import sys, time
import subprocess
#try:
print("Press CTRL+C to abort.")
print "R_s = 2kOhm - 20 kOhm"
print "R_s/R_o = 0.1 - 10"
print "-> R_o = 200 Ohm - 200 kOhm"

mq = MQ();
while True:
    perc = mq.MQPercentage()
    sys.stdout.write("\r")
    sys.stdout.write("\033[K")
    sys.stdout.write("LPG: %g ppm, CO: %g ppm, Smoke: %g ppm\n" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
    post = "MQ2_sensor,no=LPG value=" + str(perc["GAS_LPG"])
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb_calib", "--data-binary", post])
    post = "MQ2_sensor,no=CO value=" + str(perc["CO"])
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb_calib", "--data-binary", post])
    post = "MQ2_sensor,no=SMOKE value=" + str(perc["SMOKE"])
    subprocess.call(["curl", "-i", "-XPOST", "localhost:8086/write?db=mydb_calib", "--data-binary", post])
    
    sys.stdout.flush()
    time.sleep(0.1)
    #perc = mq.MQPercentage_tom()
    #sys.stdout.write("\r")
    #sys.stdout.write("\033[K")
    #sys.stdout.write("Tom LPG: %g ppm, CO: %g ppm, Smoke: %g ppm\n" % (perc["GAS_LPG"], perc["CO"], perc["SMOKE"]))
    #sys.stdout.flush()
    #time.sleep(0.1)

#except:
#    print("\nAbort by user")
