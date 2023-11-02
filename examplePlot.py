from matplotlib import pyplot as plt
import math
import numpy as np


x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
fig, ax = plt.subplots(figsize=(5, 2.7), layout='constrained')
ax.plot([0,1.5,2], [0,1,3], label='linear')  # Plot some data on the axes.
ax.legend()  # Add a legend.


plt.show()