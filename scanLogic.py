"""
File to set rules about freq span, bandwidth based on Keypad input 
and calculate points on display

"""

import specanalyser as m

class Scan:
    
    def __init__(self):
        
        # main objects
        self.keypad = m.keys
        self.display = m.output
        self.other_keys = m.other_keys 
        
        # Variables
        self.RBW = m.RBW
        self.RBW_unit = "MHz"
        self.start_freq = 0.00
        self.start_freq_unit = "MHz"
        self.stop_freq = 2.8
        self.stop_freq_unit = "GHz"
        self.reference = 0 
        self.reference_unit = "dBm"
        self.scale = 10
        self.scale_unit = "dB/Div" 
        self.marker = [0,500]
        
        self.step = 1.0     # PLL step frequency in ?Hz
        
    def calculateSpan():
        pass
        
    def setBandwidth():
        pass
        
    def calculateStep():
        pass
        
    
        
        
