# This file has code for Spectrum Analyser interface 
# Keypad
# Frequency and bandwidth and marker data can be entered via
# a touchscreen interface 
# (?Sweep)

from tkinter import * 

class Keypad:
    
    # Handlers have to be declared first
    
    def keypad1():
        pass
    
    def keypad2():
        pass
        
    def keypad3():
        pass
    
    def keypad4():
        pass 

    def keypad5():
        pass
    
    def keypad6():
        pass
        
    def keypad7():
        pass
    
    def keypad8():
        pass 

    def keypad9():
        pass
    
    def keypadclear():
        pass
        
    def keypad0():
        pass
    
    def keypadback():
        pass
        
    def clickedUpdate():
        pass        
   
    def __init__(self, container):
        self.keypad = container

        #KEYPAD
        # Keypad widgets
        
        lbl = Label(self.keypad, text="Data entered", height = 1, width = 12)
        lbl.grid(column=0, row=0, columnspan = 3)

        entryBoxText= StringVar()
        entryBoxText = '2223'
        entryBox = Entry(self.keypad, width=10,  text = entryBoxText, font=('arial', 24))
        entryBox.grid(column=0, row=1, columnspan = 3)
        
        
        btn = Button(self.keypad, text=" 1 ",   command=self.keypad1, height = 3, width = 3)
        btn.grid(column=0, row=2, padx=10, pady=10)

        btn = Button(self.keypad, text=" 2 ",   command=self.keypad2, height = 3, width = 3)
        btn.grid(column=1, row=2, padx=10, pady=10)

        btn = Button(self.keypad, text=" 3 ",   command=self.keypad3, height = 3, width = 3)
        btn.grid(column=2, row=2, padx=10, pady=10)

        btn = Button(self.keypad, text=" 4 ",   command=self.keypad4, height = 3, width = 3)
        btn.grid(column=0, row=3, padx=10, pady=10)

        btn = Button(self.keypad, text=" 5 ",   command=self.keypad5, height = 3, width = 3)
        btn.grid(column=1, row=3, padx=10, pady=10)

        btn = Button(self.keypad, text=" 6 ",   command=self.keypad6, height = 3, width = 3)
        btn.grid(column=2, row=3, padx=10, pady=10)

        btn = Button(self.keypad, text=" 7 ",   command=self.keypad7, height = 3, width = 3)
        btn.grid(column=0, row=4, padx=10, pady=10)

        btn = Button(self.keypad, text=" 8 ",   command=self.keypad8, height = 3, width = 3)
        btn.grid(column=1, row=4, padx=10, pady=10)

        btn = Button(self.keypad, text=" 9 ",   command=self.keypad9, height = 3, width = 3)
        btn.grid(column=2, row=4, padx=10, pady=10)

        btn = Button(self.keypad, text=" C ",   command=self.keypadclear, height = 3, width = 3)
        btn.grid(column=0, row=5, padx=10, pady=10)

        btn = Button(self.keypad, text=" 0 ",   command=self.keypad0, height = 3, width = 3)
        btn.grid(column=1, row=5, padx=10, pady=10)

        btn = Button(self.keypad, text=" < ",   command=self.keypadback, height = 3, width = 3)
        btn.grid(column=2, row=5, padx=10, pady=10)
        
       # Update  
        btn = Button(self.keypad, text="Update", command=self.clickedUpdate, height = 3, width = 10)
        btn.grid(column=0, row=6, columnspan = 3, padx=20, pady=10)                

 
        
# End of class Keypad
    
class OtherKeys:    
    
    def GHz():
        pass
    
    def MHz():
        pass
        
    def KHz():
        pass
    
    def RBW():
        pass 

    def Centre():
        pass
    
    def Span():
        pass
        
    def sweep():
        pass
        
    def freqStart():
        pass
        
    def freqStop():
        pass
        
    
        
    
    def __init__(self, container):
        self.keypad = container
        
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
        
        btn = Button(self.keypad, text="Sweep ",   command=self.sweep, height = 3, width = 10)
        btn.grid(column=1, row=2, padx=20, pady=10 )
        
        btn = Button(self.keypad, text=" Freq Start ",   command=self.freqStart, height = 3, width = 10)
        btn.grid(column=1, row=0, padx=20, pady=10 )

        btn = Button(self.keypad, text="Freq Stop ",   command=self.freqStop, height = 3, width = 10)
        btn.grid(column=1, row=1, padx=20, pady=10 )
        


                        
                
    
# End of class OtherKeys        
        


