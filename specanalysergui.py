# This file has code for a Spectrum Analyser 
# using a Raspberry Pi as a display and interface 
# Frequency data can be entered via
# a touchscreen interface 
# Not working yet (V0) Jan 2020

from Tkinter import * 
import display

# Main window 
mainwindow = Tk()
mainwindow.title("Spectrum Analyser")
# Fit mainwindow to screen
w, h = mainwindow.winfo_screenwidth(), mainwindow.winfo_screenheight()
mainwindow.geometry("%dx%d+0+0" % (w, h))

#Frames
# Frequency control frame to enclose freq widgets
displayframe = Frame(mainwindow,  borderwidth = 10)
displayframe.grid(column = 0,   row = 0,  sticky=(N,S))

 
# Frame to enclose level widgets
levels = Frame(mainwindow, borderwidth = 10)
levels.grid(column = 1,  row = 0,  sticky=(N,S))

# Keys to enter data 
# Inside a frame called keypad
keypad = Frame(mainwindow,  borderwidth = 10, height=h-10, width=w-200)
keypad.grid(column = 2,  row = 0, sticky=N)

# Handlers - need to be declared before widget is defined
def clickedMute1():
    Gen1message =  StringVar()

    levlbl1 = Label(levels, text=Gen1message)
    levlbl1.grid(column=1, row=2,  padx=5)



def clickedUpdate():
    # these varaiables need to be a StringVar to be used in widget
    error = StringVar()
    errorText = StringVar()
    lbl1 = Label(keypad, textvariable=error)
    lbl1.grid(column=0, row=5)
    lbl2 = Label(keypad, textvariable=errorText)
    lbl2.grid(column=1, row=5,  columnspan=2)
    
#Insert digit at end of variable in window in focus   
def keypad1():
    mainwindow.focus_get().insert(END,"1") 
def keypad2():
    mainwindow.focus_get().insert(END,"2") 
def keypad3():
    mainwindow.focus_get().insert(END, "3") 
def keypad4():
    mainwindow.focus_get().insert(END, "4") 
def keypad5():
    mainwindow.focus_get().insert(END, "5") 
def keypad6():
    mainwindow.focus_get().insert(END, "6") 
def keypad7():
    mainwindow.focus_get().insert(END, "7") 
def keypad8():
    mainwindow.focus_get().insert(END, "8") 
def keypad9():
    mainwindow.focus_get().insert(END, "9") 
def keypad0():
    mainwindow.focus_get().insert(END, "0") 
# Clear data 
def keypadclear():
    mainwindow.focus_get().delete(0, END)
def keypadback():
    # Go back one character 
    data = mainwindow.focus_get().get()
    index = len(data)-1
    mainwindow.focus_get().delete(index) 

#FREQ FRAME
#Widgets frequency frame
lbl = Label(freq, text="Frequency")
lbl.grid(column=0, row=1)

lbl = Label(freq, text="Generator 1")
lbl.grid(column=0,   row=2)

freqGen1text= StringVar()
freqGen1 = Entry(freq,width=10,  textvariable=freqGen1text)
freqGen1.grid(column=0,  row=3,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1,  row=3)

# Spacer
lbl = Label(freq)
lbl.grid(column=0, row=4)

lbl = Label(freq, text="Generator 2")
lbl.grid(column=0,   row=5)

freqGen2text= StringVar()
freqGen2 = Entry(freq,width=10,  textvariable=freqGen2text)
freqGen2.grid(column=0, row=6,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1, row=6)

# Spacer
lbl = Label(freq)
lbl.grid(column=0, row=7)

lbl = Label(freq, text="Generator 3")
lbl.grid(column=0,  row=8)

freqGen3text= StringVar()
freqGen3 = Entry(freq,width=10,  textvariable=freqGen3text)
freqGen3.grid(column=0, row=9,  pady=3)

lbl = Label(freq, text="KHz")
lbl.grid(column=1, row=9)

#LEVEL FRAME
# Level widgets
lbl = Label(levels, text="Level")
lbl.grid(column=0, row=0)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=1)

mute1 = Button(levels, text="Power/Mute", command=clickedMute1)
mute1.grid(column=0, row=2)
levlbl1 = Label(levels, text='MUTED')
levlbl1.grid(column=1, row=2,  padx=5)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=3)
lbl = Label(levels)
lbl.grid(column=0, row=4)

mute2 = Button(levels, text="Power/Mute", command=clickedMute1)
mute2.grid(column=0, row=5)
levlbl2 = Label(levels, text='MUTED')
levlbl2.grid(column=1, row=2,  padx=5)

# Spacer
lbl = Label(levels)
lbl.grid(column=0, row=6)
lbl = Label(levels)
lbl.grid(column=0, row=7)

mute3 = Button(levels, text="Power/Mute", command=clickedMute1)
mute3.grid(column=0, row=8)
levlbl3 = Label(levels, text='MUTED')
levlbl3.grid(column=1, row=2,  padx=5)

#KEYPAD
# Keypad widgets
btn = Button(keypad, text=" 1 ",   command=keypad1, height = 3, width = 3)
btn.grid(column=0, row=0)

btn = Button(keypad, text=" 2 ",   command=keypad2, height = 3, width = 3)
btn.grid(column=1, row=0)

btn = Button(keypad, text=" 3 ",   command=keypad3, height = 3, width = 3)
btn.grid(column=2, row=0)

btn = Button(keypad, text=" 4 ",   command=keypad4, height = 3, width = 3)
btn.grid(column=0, row=1)

btn = Button(keypad, text=" 5 ",   command=keypad5, height = 3, width = 3)
btn.grid(column=1, row=1)

btn = Button(keypad, text=" 6 ",   command=keypad6, height = 3, width = 3)
btn.grid(column=2, row=1)

btn = Button(keypad, text=" 7 ",   command=keypad7, height = 3, width = 3)
btn.grid(column=0, row=2)

btn = Button(keypad, text=" 8 ",   command=keypad8, height = 3, width = 3)
btn.grid(column=1, row=2)

btn = Button(keypad, text=" 9 ",   command=keypad9, height = 3, width = 3)
btn.grid(column=2, row=2)

btn = Button(keypad, text=" C ",   command=keypadclear, height = 3, width = 3)
btn.grid(column=0, row=3)

btn = Button(keypad, text=" 0 ",   command=keypad0, height = 3, width = 3)
btn.grid(column=1, row=3)

btn = Button(keypad, text=" < ",   command=keypadback, height = 3, width = 3)
btn.grid(column=2, row=3)

# Update generator which has current focus 
btn = Button(keypad, text="Update Generator", command=clickedUpdate, height = 3)
btn.grid(column=0, row=4, columnspan = 3)




