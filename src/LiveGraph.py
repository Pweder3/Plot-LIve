import time
from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from plot import Plot
import logging
logging.basicConfig(level=logging.INFO)

class LiveGraph():
    
    
    def __init__(self,*args,inteactiveMode = True,plot_size = (10,10) ) -> None:
        
        
        # TODO: type cast correctly and docstrings
        
        # plotData = [grain,dataNames,overAllName,colors]
        
        self.fig = plt.figure(figsize=plot_size)
        
        
        self.plots = []
        for i,data in enumerate(args):
            
            self.plots.append(Plot(
                                   self.fig,
                                   self.fig.add_subplot(len(args),1,i+1),
                                   data[0],
                                   data[1],
                                   data[2],
                                   data[3] if len(data) > 3 else None
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
        
        
    def update(self,*args,drawInSequence: bool = True) -> None :
        if len(args) < len(self.plots) :
            raise ValueError("No data to plot")
        
        self.tick += 1
        if drawInSequence:
            [plot.restore() for plot in self.plots]
            [plot.setYData(args[i]) for i, plot in enumerate(self.plots)] 
            [plot.draw_artist() for plot in self.plots]
            [plot.blit() for plot in self.plots]
            
        else:
            for i,plot in enumerate(self.plots):
                plot.restore()
                plot.setYData(args[i])
                plot.draw_artist()
                plot.blit()
        self.fig.canvas.flush_events()
        
    def updateOnWindowChange(self,event):
        raise NotImplementedError
        
        for plot in self.plots:
            if event is not None:
                if event.canvas != self.fig.canvas:
                    raise RuntimeError
            plot.updateBg()
        self.update()
    
            
        
            

if __name__ == "__main__":
    LG = LiveGraph([200,['a','b'],'fig1',["r","b"]],
                   [50,['a','b'],'fig2',["r","b"]]
                   )
    cycleCount = 0
    start_time = time.time()
    
    for j in range(1000):
        LG.update([1,math.sin(j/100)],
                  [math.sin(j/100),1]
                  )
        cycleCount += 1
        print(cycleCount/(time.time()-start_time))
        

            
        
    
    