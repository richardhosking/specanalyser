#!/usr/bin/python3

# Display window and main program for spectrum analyser
# Currently simulates a display with noise floor and a single carrier
# Keypad layout 
# (7 Jan 2020)
# Using Python 3 
# Raspberry Pi interface

import tkinter as tk  

import display
import keys

# Main window 
mainwindow = tk.Tk()
mainwindow.title("Spectrum Analyser")

# Fit mainwindow to screen
w, h = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
mainwindow.geometry("%dx%d+0+0" % (w, h))

# Get project wide graphics options 
mainwindow.option_readfile('options.txt')

# Project wide variables
# Use tkinter variable classes so can use trace as an interrupt

# setup a dictionary with global data 
projectData = {} 

# Current function Key
functionKeysEntry = tk.StringVar()
# Trace function
def updateFunctionKeysEntry(*args):
	keys.update()
	output.update(projectData)
# Callback calls trace function when variable changes
functionKeysEntry.trace('w', updateFunctionKeysEntry)
# Add entry to dictionary
projectData['functionKey'] = functionKeysEntry

# KeypadEntry digits
keypadEntry = tk.IntVar()
# Trace function
def updateKeypadEntry(*args):
	result = keys.update()
	# Add latest result to global variables 
	projectData[result[0]].set(result[1])
	projectData['latestResult'] = result
	output.update(projectData)
functionKeysEntry.trace('w', updateKeypadEntry)
# Add entry to dictionary
projectData['keypad'] = keypadEntry


# Scan start
startFreq = tk.DoubleVar()
startFreq.set(100)
def updateStartFreq(*args):
	output.update(projectData)
startFreq.trace('w', updateStartFreq)
projectData['startFreq'] = startFreq

# Scan stop
stopFreq = tk.DoubleVar()
stopFreq.set(2200)
def updateStopFreq(*args):
	output.update(projectData)
stopFreq.trace('w', updateStopFreq)
projectData['stopFreq'] = stopFreq


#import ADC

# Setup main display components 

# Function keys column 1 row 0
otherKeysWindow = tk.Frame(mainwindow, height=600, width=200, bg = 'SlateGray4')
otherKeysWindow.grid(column = 1,  row = 0, sticky='NS')
# and pass widget to Class constructor
otherKeys = keys.OtherKeys(otherKeysWindow, projectData)

# Digit Keypad column 2
keypadWindow = tk.Frame(mainwindow, height=600, width=200, bg = 'SlateGray3')
keypadWindow.grid(column = 2,  row = 0, sticky='NS')
keys = keys.Keypad(keypadWindow,projectData)

#adc = ADC.ADC()
#adc.setup_port()
#data = adc.get_data()

# Canvas to display spectrum analyser output
display_window = tk.Canvas(mainwindow, height=600, width=800)
display_window.grid(column = 0, row = 0, sticky='NS')
# output - instance of object Display from module display with display_window passed to it
output=display.Display(display_window, projectData)
output.initialize()
output.write_units()

# scan continuously method .after allows this 
output.sim_scan()
output.write_marker()

mainwindow.mainloop()




