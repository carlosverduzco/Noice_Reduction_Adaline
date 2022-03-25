from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigCanvasTk
from tkinter import *
from plot import Plot
import threading
from adaline import Adaline
from archive import getX
from sys import exit

Font_tuple = ("Comic Sans MS", 20, "bold")

class GUI:
    def __init__(self):
        self.mainwindow = Tk()
        self.mainwindow.attributes("-fullscreen", True)
        self.mainwindow.config(bg='#18191A')
        self.mainwindow.wm_title('Adaline - Noise Reduction')

        #Plots
        self.plotInput = Plot("Raw", "Time (s)", "Decibels (dB)")
        self.plotOutput = Plot("Smoothed", "Time (s)", "Decibels (dB)")

        self.canvasInput = FigCanvasTk(self.plotInput.fig, master = self.mainwindow)
        self.canvasInput.get_tk_widget().place(x=0, y=0, width=1000, height=580)

        self.canvasOutput = FigCanvasTk(self.plotOutput.fig, master = self.mainwindow)
        self.canvasOutput.get_tk_widget().place(x=930, y=0, width=1000, height=580)

        #Inputs
        self.eta_gui = StringVar(self.mainwindow, 0)
        self.a_gui = StringVar(self.mainwindow, 0)
        self.x_gui = StringVar(self.mainwindow, 0)
        self.noise_gui = StringVar(self.mainwindow, 0)

        ##TextEntrys
        self.NumX_label = Label(self.mainwindow, text = "Num. of Samples: ", bg='#242526', fg= "white", font = Font_tuple)
        self.NumX_label.place(x=1050, y=600)

        self.NumX_entry = Entry(self.mainwindow, textvariable=self.x_gui, bg='#ABABAB', font = Font_tuple)
        self.NumX_entry.place(x=1050, y=645)

        self.Eta_label = Label(self.mainwindow, text = "η (Eta): ", bg='#242526', fg= "white", font = Font_tuple)
        self.Eta_label.place(x=1050, y=700)

        self.Eta_entry = Entry(self.mainwindow, textvariable=self.eta_gui, bg='#ABABAB', font = Font_tuple)
        self.Eta_entry.place(x=1050, y=745)

        self.a_label = Label(self.mainwindow, text = "A: ", bg='#242526', fg= "white", font = Font_tuple)
        self.a_label.place(x=1050, y=800)

        self.a_entry = Entry(self.mainwindow, textvariable=self.a_gui, bg='#ABABAB', font = Font_tuple)
        self.a_entry.place(x=1050, y=845)

        ##Buttons
        self.file_button = Button(self.mainwindow, text="Select File", bg='#ABABAB', command=self.drawInputs, font = Font_tuple)
        self.file_button.place(x=1500, y=600)

        self.start_button = Button(self.mainwindow, text="Start", bg='#ABABAB', command=lambda:threading.Thread(target=self.processing).start(), state=DISABLED, font = Font_tuple)
        self.start_button.place(x=1500, y=700)

        self.exit_button = Button(self.mainwindow, text="X", bg='#AC2F40', command=self.exit, font = Font_tuple)
        self.exit_button.place(x=1880, y=0)

        ##Add Noise Section
        self.noise_label = Label(self.mainwindow, text = "Add Noise: ", bg='#242526', fg= "white", font = Font_tuple)
        self.noise_label.place(x=350, y=600)

        self.noise_entry = Entry(self.mainwindow, textvariable=self.noise_gui, bg='#ABABAB', font = Font_tuple)
        self.noise_entry.place(x=350, y=650)

        self.noise_button = Button(self.mainwindow, text="Add", bg='#ABABAB', command=self.addNoise, state=DISABLED, font = Font_tuple)
        self.noise_button.place(x=350, y=700)

        self.mainwindow.mainloop()

    def drawInputs(self):
        YfromInput = getX()
        if self.plotInput.loadInputs(YfromInput):
            self.start_button["state"] = NORMAL
            self.noise_button["state"] = NORMAL
        else:
            self.start_button["state"] = DISABLED
            self.noise_button["state"] = DISABLED
        self.plotOutput.cleanPoints()
        self.canvasInput.draw()
        self.canvasOutput.draw()

    def addNoise(self):
        self.plotInput.addNoise(float(self.noise_gui.get()))
        self.canvasInput.draw()

    def processing(self):
        eta = float(self.eta_gui.get())
        a = float(self.a_gui.get())
        numX = int(self.x_gui.get())

        YfromInput = self.plotInput.Y
        neuron = Adaline(numX, a, eta)

        YfromOutput = []
        for i in range(numX):
            YfromOutput.append(YfromInput[i])
        self.plotOutput.loadInputs(YfromOutput)
        self.canvasOutput.draw()

        #Learning stage
        for i in range(len(YfromInput)):
            pattern = [1]
            if i + numX >= len(YfromInput):
                break
            for j in range(i, i + numX):
                pattern.append(YfromInput[j])
            YfromOutput.append(neuron.learning(pattern,YfromInput[i + numX]))
            self.plotOutput.loadInputs(YfromOutput)
            self.canvasOutput.draw()

    def exit(self):
        self.mainwindow.destroy()
        exit()