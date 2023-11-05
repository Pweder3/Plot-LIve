from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from plot import Plot

class LiveGraph():
    
    
    def __init__(self,plotdata) -> None:
        
        
        # plotData = [grain,dataAmount,dataNames,overAllName]
        
        fig = plt.figure(figsize=(10,10))

        
        self.plots = []
        for i in range(len(plotdata)-1):
            self.plots.append(Plot(
                                   fig,
                                   fig.add_subplot(i,1,i+1),
                                   plotdata[i][0],
                                   plotdata[i][1],
                                   plotdata[i][2],
                                   plotdata[i][3],
                                   ))
        
        
        self.tick = 0
        
        plt.show(block=False)
        plt.pause(0.1)  
        
        
    def update(self,y):
        
        self.tick += 1
        [plot.restore() for plot in self.plots]
        [plot.setYData(y[i]) for i, plot in enumerate(self.plots)]
        [plot.draw_artist() for plot in self.plots]
        [plot.blitAndFlush() for plot in self.plots]
            

            
        
            
        
if __name__ == "__main__":
    LG = LiveGraph([200,2,['a','b'],'fig1'],
                   [200,2,['a','b'],'fig2'])

    for j in range(1000):
        LG.update()
    
    