#!/usr/bin/python3

# Display window for spectrum analyser
# Currently simulates a display with noise floor and a single carrier
# (Jan 2020)
# Using Python 3 
# Ultimately a Raspberry Pi interface

from tkinter import *  
import display

# Main window 
mainwindow = Tk()
mainwindow.title("Spectrum Analyser")
# Fit mainwindow to screen
w, h = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
mainwindow.geometry("%dx%d+0+0" % (w, h))
# mainwindow.geometry('800x800')

# Canvas to display spectrum analyser output
display_window = Canvas(mainwindow, height=600, width=800)

# output - instance of object Display from module display with display_window passed to it
output=display.Display(display_window)

output.initialize()
output.write_units()

# scan continuously method .after allows this 
output.sim_scan()
output.write_marker()

mainwindow.mainloop()




