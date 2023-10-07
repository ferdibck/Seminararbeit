import numpy as np
import random
import matplotlib.pyplot as plt

class walker:
  vertex = None
  start = (None, None)
  curr = []
  steps = []

  def __init__(self, v):
    v.set_walker = True
    self.start = v.get_Gamma()
    self.curr.append(v.get_Gamma())
    self.vertex = v

  def update(self, v):
    self.vertex.set_walker = False
    v.set_walker = True
    self.curr.append(v.get_Gamma())
    self.vertex = v

  def get_vertex(self):
    return self.vertex

  def append_steps(self, t):
    self.steps.append(t)

  def get_curr(self):
    return self.curr

  def calc_avg_t(self):
    steps = self.steps

    for i in len(steps):
      sum =+ i

    return sum/len(steps)

class vertex:
  omega = None
  Gamma = (None, None)
  neighbours = [None, None, None, None] # N O S W
  walker_y_n = False

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
  
  def get_walker_edges(self):
    edges = []
    neighbors = self.neighbours
    if len(neighbors) != 0:
      possible_edges = [n for n in neighbors if n is not None]
      edges = [n for n in possible_edges if (n.get_omega() == 1 and not n.get_walker())]
    return edges
  
  def set_omega(self, o):
    self.omega = o

  def set_walker(self, v):
    self.walker_y_n = v

  def get_walker(self):
    return self.walker_y_n
  
class lattice:
  V = None

  def __init__(self, x, y, p):
    V = np.empty((x, y), dtype=object)
    probabilities = [p, 1-p]

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

  def random_walk(self, t):
    V = self.V
    walkers = []

    for yi in range(len(V[0])):
      walkers.append(walker(V[0][yi]))

    for ti in range(1, t+1):
      random.shuffle(walkers)
      
      for w in walkers:
        vertex = w.get_vertex()
        neighbours = vertex.get_walker_edges()

        if len(neighbours) != 0:
          new_vertex = random.choice(neighbours)
          w.update(new_vertex)
          w.append_steps(ti)

    return walkers

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

    # Walker
    walkers = self.random_walk(5)

    for w in walkers:
      x_values = []
      y_values = []

      values = w.get_curr()

      for pair in values:
        x, y = pair
        x_values.append(x)
        y_values.append(y)

        ax.plot(x_values, y_values)


    plt.xticks(range(0, len(V[0])), fontsize=24)
    plt.yticks(range(0, len(V)), fontsize=24)
    plt.grid(True)
    plt.show()

L = lattice(5,5, 0.5)

L.visual()