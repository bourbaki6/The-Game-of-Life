#---viz---#


import matplotlib.pyplot as plt

from core.grid import Grid

class Renderer:
    
    def __init__(self, grid: Grid):
        self.fig, self.ax = plt.subplots()
        self.im = self.ax.imshow(grid.data, cmap = 'binary')
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        pass

    def draw(self, grid:Grid):
        self.im.set_data(grid.data)
        self.fig.canvas.draw()
        self.fig.canvas.flush_events()
        plt.pause(0.05)