#from spidev import SpiDev
import piplates.DAQCplate as DAQC

class MCP3008_MQ3:
    def __init__(self, bus = 0, device = 0):
        self.bus, self.device = bus, device
        #self.spi = SpiDev()
        self.open()

    def open(self):
        #self.spi.open(self.bus, self.device)
        print 'open'
    
    def read(self, channel = 0):
        #adc = self.spi.xfer2([1, (8 + channel) << 4, 0])
        #data = ((adc[1] & 3) << 8) + adc[2]
        data = DAQC.getADC(4,1)
        #print "measured: ", data
        return data
            
    def close(self):
        print 'close'
