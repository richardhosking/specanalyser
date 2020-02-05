# This file has code for Spectrum Analyser interface 
# Keypad
# Frequency and bandwidth and marker data can be entered via
# a touchscreen interface 
# (?Sweep)

from tkinter import *


class Keypad:
    # Class variables


    def __init__(self, container,projectData):
        # Keypad object
        self.keypad = container
        self.projectData = projectData
        self.keypadEntry = projectData['keypad']  # parameter to  to update with keypad entry        
        self.functionKey = projectData['functionKey']  # Label text 
               
        self.lbl = Label(self.keypad, text= self.functionKey.get(), width = 16, height = 1)
        self.lbl.grid(column=0, row=0, columnspan = 3)
        
        #self.entryBoxText= StringVar()   
        self.entryBox = Entry(self.keypad, width=10, font=('arial', 24))
        self.entryBox.grid(column=0, row=1, columnspan = 3)
        
        
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

    # Keypad handlers    
    def keypad1(self):
        self.entryBox.insert(END,"1") 
    def keypad2(self):
        self.entryBox.insert(END,"2") 
    def keypad3(self):
        self.entryBox.insert(END, "3") 
    def keypad4(self):
        self.entryBox.insert(END, "4") 
    def keypad5(self):
        self.entryBox.insert(END, "5") 
    def keypad6(self):
        self.entryBox.insert(END, "6") 
    def keypad7(self):
        self.entryBox.insert(END, "7") 
    def keypad8(self):
        self.entryBox.insert(END, "8") 
    def keypad9(self):
        self.entryBox.insert(END, "9") 
    def keypad0(self):
        self.entryBox.insert(END, "0") 
    # Clear data 
    def keypadclear(self):
        self.entryBox.delete(0, END)
    def keypadback(self):
        # Go back one character 
        data = self.entryBox.get()
        index = len(data)-1
        self.entryBox.delete(index)     
       
    def clickedUpdate(self):
        self.keypadEntry.set(self.entryBox.get()) 
        functionKey = self.projectData['functionKey'].get()
        self.lbl['text'] = functionKey

        self.entryBox.delete(0, END)
                
    def update(self):

        result = [self.projectData['functionKey'].get(), self.keypadEntry.get()]

        return result
        
# End of class Keypad
    
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
        


