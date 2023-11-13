import time
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from src.plot import Plot
import logging
logging.basicConfig(level=logging.INFO)

class LiveGraph():
    
    
    def __init__(self,plotdata,inteactiveMode = False) -> None:
        
        
        # plotData = [grain,dataAmount,dataNames,overAllName,colors]
        
        self.fig = plt.figure(figsize=(10,10))
        
        self.plots = []
        for i in range(len(plotdata)):
            self.plots.append(Plot(
                                   self.fig,
                                   self.fig.add_subplot(len(plotdata),1,i+1),
                                   plotdata[i][0],
                                   plotdata[i][1],
                                   plotdata[i][2],
                                   plotdata[i][3],
                                   plotdata[i][4] if len(plotdata[i]) > 4 else None
                                   ))
        

        
        self.tick = 0
        plt.show(block = False)
        plt.pause(0.1)  
        if inteactiveMode: 
            plt.ion() 
        else:
            pass
            # self.fig.canvas.mpl_connect('draw_event', self.updateOnWindowChange)
            # TODO: Allow for non interactive mode with window change detection and then updating after change 
        
        
    def update(self,y = None ,drawInSequence = True):
        
        
        
        
        self.tick += 1
        if drawInSequence:
            [plot.restore() for plot in self.plots]
            [plot.setYData(y[i]) for i, plot in enumerate(self.plots)] if y is not None else None
            [plot.draw_artist() for plot in self.plots]
            [plot.blit() for plot in self.plots]
        else:
            for i,plot in enumerate(self.plots):
                plot.restore()
                plot.setYData(y[i]) if y is not None else None
                plot.draw_artist()
                plot.blit()
        self.fig.canvas.flush_events()
        
    def updateOnWindowChange(self,event):
        
        for plot in self.plots:
            if event is not None:
                if event.canvas != self.fig.canvas:
                    raise RuntimeError
            plot.updateBg()
        self.update()
    
            
        
            
        
if __name__ == "__main__":
    LG = LiveGraph(([200,2,['a','b'],'fig1',["r","b"]],[200,2,['c','d'],'fig2',["r","b"]]),True)
    

    for j in range(1000):
        LG.update([[1,math.sin(j/10)],
                   [math.cos(j/100),math.sin(j/100)]],False)
        

            
        
    
    