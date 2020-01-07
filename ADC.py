""" Module to drive the MCP3004 ADC via a serial interface 
    from a Raspberry Pi

"""
import RPi.GPIO as io # using RPi.GPIO
io.setmode(io.BOARD)  # straight pin assignment 
  
HIGH = 1 
LOW = 0
    
class ADC:
    
    def __init__(self):
        
        # Port pin assignments 
        self.chipSelect = 400 
        self.serialClock = 402 
        self.serialDataIn = 403 
        self.serialDataOut = 401 
        self.dataWord = 0b0000000000   # 10 bit data word 
        self.setupWord = 0b111000000
        
    def setup_port(self):
        io.setup(self.chipSelect,io.OUT) # make pin into an output   
        io.setup(self.serialClock,io.OUT) 
        io.setup(self.serialDataIn,io.OUT) 
        io.setup(serialDataOut, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 
        
        
    def get_data(self):
        # Chip setup
        # ChipSelect high- low to initiate transfer
        io.output(self,chipSelect, HIGH)
        io.output(self,chipSelect, LOW)
        # DataIn high as a start bit 
        # SerialClock high- low - clock in start bit 
        # DataIn high 1X single ended input - second bit dont care for 3004
        # DataIn low 00 CH1 input 
        # and then another  
        # SerialClock high- low X2 to initiate sample period 
        # sample period will end on the falling edge of the second clock
        # hence setup data  111000000
        
        for i in range(0,len(setupWord)):
            io.output(serialDataIn, setupWord[i])
            io.output(self,serialClock, HIGH)
            io.output(self,serialClock, LOW)                   
        
        # Read data from ADC 
        # serialDataOut low - NULL bit
        # next 10 clocks will output 10 bit conversion word on the falling edge of the serial clock MSB first              
        for i in range(9,0):
            io.output(self,serialClock, HIGH)
            io.output(self,serialClock, LOW)       
            self.dataWord[i]= io.input(self,serialDataOut)
        
        return dataWord
        
# end of class ADC
