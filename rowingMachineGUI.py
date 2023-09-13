import serial
from tkinter import *
import tkinter as tk
import time
import random

commPort = '/dev/cu.usbmodem14401'
ser = serial.Serial(commPort, baudrate = 9600, timeout = 1)
numTime = 0
totalSumTime = 0

class rowingGUI:

    def __init__(self,master):
        self.master = master
        master.title("Rowing Machine")

        self.startCount = 0
        self.runningReedCount = 0
        
        self.btn_Start= tk.Button(root, text="Start", command=self.startWorkout)
        self.btn_Start.grid(row=0, column=0)

        self.lbl_StartTime = tk.Label(root, font=("times", 50, "bold"))
        self.lbl_StartTime.grid(row=1, column=0)

        self.btn_Stop = tk.Button(root, text="Stop", command=self.stopWorkout, state = DISABLED)
        self.btn_Stop.grid(row=0, column=1)

        self.lbl_StopTime = tk.Label(root, font=("times", 50, "bold"))
        self.lbl_StopTime.grid(row=1, column=1)

        self.reedRunningCountLabel = tk.Label(root, text = "Count: ", font=("times", 50, "bold"))
        self.reedRunningCountLabel.grid(row = 2, column =0)

        self.reedRunningCount = tk.Label(root, font=("times", 50, "bold"))
        self.reedRunningCount.grid(row = 2, column =1)

        self.clock = tk.Label(root, font=("times", 25, "bold"))
        self.clock.grid(row = 3, column =0)

        self.time_update()
        self.rowingValueUpdate()
        
        
    def startWorkout(self):
        ser.write(b's')
        self.startTime = time.strftime("%H:%M:%S")
        self.lbl_StartTime.config(text=self.startTime)
        self.btn_Start.config(state = DISABLED)
        self.btn_Stop.config(state = NORMAL)
        self.startCount += 1
        self.runningReedCount = 0
        if self.startCount > 1:
            self.lbl_StopTime.config(text=" ")
            ser.write(b's')
            
    def stopWorkout(self):
        ser.write(b'x')
        self.stopTime = time.strftime("%H:%M:%S")
        self.lbl_StopTime.config(text=self.stopTime)
        self.btn_Start.config(state = NORMAL)
        self.btn_Stop.config(state = DISABLED)
    
    def time_update(self):
        self.current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time)
        self.clock.after(300, self.time_update)

    def rowingValueUpdate(self):
        self.reedValList = list()
        
        def update():
            self.value = self.getData()
            self.value = self.value.rstrip()
            self.reedRunningCount.after(300, update)
            try:
                if self.value == 'r':
                    self.runningReedCount += 1
                    textRunningCount = str(self.runningReedCount)
                    self.reedRunningCount.config(text=textRunningCount)
                
            except:
                pass

        update()

    def getData(self):
        ser.write(b'd')
        rawData = ser.readline().decode('ascii')
        print("in getData")
        return rawData
    
# creating tkinter window 
root = Tk()
rowingApp = rowingGUI(root)
root.geometry("350x350")
root.mainloop()
