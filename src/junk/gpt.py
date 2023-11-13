import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        self.ln, = self.ax.plot([], [], 'r-')
        self.x_data = []
        self.y_data = []

    def init(self):
        self.ax.set_xlim(0, 10)
        self.ax.set_ylim(-1, 1)
        self.fig.canvas.draw()
        self.bg = self.fig.canvas.copy_from_bbox(self.fig.bbox)
        self.fig.canvas.blit(self.fig.bbox)

    def update(self, x, y):
        self.x_data.append(x)
        self.y_data.append(y)
        self.ln.set_data(self.x_data, self.y_data)
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw_idle()
        self.fig.canvas.flush_events()

plot = Plot()
plot.init()

while True:
    plot.update(2, 3)
    plt.pause(0.1)