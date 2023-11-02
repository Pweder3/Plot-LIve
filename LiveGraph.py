from matplotlib import pyplot as plt
import math
import numpy as np
from plot import plot

class LiveGraph():
    
    
    def __init__(self,plotNum,names) -> None:
        
        fig,ax = plt.subplots(plotNum)

        self.plots = []
        for i in range(plotNum):
            
            self.plots.append(plot( fig,ax[i] ,5,names[i],"r")  )
        
        self.tick = 0
        
        plt.show(block=False)
        plt.pause(0.1)  
        
        
    def update(self):
        
        self.tick += 1
        for plot in self.plots:
            plot.update(self.tick,self.tick/100)
        
            
        
if __name__ == "__main__":
    LG = LiveGraph(1,["test1"])

    while True:
        LG.update()
    
    