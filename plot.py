import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np
import math
class Plot():
    
    def __init__(self,fig,ax,grain,dataAmount,dataNames,names,colors = None ) -> None:
        
        

        self.fig = fig
        self.ax = ax
        self.names = names
        self.color = "r" * dataAmount if colors == None else colors
        
        self.xData = range(grain)
        
        self.Ydata = []
        self.Lines = []
        
        for i in range(dataAmount):
            self.Ydata.append([0] * grain ) 
            
            self.ln, = self.ax.plot(self.xData,self.Ydata[i] , animated=True,label=dataNames[i], color=self.color[i])
            self.Lines.append(self.ln)            
        
    
        
      
        plt.pause(0.00001)
        
        self.bg = fig.canvas.copy_from_bbox(fig.bbox)
        self.fig.canvas.blit(self.fig.bbox)
        self.ax.legend()
        
            
    def restore(self):
        self.fig.canvas.restore_region(self.bg)
    
    def setYData(self,y):
        for i,yVal in enumerate(y):
            self.yData[i].append(yVal) if yVal != None else self.yData[i]
            self.yData[i].pop(0) if yVal != None else None
            self.ln.set_ydata(self.yData)
        
        
    def draw_artist(self):
        self.ax.relim()
        self.ax.autoscale_view()
        for line in self.Lines:
            self.ax.draw_artist(line)
        self.ax.set_title(self.names)
        self.ax.legend()
        
    def blitAndFlush(self):
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()
    