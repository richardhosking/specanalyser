"""
Function keys 

"""

from tkinter import *


class OtherKeys:            
    
    def __init__(self, container, projectData):
        self.keypad = container     # tkinter widget enclosing other keys
        self.functionKey = projectData['functionKey']  # which key has been pressed
        
               # Keypad widgets
        btn = Button(self.keypad, text=" GHz ",   command=self.GHz, height = 3, width = 10)
        btn.grid(column=0, row=0, padx=20, pady=10 )

        btn = Button(self.keypad, text=" MHz ",   command=self.MHz, height = 3, width = 10)
        btn.grid(column=0, row=1, padx=20, pady=10 )

        btn = Button(self.keypad, text=" KHz ",   command=self.KHz, height = 3, width = 10)
        btn.grid(column=0, row=2, padx=20, pady=10 )

        btn = Button(self.keypad, text="Centre",   command=self.Centre, height = 3, width = 10)
        btn.grid(column=0, row=3, padx=20, pady=10 )

        btn = Button(self.keypad, text=" Bandwidth ",   command=self.RBW, height = 3, width = 10)
        btn.grid(column=0, row=4, padx=20, pady=10 )

        btn = Button(self.keypad, text="Span ",   command=self.Span, height = 3, width = 10)
        btn.grid(column=0, row=5, padx=20, pady=10 )
        
        btn = Button(self.keypad, text="Sweep ",   command=self.Sweep, height = 3, width = 10)
        btn.grid(column=1, row=2, padx=20, pady=10 )
        
        btn = Button(self.keypad, text=" Freq Start ",   command=self.freqStart, height = 3, width = 10)
        btn.grid(column=1, row=0, padx=20, pady=10 )

        btn = Button(self.keypad, text="Freq Stop ",   command=self.freqStop, height = 3, width = 10)
        btn.grid(column=1, row=1, padx=20, pady=10 )
        
    # key handlers    
    def GHz(self):
        self.functionKey.set("GHz") 
    
    def MHz(self):
        self.functionKey.set("MHz") 
        
    def KHz(self):
        self.functionKey.set("KHz") 
    
    def RBW(self):
        self.functionKey.set("Bandwidth") 

    def Centre(self):
        self.functionKey.set("Centre") 
    
    def Span(self):
        self.functionKey.set("Frequency Span") 
        
    def Sweep(self):
        self.functionKey.set("Sweep") 
        
    def freqStart(self):
        self.functionKey.set("startFreq") 
        
    def freqStop(self):
        self.functionKey.set("stopFreq") 
           
                
    
# End of class OtherKeys        
        


