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
    edges = []
    neighbors = self.neighbours
    if len(neighbors) != 0:
      possible_edges = [n for n in neighbors if n is not None]
      edges = [n for n in possible_edges if n.get_omega() == 1 or n.get_omega() == 0]
    return edges
  
  def set_omega(self, o):
    self.omega = o
  
class lattice:
  V = None

  def __init__(self, x, y):
    V = np.empty((x, y), dtype=object)

    for xi in range(0, x):
      for yi in range(0, y):
        V[xi][yi] = vertex()

    for xi in range(0, x):
      for yi in range(0, y):
        omega = random.choices([1, 2, 0], k=1)[0]
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

  def hopping(self):
    return
    

  def visual(self):
    V = self.V

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Knoten
    for xi in range(len(V)):
      for yi in range(len(V[0])):

        # Knoten
        if V[xi][yi].get_omega() == 1:
          ax.plot(xi, yi, "o", markersize=20, color="black", fillstyle = "left")
        elif V[xi][yi].get_omega() == 2:
          ax.plot(xi, yi, "o", markersize=20, color = "black", fillstyle = "full")
        else:
          ax.plot(xi, yi, "o", markersize=20, color="black", fillstyle = "none")

        # Kanten
        """
        if xi > 0 and V[xi][yi].get_omega() == 1 and V[xi-1][yi].get_omega() == 1:
          ax.plot([xi, xi - 1], [yi, yi], color="red")
        if yi > 0 and V[xi][yi].get_omega() == 1 and V[xi][yi-1].get_omega() == 1:
          ax.plot([xi, xi], [yi, yi - 1], color="red")
        """

    plt.xticks(range(0, len(V[0])), fontsize=24)
    plt.yticks(range(0, len(V)), fontsize=24)
    plt.grid(True)
    plt.show()

  def update(self, p):
    V = self.V

    for xi in range(len(V)):
      for yi in range(len(V[0])):
        possible_neighbours = V[xi][yi].get_edges()

        yes_no = random.uniform(0, 1)

        if yes_no < p and len(possible_neighbours) != 0:
          hopped_to = random.choice(possible_neighbours)
          hopped_to.set_omega(hopped_to.get_omega() + 1)

for n in range(10):
  l = lattice(5, 5)
  l.visual()
  l.update(0.5)