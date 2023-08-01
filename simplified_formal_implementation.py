import random as rd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np

class Vertex:
    state = None
    pos = (None, None)
    neighbours = (None, None, None, None)

    def __init__(self, state, pos):
        self.state = state
        self.pos = pos

    def set_neighbours(self, n):
        self.neighbours = n

    def ω(self):
        return self.state


class Grid:
    grid = None
    probablities = [None, None]
    xmax = 0
    ymax = 0

    def __init__(self, xmax, ymax, p):
        grid = np.empty([ymax, xmax], dtype=object)
        probabilities = [p, 1-p]
        self.xmax = xmax
        self.ymax = ymax

        for y in range(ymax):
            for x in range(xmax):
                grid[y][x] = Vertex(rd.choices([1,0], probabilities)[0], (x+1, y+1))

        for y in range(ymax):
            for x in range(xmax):
                if x == 0 and y == 0:
                    grid[y][x].set_neighbours((grid[y][x+1], grid[y+1][x], None, None))
                elif x == xmax-1 and y == ymax-1:
                    grid[y][x].set_neighbours((None, None, grid[y-1][x], grid[y][x-1]))
                elif x == 0:
                    grid[y][x].set_neighbours((grid[y][x+1], grid[y+1][x], grid[y-1][x], None))
                elif x == xmax-1:
                    grid[y][x].set_neighbours((None, grid[y+1][x], grid[y-1][x], grid[y][x-1]))
                elif y == 0:
                    grid[y][x].set_neighbours((grid[y][x+1], grid[y+1][x], None, grid[y][x-1]))
                elif y == ymax-1:
                    grid[y][x].set_neighbours((grid[y][x+1], None, grid[y-1][x], grid[y][x-1]))
                else: 
                    grid[y][x].set_neighbours((grid[y][x+1], grid[y+1][x], grid[y][x-1], grid[y-1][x]))

        self.grid = grid
        self.probablities = probabilities

    def plot(self):
        grid = self.grid
        ymax = self.ymax
        xmax = self.xmax

        bin_grid = np.empty([ymax, xmax])

        for y in range(ymax):
            for x in range(xmax):
                bin_grid[y][x] = grid[y][x].ω()

        binary_cmap = ListedColormap(["white", "red"])
        plt.imshow(bin_grid, cmap = binary_cmap, origin = "lower")

        cbar = plt.colorbar(ticks=[0, 1])
        cbar.ax.set_yticklabels(["Geschlossen", "Offen"])

        plt.show()

g = Grid(5,5,0.5)

g.plot()