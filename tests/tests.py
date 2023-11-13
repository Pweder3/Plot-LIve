import unittest
from src.LiveGraph import LiveGraph
import math


class testGraph(unittest.TestCase):
    
    def test_graph(self):
        LG = LiveGraph(([200,2,['a','b'],'fig1',["r","b"]],[200,2,['c','d'],'fig2',["r","b"]]),True)
    
        for j in range(100):
            LG.update([[1,math.sin(j/10)],
                       [math.cos(j/100),math.sin(j/100)]],False)
            
            
if __name__ == '__main__':
    unittest.main()