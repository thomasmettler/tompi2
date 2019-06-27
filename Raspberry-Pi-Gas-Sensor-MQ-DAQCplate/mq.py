
# adapted from sandboxelectronics.com/?p=165

import time
import math
from MCP3008 import MCP3008

class MQ():

    ######################### Hardware Related Macros #########################
    MQ_PIN                       = 0        # define which analog input channel you are going to use (MCP3008)
    RL_VALUE                     = 5        # define the load resistance on the board, in kilo ohms
    RO_CLEAN_AIR_FACTOR          = 9.83     # RO_CLEAR_AIR_FACTOR=(Sensor resistance in clean air)/RO,
                                            # which is derived from the chart in datasheet
 
    ######################### Software Related Macros #########################
    CALIBARAION_SAMPLE_TIMES     = 50#50       # define how many samples you are going to take in the calibration phase
    CALIBRATION_SAMPLE_INTERVAL  = 50#500      # define the time interal(in milisecond) between each samples in the
                                            # cablibration phase
    READ_SAMPLE_INTERVAL         = 20       # define how many samples you are going to take in normal operation
    READ_SAMPLE_TIMES            = 100#5        # define the time interal(in milisecond) between each samples in 
                                            # normal operation
 
    ######################### Application Related Macros ######################
    GAS_LPG                      = 0
    GAS_CO                       = 1
    GAS_SMOKE                    = 2
    GAS_LPG2                     = 3

    def __init__(self, Ro=10, analogPin=0):
        self.Ro = Ro
        self.MQ_PIN = analogPin
        self.adc = MCP3008()
        
        self.Temp = [0,0]
        
        self.LPGCurve = [2.3,0.21,-0.47]    # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent"
                                            # to the original curve. 
                                            # data format:{ x, y, slope}; point1: (lg200, 0.21), point2: (lg10000, -0.59) 
        self.COCurve = [2.3,0.72,-0.34]     # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg200, 0.72), point2: (lg10000,  0.15)
        self.SmokeCurve =[2.3,0.53,-0.44]   # two points are taken from the curve. 
                                            # with these two points, a line is formed which is "approximately equivalent" 
                                            # to the original curve.
                                            # data format:[ x, y, slope]; point1: (lg200, 0.53), point2: (lg10000,  -0.22)  
                                            
        #Tom version of calibration data sheet
        self.LPGCurve_tom = [200,1.62,-0.000162755]    # two points are taken from the curve. p1: 200, 1.62  p2: 10000, 0.25
                                                # with these two points, a line is formed which is "approximately equivalent"
                                                # to the original curve. 
                                                # data format:{ x, y, slope}; point1: (lg200, 0.21), point2: (lg10000, -0.59) 
        self.COCurve_tom = [200, 5.2, -0.000379009]     # two points are taken from the curve. 1: 200, 5.2  p2: 10000, 1.4
                                                # with these two points, a line is formed which is "approximately equivalent" 
                                                # to the original curve.
                                                # data format:[ x, y, slope]; point1: (lg200, 0.72), point2: (lg10000,  0.15)
        self.SmokeCurve_tom =[200,3.4,-0.000295918]   # two points are taken from the curve. 1: 200, 3.4  p2: 10000, 0.5
                                                # with these two points, a line is formed which is "approximately equivalent" 
                                                # to the original curve.
                                                # data format:[ x, y, slope]; point1: (lg200, 0.53), point2: (lg10000,  -0.22)  
                
        print("Calibrating...")
        self.Ro = self.MQCalibration(self.MQ_PIN)
        print("Calibration is done...\n")
        print("Ro=%f kohm" % self.Ro)
    
    
    def MQPercentage(self):
        val = {}
        read = self.MQRead(self.MQ_PIN)
        #print "read value: " , read
        #print "self.Ro = " , self.Ro
        self.Temp = self.GetTemp()
        #print "self.Temp = " ,self.Temp[0]
        #print "self.Humid = " ,self.Temp[1]
        Rs_Ro = read/self.Ro+(60-self.Temp[1])*0.18 + (20-self.Temp[0])*0.23
        #print "RsRo before: ", read/self.Ro
        #print "RsRo after: ", Rs_Ro
        val["GAS_LPG"]  = self.MQGetGasPercentage(read/self.Ro, self.GAS_LPG)
        val["CO"]       = self.MQGetGasPercentage(read/self.Ro, self.GAS_CO)
        val["SMOKE"]    = self.MQGetGasPercentage(read/self.Ro, self.GAS_SMOKE)
        #val["GAS_LPG2"] = self.MQGetGasPercentage(read/self.Ro, self.GAS_LPG2)
        return val
        
    def MQPercentage_tom(self):
        val = {}
        read = self.MQRead(self.MQ_PIN)
        #print "read value: " , read
        #print "self.Ro = " , self.Ro
        val["GAS_LPG"]  = self.MQGetGasPercentage_tom(read/self.Ro, self.GAS_LPG)
        val["CO"]       = self.MQGetGasPercentage_tom(read/self.Ro, self.GAS_CO)
        val["SMOKE"]    = self.MQGetGasPercentage_tom(read/self.Ro, self.GAS_SMOKE)
        #val["GAS_LPG2"] = self.MQGetGasPercentage_tom(read/self.Ro, self.GAS_LPG2)
        return val
        
    ######################### MQResistanceCalculation #########################
    # Input:   raw_adc - raw value read from adc, which represents the voltage
    # Output:  the calculated sensor resistance
    # Remarks: The sensor and the load resistor forms a voltage divider. Given the voltage
    #          across the load resistor and its resistance, the resistance of the sensor
    #          could be derived.
    ############################################################################ 
    def MQResistanceCalculation(self, raw_adc): 
        #print "rawadc: ", raw_adc
        if raw_adc!=0:
            RS_VALUE = ((self.RL_VALUE * 5.0 / float(raw_adc)) - self.RL_VALUE) / self.RO_CLEAN_AIR_FACTOR
        else:
            RS_VALUE = self.Ro
        #RS_VALUE3 = (self.RL_VALUE * 1023.0 / float(raw_adc)) - self.RL_VALUE
        #RS_VALUE2 = float(self.RL_VALUE*(1023.0-raw_adc)/float(raw_adc));
        #print "RS value: ", RS_VALUE 
        #print "RS value: ", RS_VALUE2 
        return RS_VALUE
     
     
    ######################### MQCalibration ####################################
    # Input:   mq_pin - analog channel
    # Output:  Ro of the sensor
    # Remarks: This function assumes that the sensor is in clean air. It use  
    #          MQResistanceCalculation to calculates the sensor resistance in clean air 
    #          and then divides it with RO_CLEAN_AIR_FACTOR. RO_CLEAN_AIR_FACTOR is about 
    #          10, which differs slightly between different sensors.
    ############################################################################ 
    def MQCalibration(self, mq_pin):
        val = 0.0
        for i in range(self.CALIBARAION_SAMPLE_TIMES):          # take multiple samples
            val += self.MQResistanceCalculation(self.adc.read(mq_pin))
            time.sleep(self.CALIBRATION_SAMPLE_INTERVAL/1000.0)
            
        val = val/self.CALIBARAION_SAMPLE_TIMES                 # calculate the average value

        val = val/self.RO_CLEAN_AIR_FACTOR                      # divided by RO_CLEAN_AIR_FACTOR yields the Ro 
                                                                # according to the chart in the datasheet 
        #print "val: ", val
        return val;
      
      
    #########################  MQRead ##########################################
    # Input:   mq_pin - analog channel
    # Output:  Rs of the sensor
    # Remarks: This function use MQResistanceCalculation to caculate the sensor resistenc (Rs).
    #          The Rs changes as the sensor is in the different consentration of the target
    #          gas. The sample times and the time interval between samples could be configured
    #          by changing the definition of the macros.
    ############################################################################ 
    def MQRead(self, mq_pin):
        rs = 0.0

        for i in range(self.READ_SAMPLE_TIMES):
            rs += self.MQResistanceCalculation(self.adc.read(mq_pin))
            time.sleep(self.READ_SAMPLE_INTERVAL/1000.0)

        rs = rs/self.READ_SAMPLE_TIMES

        return rs
     
    #########################  MQGetGasPercentage ##############################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          gas_id      - target gas type
    # Output:  ppm of the target gas
    # Remarks: This function passes different curves to the MQGetPercentage function which 
    #          calculates the ppm (parts per million) of the target gas.
    ############################################################################ 
    def MQGetGasPercentage(self, rs_ro_ratio, gas_id):
        if ( gas_id == self.GAS_LPG ):
            return self.MQGetPercentage(rs_ro_ratio, self.LPGCurve)
        elif ( gas_id == self.GAS_CO ):
            return self.MQGetPercentage(rs_ro_ratio, self.COCurve)
        elif ( gas_id == self.GAS_SMOKE ):
            return self.MQGetPercentage(rs_ro_ratio, self.SmokeCurve)
        elif ( gas_id == self.GAS_LPG2 ):
            print "Percentage"
            return self.MQGetPercentage2(rs_ro_ratio, self.LPGCurve2)
        return 0
        
    def MQGetGasPercentage_tom(self, rs_ro_ratio, gas_id):
        if ( gas_id == self.GAS_LPG ):
            return self.MQGetPercentage_tom(rs_ro_ratio, self.LPGCurve)
        elif ( gas_id == self.GAS_CO ):
            return self.MQGetPercentage_tom(rs_ro_ratio, self.COCurve)
        elif ( gas_id == self.GAS_SMOKE ):
            return self.MQGetPercentage_tom(rs_ro_ratio, self.SmokeCurve)
        elif ( gas_id == self.GAS_LPG2 ):
            print "Percentage"
            return self.MQGetPercentage_tom(rs_ro_ratio, self.LPGCurve2)
        return 0
     
    #########################  MQGetPercentage #################################
    # Input:   rs_ro_ratio - Rs divided by Ro
    #          pcurve      - pointer to the curve of the target gas
    # Output:  ppm of the target gas
    # Remarks: By using the slope and a point of the line. The x(logarithmic value of ppm) 
    #          of the line could be derived if y(rs_ro_ratio) is provided. As it is a 
    #          logarithmic coordinate, power of 10 is used to convert the result to non-logarithmic 
    #          value.
    ############################################################################ 
    def MQGetPercentage(self, rs_ro_ratio, pcurve):
        #print "calculation"
        return (math.pow(10,( ((math.log(rs_ro_ratio)-pcurve[1])/ pcurve[2]) + pcurve[0])))
        
    def MQGetPercentage_tom(self, rs_ro_ratio, pcurve):
        #print "calculation"
        concentration = (rs_ro_ratio - pcurve[1]) / pcurve[2]  + pcurve[0]
        return concentration
        
    def GetTemp(self):
        #print "calculation"
        with open('/home/pi/Tom_Stuff/somefile.txt') as f:
            Tmp = f.readline().split()
            if( len(Tmp) > 1 ):
                te = float(Tmp[0])
                hu = float(Tmp[1])
                Temp = [te,hu]
            else:
                Temp = self.Temp
        return Temp
        
