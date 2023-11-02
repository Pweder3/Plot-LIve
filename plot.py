import time
import matplotlib.pyplot as plt
import numpy as np


class plot():
    
    def __init__(self,fig,ax,grain,name,color) -> None:
        
        
        self.fig,self.ax = fig,ax
        
        self.xData = range(grain)
        self.yData = [0] * grain 
        
        self.name = name
        self.color = color
        
        self.ln, = self.ax.plot(self.xData, self.yData, animated=True,label=self.name)
        
        
        
        
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.fig.canvas.blit(self.fig.bbox)
        
    def update(self,ticks,y):
        
        
        self.fig.canvas.restore_region(self.bg)
        

        self.yData.append(y)
        self.yData.pop(0)
        
        self.ln.set_ydata(self.yData)
        
        
        self.ax.relim()
        self.ax.autoscale_view()
        time.sleep(.1)
        self.fig.draw_artist(self.ln)
        
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()
        