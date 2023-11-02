from matplotlib import pyplot as plt
import math
import numpy as np
from plot import plot

class LiveGraph():
    
    
    def __init__(self,plotNum,names) -> None:
        
        fig,ax = plt.subplots(plotNum)

        self.plots = []
        for i in range(plotNum):
            
            self.plots.append(plot( fig,ax[i] ,names[i],"r")  )
        
        self.tick = 0
        
        plt.show(block=False)
        plt.pause(0.1)  
        
        
    def update(self):
        
        self.tick += 1
        for plot in self.plots:
            plot.update(self.tick,self.tick/100)
        
            
        
        
LG = LiveGraph(2,["test1","test2"])

while True:
    LG.update()
    
    