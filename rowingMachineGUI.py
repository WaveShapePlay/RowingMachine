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
        
        self.btn_Start= tk.Button(root, text="Start", command=self.startWorkout)
        self.btn_Start.grid(row=0, column=0)

        self.lbl_StartTime = tk.Label(root, font=("times", 50, "bold"))
        self.lbl_StartTime.grid(row=1, column=0)

        self.btn_Stop = tk.Button(root, text="Stop", command=self.stopWorkout, state = DISABLED)
        self.btn_Stop.grid(row=0, column=1)

        self.lbl_StopTime = tk.Label(root, font=("times", 50, "bold"))
        self.lbl_StopTime.grid(row=1, column=1)

        self.reedSpeed = tk.Label(root, font=("times", 50, "bold"))
        self.reedSpeed.grid(row = 2, column =0)

        self.totalRowingTime = tk.Label(root, font=("times", 50, "bold"))
        self.totalRowingTime.grid(row = 3, column =0)

        self.clock = tk.Label(root, font=("times", 25, "bold"))
        self.clock.grid(row = 4, column =0)

        self.time_update()
        #self.testVal = self.testValue()
        self.rowingValueUpdate(self.reedSpeed,self.totalRowingTime)
        
        
    def startWorkout(self):
        ser.write(b's')
        self.startTime = time.strftime("%H:%M:%S")
        self.lbl_StartTime.config(text=self.startTime)
        self.btn_Start.config(state = DISABLED)
        self.btn_Stop.config(state = NORMAL)
        self.startCount += 1
        if self.startCount > 1:
            self.lbl_StopTime.config(text=" ")
            ser.write(b's')
            
    def stopWorkout(self):
        ser.write(b'x')
        self.stopTime = time.strftime("%H:%M:%S")
        self.lbl_StopTime.config(text=self.stopTime)
        self.btn_Start.config(state = NORMAL)
        self.btn_Stop.config(state = DISABLED)
    '''
    def testValue(self):
        test = str(random.randrange(300,1000,1))
        return test
    '''
    
    def time_update(self):
        self.current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=self.current_time)
        self.clock.after(300, self.time_update)

    def rowingValueUpdate(self,reedSpeed,totalRowingTime):
        self.reedValList = list()
        self.totalSumTime = int()
        
        def update():
            self.value = self.getData()
            print(self.value)
            self.reedSpeed.after(300, update)
            try:
                self.value = int(self.value)
                self.reedValList.append(self.value)
                self.reedValList = self.reedValList[-10:]
                self.totalSumTime += int(self.reedValList[-1])
                print("in update() try" + str(self.value))
                self.reedSpeed.config(text=self.value)
                self.totalRowingTime.config(text=self.totalSumTime)
            except:
                print("Waiting for data")
            print(self.reedValList)
            #print("testList")
            #print(self.testList)
            #print(self.totalSumTime)

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
