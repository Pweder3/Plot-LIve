# Plot-LIve
A simple Graphing utility to display data in real time which also dynamicaly allows you to add graphs while still perfoming well.


# Installation 

To install this package you simply download both files in the [src](https://github.com/Pweder69/Plot-LIve/tree/a57e47303f3a326acfb23c3ee2b4b03e265ad297/src) folder put them in the root of your project and thn import live graph with:

```python
from LiveGraph import LiveGraph
```


# Documentation
The usage is split into 2 parts as the the library only has 2 real operations. 
    
1. [Creating a graph](#creating-a-graph)
2. [Adding data to a graph](#adding-data-to-a-graph)



## Creating a graph
To create the graph you simply call the constructor of the LiveGraph class with the following parameters:

* **plotData** `tuple(list[],)` - This is a tuple containing 1 or several lists of properties to be passed to each in individual graph to be created each new list represents a new graph to be displayed on the plot.
- InteractiveMode `bool` - This is a bool that determines if the graph is interactive or not. its a backround feature to matplotlib and should only be turned off for better performance.