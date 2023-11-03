import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np


class Plot():
    
    def __init__(self,fig,ax,grain,dataAmount,names,colors) -> None:
        
        
        self.fig = fig
        self.ax = ax
        
        self.xData = range(grain)
        self.yData = [0] * grain 
        
        self.name = names
        self.color = colors
        
        self.ln, = self.ax.plot(self.xData, self.yData, animated=True,label=self.name)
        
        
        
        
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.origBB = self.fig.bbox
        self.fig.canvas.blit(self.fig.bbox)
        self.ax.legend()
        
    def update(self,ticks,y):
        
        
        self.fig.canvas.restore_region(self.bg)
        self.fig.canvas.draw()
        self.fig.clear()
        

        self.yData.append(y)
        self.yData.pop(0)
        
        self.ln.set_ydata(self.yData)
        
        self.ax.relim()
        self.ax.autoscale_view()
        self.ax.add_artist(self.ln)
        # self.ax.draw_artist(self.ln)
        self.ax.set_title(self.name)
        self.ax.legend()
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()
        
        

        