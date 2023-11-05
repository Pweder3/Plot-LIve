
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import time
import math

class  test():
    
    def  __init__(self,fig,ax) -> None:
        
        
        
        self.fig = fig
        self.ax = ax

        (self.ln,) = self.ax.plot([0,1.5,2], [0,1,3], animated=True)

        plt.show(block=False)

      
        plt.pause(0.1)

        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.ax.draw_artist(self.ln)
        self.fig.canvas.blit(self.fig.bbox)

        self.ydata = [0] *100

    def update(self,j):
       
        self.fig.canvas.restore_region(self.bg)
        self.ydata.append(math.sin(j/10))
        self.ydata.pop(0)    
        self.ln.set_ydata(self.ydata)
        self.ln.set_xdata(range(len(self.ydata)))
        self.ax.relim()
        self.ax.autoscale_view()
        time.sleep(.01)
        self.ax.draw_artist(self.ln)
        self.ax.set_title("test")
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)

NC = test(fig,ax)

for j in range(1000):
    NC.update(j)