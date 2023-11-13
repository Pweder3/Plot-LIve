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

* **plotData** ```tuple(list[int,int,list[str,],str,list[str],],list[...],...)``` 
    - This is a tuple containing 1 or several lists of properties to be passed to each in individual graph to be created each new list represents a new graph to be displayed on the plot. Importantly the contents of each list is structured as such:
    - **[0]** ```int``` 
        - This is the number of data points to be displayed on the graph at any given time. This is used to determine the x axis range of the graph its called the **"grain"** of the graph.
    - **[1]** ```int```
        - This is the number of lines in that graph to be displayed at any given time each line will have `n` points `n` being the grain of the graph.
    - **[2]** ```list[str,]```
        - This is a list of the names of the lines to be displayed on the graph. The length of this list must be equal to the number of lines in the graph.
    - **[3]** ```str```
        - This is the name of the graph to be displayed on the plot.
    - **[4]** ```list[str,]```
        - This is a list of the colors of the lines to be displayed on the graph. The length of this list must be equal to the number of lines in the graph when inputed its an optional paramater and the default will set all lines to red and the colors must be valid matplotlib colors. 

- **InteractiveMode** `bool` 
    - This is a bool that determines if the graph is interactive or not. its a backround feature to matplotlib and should only be turned off for better performance. (defaults to true)

### Example 
```python
from LiveGraph import LiveGraph

LG = LiveGraph(
    plotData=(
        (100, 2, ["line1", "line2"], "graph1", ["r", "b"]),
        # A graph with the name graph1 and two lines one red and one blue with 
        # the names line 1 and line 2

        (100, 1, ["line1"], "graph2", ["g"]) 
        # A graph with the name graph2 and one green line with the name line 1
    ),
    InteractiveMode=True # this is optional and defaults to True
)

```

