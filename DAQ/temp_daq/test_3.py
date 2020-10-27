import adafruit_dht
#from ISStreamer.Streamer import Streamer
import time
import board

# --------- User Settings ---------
SENSOR_LOCATION_NAME = "Office"
BUCKET_NAME = ":partly_sunny: Room Temperatures"
BUCKET_KEY = "dht22sensor"
ACCESS_KEY = "ENTER ACCESS KEY HERE"
MINUTES_BETWEEN_READS = 1
METRIC_UNITS = True
# ---------------------------------

dhtSensor = adafruit_dht.DHT22(board.D4)
#streamer = Streamer(bucket_name=BUCKET_NAME, bucket_key=BUCKET_KEY, access_key=ACCESS_KEY)

while True:
        humidity = dhtSensor.humidity
        temp_c = dhtSensor.temperature
        #if METRIC_UNITS:
        #        #streamer.log(SENSOR_LOCATION_NAME + " Temperature(C)", temp_c)
        #else:
        #        #temp_f = format(temp_c * 9.0 / 5.0 + 32.0, ".2f")
        #        #streamer.log(SENSOR_LOCATION_NAME + " Temperature(F)", temp_f)
        humidity = format(humidity,".2f")
        print(humidity ,temp_c)
        #streamer.log(SENSOR_LOCATION_NAME + " Humidity(%)", humidity)
        #streamer.flush()
        
        time.sleep(3)
        
