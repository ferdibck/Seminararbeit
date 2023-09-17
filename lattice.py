import numpy as np
import random
import matplotlib.pyplot as plt

class vertex:
  omega = None
  Gamma = [None, None]
  neighbours = [None, None, None, None] # N O S W

  def __init__(self):
    self.omega = None
    self.Gamma = (None, None)
    self.neighbours = [None, None, None, None]

  def set_properties(self, o, g, n):
    self.omega = o
    self.Gamma = g
    self.neighbours = n

  def get_omega(self):
    return self.omega
  
  def get_Gamma(self):
    return self.Gamma
  
  def get_edges(self):
    neighbors = self.neighbours
    edges = [n for n in neighbors if n is not None and n.get_omega() == 1]
    return edges
class lattice:
  V = None

  def __init__(self, x, y, p):
    probabilities = [p, 1-p]

    V = np.empty((x, y), dtype=object)

    for xi in range(0, x):
      for yi in range(0, y):
        V[xi][yi] = vertex()

    for xi in range(0, x):
      for yi in range(0, y):
        omega = random.choices([1, 0], probabilities, k=1)[0]
        Gamma = (xi, yi)

        if xi == 0 and yi == 0:  # links-unten
          neighbours = [V[xi][yi + 1], V[xi + 1][yi], None, None]
        elif xi == 0 and yi == y-1:  # links-oben
          neighbours = [None, V[xi + 1][yi], V[xi][yi - 1], None]
        elif xi == x-1 and yi == 0:  # rechts-unten
          neighbours = [V[xi][yi + 1], None, None, V[xi - 1][yi]]
        elif xi == x-1 and yi == y-1:  # rechts-oben
          neighbours = [None, None, V[xi][yi - 1], V[xi - 1][yi]]
        elif xi == 0:  # linker Rand
          neighbours = [V[xi][yi + 1], V[xi + 1][yi], V[xi][yi - 1], None]
        elif xi == x-1:  # rechter Rand
          neighbours = [V[xi][yi + 1], None, V[xi][yi - 1], V[xi - 1][yi]]
        elif yi == 0:  # unterer Rand
          neighbours = [V[xi][yi + 1], V[xi + 1][yi], None, V[xi - 1][yi]]
        elif yi == y-1:  # oberer Rand
          neighbours = [None, V[xi + 1][yi], V[xi][yi - 1], V[xi - 1][yi]]
        else:
          neighbours = [V[xi][yi + 1], V[xi + 1][yi], V[xi][yi - 1], V[xi - 1][yi]]

        V[xi][yi].set_properties(omega, Gamma, neighbours)

    self.V = V

  def visual(self):
    V = self.V

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Knoten
    for xi in range(len(V)):
      for yi in range(len(V[0])):

        # Knoten
        if V[xi][yi].get_omega() == 1:
          ax.plot(xi, yi, "o", markersize=5, color="red")
        else:
          ax.plot(xi, yi, "o", markersize=5, color="black")

        # Kanten
        if xi > 0 and V[xi][yi].get_omega() == 1 and V[xi-1][yi].get_omega() == 1:
          ax.plot([xi, xi - 1], [yi, yi], color="red")
        if yi > 0 and V[xi][yi].get_omega() == 1 and V[xi][yi-1].get_omega() == 1:
          ax.plot([xi, xi], [yi, yi - 1], color="red")

    plt.xticks(range(0, len(V[0])), fontsize=24)
    plt.yticks(range(0, len(V)), fontsize=24)
    plt.grid(True)
    plt.show()

  def random_walk(self, n):
    V = self.V
    coordinates = [(0, 0)]
    x_values = [0]
    y_values = [0]

    for ni in range(n):
      x, y = coordinates[-1]
      edges = V[x, y].get_edges()
      vertex = random.choice(edges)
      x, y = vertex.get_Gamma()
      coordinates.append((x, y))
      x_values.append(x)
      y_values.append(y)

    x0, y0 = coordinates[0]
    x1, y1 = coordinates[-1]

    dist = np.sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.plot(x_values, y_values, marker='o', markersize=5, color='blue', label='Random Walk')
    ax.plot(x0, y0, marker='o', markersize=5, color='green', label='Start')
    ax.plot(x1, y1, marker='o', markersize=5, color='red', label='End')
    ax.legend()
    plt.xticks(range(0, len(V[0])), fontsize=24)
    plt.yticks(range(0, len(V)), fontsize=24)
    plt.grid(True)
    plt.show()

    return dist

l = lattice(5, 5, 0.7)
l.visual()

print(l.random_walk(100))