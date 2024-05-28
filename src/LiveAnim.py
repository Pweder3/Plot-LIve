from dataclasses import dataclass
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

import numpy as np
import math
import multiprocessing as mp
import time
import  random

class LiveAnim:
    
    
    def __init__(self,plot_number) -> None:
        self.data_queue = mp.Queue()
        self.main_process = mp.Process(target=self._innit_process,args=(plot_number,self.data_queue),daemon=True)
        self.main_process.start()
        self._plotData = [[[],[]]*plot_number]
    
    
    
    def _innit_process(self,plot_number,dataQueue):
        if plot_number >1:
            _colls = math.ceil(math.sqrt(plot_number))
            _rows = math.ceil(plot_number / _colls)
            # algo to get the best possible plot grid
            fig, [*_ax] = plt.subplots(_rows, _colls)
            for i in range((_rows * _colls) - plot_number):
                fig.delaxes(_ax[-1][-i -1]) 
            fig.tight_layout()
            for axes in _ax:
                axes.plot([], [])
        else:
            fig, _ax = plt.subplots(1, 1)


        def animate(i):
            # print("animating")
            data = dataQueue.get()
            if plot_number >1:
                for i,axes in enumerate(_ax):
                    axes.clear()
                    fig.clear()
                    axes.set_data(data[i][0],data[i][1])
            else:
                _ax.clear()
                _ax.plot(data[0][0],data[0][1])
                
            return _ax.lines
            
        anim = FuncAnimation(fig, animate, interval=1/100,save_count= 10,blit = True)
        plt.show()
        
    def __exit__(self):
        print("Exiting")
        self.main_process.join()
            
    def update(self, *args):
        
        for i,data_t in enumerate(args):
            self._plotData[i][0].append(data_t[0])
            self._plotData[i][1].append(data_t[1])
        print(len(self._plotData[0][0]))
        self.data_queue.put(tuple(self._plotData)) # hopfully makes this picklable
    
    
    
if __name__ == "__main__":
    graph =LiveAnim(1)
    while True:
        time.sleep(.1)
        graph.update([time.time(),random.randrange(0,100)])