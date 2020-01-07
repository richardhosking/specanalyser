#!/usr/bin/python3

# Display window and main program for spectrum analyser
# Currently simulates a display with noise floor and a single carrier
# Yeypad layout 
# (7 Jan 2020)
# Using Python 3 
# Ultimately a Raspberry Pi interface

import tkinter as tk  
import display
import keys

#import ADC

# Main window 
mainwindow = tk.Tk()
mainwindow.title("Spectrum Analyser")

# Fit mainwindow to screen
w, h = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
mainwindow.geometry("%dx%d+0+0" % (w, h))

# Get project wide graphics options 
mainwindow.option_readfile('options.txt')

# Setup main display components 

# Function keys column 1 row 0
other_keys_window = tk.Frame(mainwindow, height=600, width=200, bg = 'SlateGray4')
other_keys_window.grid(column = 1,  row = 0, sticky='NS')
# and pass widget to Class constructor
other_keys = keys.OtherKeys(other_keys_window)

# Same for Keypad column 2
keypad_window = tk.Frame(mainwindow, height=600, width=200, bg = 'SlateGray3')
keypad_window.grid(column = 2,  row = 0, sticky='NS')
keys = keys.Keypad(keypad_window)

#adc = ADC.ADC()
#adc.setup_port()
#data = adc.get_data()

# Canvas to display spectrum analyser output
display_window = tk.Canvas(mainwindow, height=600, width=800)
display_window.grid(column = 0, row = 0, sticky='NS')
# output - instance of object Display from module display with display_window passed to it
output=display.Display(display_window)
output.initialize()
output.write_units()

# scan continuously method .after allows this 
output.sim_scan()
output.write_marker()

mainwindow.mainloop()




