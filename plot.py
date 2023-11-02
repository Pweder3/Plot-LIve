import matplotlib.pyplot as plt
import numpy as np


class plot():
    
    def __init__(self,fig,ax,name,color) -> None:
        
        
        self.fig,self.ax = fig,ax
        
        self.xData = range(5)
        self.yData = [0] *5 
        
        self.name = name
        self.color = color
        
        self.ln, = self.ax.plot(self.xData, self.yData, animated=True,label=self.name)
        
        
        
        
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.fig.canvas.blit(self.fig.bbox)
        
    def update(self,ticks,y):
        
        
        
        self.fig.canvas.restore_region(self.bg)

        
        
        # self.ln.set_ydata([0,1.5,2])
        # self.ln.set_xdata([0,3,3])
        

        
        print(self.xData[0],self.yData[0])
        self.yData.append(y)
        self.yData.pop(0)
        
        self.ax.relim()
        self.ax.autoscale_view()
        
        nl = []
        for i in range(len(self.xData)):
            nl.append((self.xData[i],self.yData[i]))
        print(nl)
        
        
        self.ln.set_ydata(self.yData)
        self.fig.clear()
        self.ax.clear()
        self.fig.draw_artist(self.ln)
        
        self.fig.canvas.blit(self.fig.bbox)
        self.fig.canvas.flush_events()
        