import time
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import figure, axes
matplotlib.use('TkAgg')
import numpy as np
import math
import logging

logging.basicConfig(level=logging.INFO)



class Plot():
    
    def __init__(self,fig: figure , ax: axes ,grain: int,data_names: list[str] , plot_name: str,colors = None ) -> None:
        self.fig = fig
        self.ax = ax
        self.grain = grain
        
        
        self.plot_names = plot_name
        self.color = "r" * len(data_names) if colors is None else colors
        # makes all red if no color is given
        
        
        self.x_data = range(grain)
        self.y_data = []
        self.lines = []
        
        
        for i in range(len(data_names)):
            self.y_data.append([0] * grain ) 
            ln, = self.ax.plot(self.x_data,self.y_data[i] , animated=False,label=data_names[i], color=colors[i])
            
            self.lines.append(ln)            
        
    
        self.minVal = 0
        self.maxVal = 0 
        
        
        
        self.fig.canvas.draw()
        self.fig.show()
        self.bg = fig.canvas.copy_from_bbox(self.ax.bbox)
        self.fig.canvas.blit(self.ax.bbox)
        self.ax.legend()
        
            
    def restore(self):
        self.fig.canvas.restore_region(self.bg)
    
    def setYData(self,y:list[int,]): # for loop could be made more readable 
        for i,yVal in enumerate(y):
            self.y_data[i].append(yVal) 
            self.y_data[i].pop(0) 
            self.lines[i].set_ydata(self.y_data[i]) # every line has its own yData
        
        
    def draw_artist(self,minVal:int  = None, maxVal: int = None):
        
        curr_max = max([max(y) for y in self.y_data ])
        curr_min = min([min(y) for y in self.y_data ])

        
        
        if maxVal is None:
            if self.maxVal <= curr_max:
                self.maxVal = curr_max    
            else:
                self.maxVal *= .95
                        
        if minVal is None:
            if self.minVal >= curr_min:
                self.minVal = curr_min  
            else:
                self.minVal *= .95
            
        for line in self.lines:
            self.ax.draw_artist(line)
            
        self.ax.axis([0,self.grain,self.minVal,self.maxVal])
            
        self.ax.set_title(self.plot_names)
        self.ax.legend()    
        
        
    def blit(self):
        self.fig.canvas.blit(self.fig.bbox)
        
    def updateBg(self):
        self.bg = self.fig.canvas.copy_from_bbox(self.ax.bbox)