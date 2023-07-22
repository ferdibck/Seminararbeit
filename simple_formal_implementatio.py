import random as rd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class Grid:
    grid = None
    probablities = [None, None]

    def __init__(self, xmax, ymax, p):
        
        grid = np.empty([ymax, xmax])
        probabilites = [p, 1-p]

        for y in range(ymax):
            for x in range(xmax):
                grid[y][x] = rd.choices([1,0],probabilites, k = 1)[0]

        self.grid = grid
        self.probablities = probabilites

    def plot(self):
        grid = self.grid

        binary_cmap = ListedColormap(["white", "red"])
        plt.imshow(grid, cmap = binary_cmap, origin = "lower")

        cbar = plt.colorbar(ticks=[0, 1])
        cbar.ax.set_yticklabels(["Geschlossen", "Offen"])

        plt.show()

g = Grid(5,5,0.1)

g.plot()