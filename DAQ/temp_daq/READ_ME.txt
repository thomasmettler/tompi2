pi@raspberrypi:~ $ python3
Python 3.7.3 (default, Dec 20 2019, 18:57:59)
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import board
>>> import adafruit_dht
>>> dht = adafruit_dht.DHT22(board.D17)
>>> dht.temperature
27.0
>>>
