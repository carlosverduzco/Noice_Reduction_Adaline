from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg as FigCanvasTk
from tkinter import *
from plot import Plot

class GUI:
    def __init__(self):
        self.mainwindow = Tk()
        self.mainwindow.attributes("-fullscreen", True)
        self.mainwindow.config(bg='#18191A')
        self.mainwindow.wm_title('Adaline - Noice Reduction')

        self.plotInput = Plot("Raw", "Time (s)", "Decibels (dB)")
        self.plotOutput = Plot("Smoothed", "Time (s)", "Decibels (dB)")

        self.canvasInput = FigCanvasTk(self.plotInput.fig, master = self.mainwindow)
        self.canvasInput.get_tk_widget().place(x=0, y=0, width=1000, height=580)

        self.canvasOutput = FigCanvasTk(self.plotOutput.fig, master = self.mainwindow)
        self.canvasOutput.get_tk_widget().place(x=930, y=0, width=1000, height=580)



        self.mainwindow.mainloop()



GUI()