from matplotlib import pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import math
import numpy as np
from plot import Plot

class LiveGraph():
    
    
    def __init__(self,plotNum,names) -> None:
        
        fig,ax = plt.subplots(plotNum)

        self.plots = []
        if type(ax) == np.ndarray:
            for i in range(plotNum):
                self.plots.append(Plot( fig,ax[i] ,100,5,names[i],"r"))
        else:
            self.plots.append(Plot( fig,ax ,100,5,names,"r"))
        
        self.tick = 0
        
        plt.show(block=False)
        plt.pause(0.1)  
        
        
    def update(self):
        
        self.tick += 1
        for plot in self.plots:
            plot.update(self.tick,math.sin(self.tick/10))
        
            
        
if __name__ == "__main__":
    LG = LiveGraph(2,["test1","test 2"])

    while True:
        LG.update()
    
    