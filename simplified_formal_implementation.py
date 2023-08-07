import random as rd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import numpy as np
import sys

sys.setrecursionlimit(1000000)

class Vertex:
    state = None
    pos = (None, None)
    neighbours = (None, None, None, None)

    def __init__(self, state, pos):
        self.state = state
        self.pos = pos

    def set_neighbours(self, n):
        self.neighbours = n

    def ret_neighbours(self):
        return self.neighbours

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
                vertex = grid[y][x]
                neighbours = []

                if x < xmax - 1:
                    neighbours.append(grid[y][x+1])

                if y < ymax - 1:
                    neighbours.append(grid[y+1][x])

                if y > 0:
                    neighbours.append(grid[y-1][x])
                

                if x > 0:
                    neighbours.append(grid[y][x-1])

                

                vertex.set_neighbours(neighbours)

        self.grid = grid
        self.probablities = probabilities

    def search(self):
        grid = self.grid
        xmax = self.xmax
        ymax = self.ymax

        S = np.empty([ymax],dtype=object)
        Z = np.empty([ymax],dtype=object)

        for y in range(ymax):
            S[y] = grid[y][0]
            Z[y] = grid[y][xmax-1]

        Clusters = []
        visited = set()

        def dfs(vertex, cluster):
            visited.add(vertex)
            
            neighbours = vertex.ret_neighbours()

            for n in neighbours:
                if n not in visited and n.ω() == 1:
                    dfs(n, cluster)

            cluster.append(vertex)

            for c in cluster:
                for z in Z:
                    if c == z:
                        return True

        for vertex in grid[0]:
            if vertex not in visited:
                cluster = []
                dfs(vertex, cluster)
                Clusters.append(cluster)

        # print(Clusters)

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

g = Grid(100,100,0.6)

g.plot()

g.search()