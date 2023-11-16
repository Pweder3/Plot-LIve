import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from LiveGraph import LiveGraph


import math


    



def sinGraph():
    LG = LiveGraph(([50,['a','b'],'fig1',["r","b"]],[50,['c','d'],'fig2',["r","b"]]),True)
    for j in range(100):
        LG.update([[1,math.sin(j/10)],
                   [math.cos(j/100),math.sin(j/100)]],False)
        
def sinOverXGraph():
    LG = LiveGraph(([50,['b'],'fig1',["b"]],))
    for j in range(500):
        LG.update([[math.sin(j/10)/(j/10+1)],])
        
sinOverXGraph()
            
            
