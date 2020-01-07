# Class for displaying scanned data
from tkinter import *  #Tk, Canvas, Frame, BOTH
import random

class Display:
    def __init__(self, canvas):
        self.canvas = canvas   #     
        self.line_data=[]      # store line IDs to allow them to be deleted between scans
        self.RBW = 1.0
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

    def initialize(self):
                
        # write a grid on the display
        self.canvas.create_rectangle(0, 0, 800, 600, outline='black', fill='black')
        
        self.canvas.create_line(50, 50, 750, 50, fill='white')
        self.canvas.create_line(50, 50, 50, 550, fill='white')
        self.canvas.create_line(50, 550, 750, 550, fill='white')        
        self.canvas.create_line(750, 50, 750, 550, fill='white') 
                 
        self.canvas.create_line(120, 50, 120, 550, fill='white', dash=(1, 5))
        self.canvas.create_line(190, 50, 190, 550, fill='white', dash=(1, 5))
        self.canvas.create_line(260, 50, 260, 550, fill='white', dash=(1, 5))
        self.canvas.create_line(330, 50, 330, 550, fill='white', dash=(1, 5))   
        self.canvas.create_line(400, 50, 400, 550, fill='white', dash=(1, 5))
        self.canvas.create_line(470, 50, 470, 550, fill='white', dash=(1, 5)) 
        self.canvas.create_line(540, 50, 540, 550, fill='white', dash=(1, 5))
        self.canvas.create_line(610, 50, 610, 550, fill='white', dash=(1, 5)) 
        self.canvas.create_line(680, 50, 680, 550, fill='white', dash=(1, 5))
        
        self.canvas.create_line(50, 100, 750, 100, fill='white', dash=(1, 5))
        self.canvas.create_line(50, 150, 750, 150, fill='white', dash=(1, 5))
        self.canvas.create_line(50, 200, 750, 200, fill='white', dash=(1, 5))
        self.canvas.create_line(50, 250, 750, 250, fill='white', dash=(1, 5))   
        self.canvas.create_line(50, 300, 750, 300, fill='white', dash=(1, 5))
        self.canvas.create_line(50, 350, 750, 350, fill='white', dash=(1, 5)) 
        self.canvas.create_line(50, 400, 750, 400, fill='white', dash=(1, 5))
        self.canvas.create_line(50, 450, 750, 450, fill='white', dash=(1, 5)) 
        self.canvas.create_line(50, 500, 750, 500, fill='white', dash=(1, 5))

    # write data and units to display    
    def write_units(self):
        message1 = ("REF: " + str(self.reference) + ' '+ self.reference_unit)
        message2 = ("RBW: " + str(self.RBW) + ' '+ self.RBW_unit)
        message3 = ("Scale: " + str(self.scale) + ' '+ self.scale_unit)
        message5 = ("Start: " + str(self.start_freq) + ' '+ self.start_freq_unit)
        message6 = ("Stop: " + str(self.stop_freq) + ' '+ self.stop_freq_unit)        
        span = self.stop_freq - self.start_freq
        message4 = ("Span: " + str(span) + ' '+ self.stop_freq_unit)
                         
        self.canvas.create_text(100,25,fill="white",font="Arial 16 bold", text=message1)
        self.canvas.create_text(450,25,fill="white",font="Arial 16 bold", text=message2)
        self.canvas.create_text(275,25,fill="white",font="Arial 16 bold", text=message3)   
        self.canvas.create_text(450,575,fill="white",font="Arial 16 bold", text=message4) 
        self.canvas.create_text(100,575,fill="white",font="Arial 16 bold", text=message5)   
        self.canvas.create_text(275,575,fill="white",font="Arial 16 bold", text=message6)        
        
        # Display dB units on graticule 
        self.canvas.create_text(85,60,fill="white",font="Arial 12", text="0 dBm")
        self.canvas.create_text(85,100,fill="white",font="Arial 12", text="-10")
        self.canvas.create_text(85,150,fill="white",font="Arial 12", text="-20")   
        self.canvas.create_text(85,200,fill="white",font="Arial 12", text="-30")
        self.canvas.create_text(85,250,fill="white",font="Arial 12", text="-40")
        self.canvas.create_text(85,300,fill="white",font="Arial 12", text="-50")
        self.canvas.create_text(85,350,fill="white",font="Arial 12", text="-60")   
        self.canvas.create_text(85,400,fill="white",font="Arial 12", text="-70")
        self.canvas.create_text(85,450,fill="white",font="Arial 12", text="-80")   
        self.canvas.create_text(85,500,fill="white",font="Arial 12", text="-90")
                     
    # Marker    
    def write_marker(self):
        x=self.marker[0]
        y=self.marker[1]
        
        # Marker outline
        self.canvas.create_polygon([x,y,x-5,y-8,x+5,y-8], outline='red',fill='red')
        
        # Write values for marker position
        x1=int(2800*(x-50)/700)
        y1=int((-y+50)*100/500)
        message1 = ("Marker :  " + str(y1) + ' '+ "dBm")
        message2 = (str(x1) + ' '+ "MHz")
        
        # Location of marker message
        if x<600:
            x=x+75
        else:
            x=x-75
                
        self.canvas.create_text(x, y,fill="yellow",font="Arial 12", text=message1)
        self.canvas.create_text(x,y+25,fill="yellow",font="Arial 12", text=message2)
                
        # allows marker to written repeatedly 
        self.canvas.after(30, self.write_marker)
                        
           
        # Scan data once 
        # this method simulates real data - random noise plus a single carrier 
    def sim_scan(self):
        y1=475
        y2=500

        # First need to delete previous scan lines
        for j in range(0, len(self.line_data)):
            self.canvas.delete(self.line_data[j])
            
        for x in range(50,750):
            y=random.randint(440,505)
            # display a single carrier
            if (x==660):
                y=170
            line_id=self.canvas.create_line(x, y1, x+1, y, fill='orange')  # line ID to allow it to be deleted between scans  
            self.line_data.append(line_id)
            y1=y
            
            # store max Y with its x position 
            if y<y2:
                y2=y
                x1=x
                self.marker=[x1,y2]
        
        # after method allows program to run continuously - creates a separate thread 
        # delay in msec         
        self.canvas.after(30, self.sim_scan)

