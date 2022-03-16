import matplotlib.pyplot as plt
import numpy as np

class Plot():
    def __init__(self, title, xlabel, ylabel):
        with plt.rc_context({'axes.edgecolor':'black', 'xtick.color':'red', 'ytick.color':'green', 'figure.facecolor':'#242526'}):
            self.fig, self.ax= plt.subplots()

            self.ax.set_title(title, color= 'white', fontweight='bold', fontsize=15)
            self.ax.set_xlabel(xlabel, color= 'red')
            self.ax.set_ylabel(ylabel, color= 'green')


            x = np.arange(0,100,0.1)
            y = np.sin(x/6)

            self.ax.plot(x,y, 'r')
