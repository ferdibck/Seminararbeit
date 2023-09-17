import numpy as np
import random
import matplotlib.pyplot as plt

class vertex:
  omega = None
  Gamma = [None, None]
  neighbours = [None, None, None, None] # N O S W

  def __init__(self):
    return

  def set_properties(self, o, g, n):
    self.omega = o
    self.Gamma = g
    self.neighbours = n

  def get_omega(self):
    return self.omega
  
  def get_Gamma(self):
    return self.Gamma

class lattice:
  V = None
  probabilites = []
  n = 0

  def __init__(self, x, y, p):
    probabilities = [p, 1-p]
    self.probabilites = probabilities
    self.n = x*y

    V = np.full((x, y), vertex())

    for xi in range(0, x):
      for yi in range(0, y):
        omega = random.choices([1,0], probabilities)[0]
        Gamma = [xi+1, yi+1]

        match (xi, yi): # Korrekte Nachbarkonfiguration
          case (1,1): # links-unten
            neighbours = [V[xi][yi+1], V[xi+1][yi], None, None]
          
          case (1, y): # links-oben
            neighbours = [None, V[xi+1][yi], V[xi][yi-1], None]

          case (x, 1): # rechts-unten
            neighbours = [V[xi][yi+1], None, None, V[xi-1][yi]]

          case (x, y): # rechts-oben
            neighbours = [None, None, V[xi][yi-1], V[xi-1][yi]]

          case (1, Any): # linker Rand
            neighbours = [V[xi][yi+1], V[xi+1][yi], V[xi][yi-1], None]

          case (Any, 1): # unterer Rand
            neighbours = [V[xi][yi+1], V[xi+1][yi], None, V[xi-1][yi]]

          case (x, Any): # rechter Rand
            neighbours = [V[xi][yi+1], None, V[xi][yi-1], V[xi-1][yi]]

          case (Any, y): # oberer Rand
            neighbours = [None, V[xi+1][yi], V[xi][yi-1], V[xi-1][yi]]

          case _:
            neighbours = [V[xi][yi+1], V[xi+1][yi], V[xi][yi-1], V[xi-1][yi]]

        V[xi][yi].set_properties(omega, Gamma, neighbours)

    self.V = V

  def visual(self):
    V = self.V

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    for xi in range(len(V)):
      for yi in range(len(V[0])):
        if V[xi][yi].get_omega() == 1:
          ax.plot(xi+1, yi+1, "o", markersize=5, color="red")
        else:
          ax.plot(xi+1, yi+1, "o", markersize=5, color="black")

    plt.xticks(range(1, len(V[0]) + 1), fontsize=24)
    plt.yticks(range(1, len(V) + 1), fontsize=24)
    plt.grid(True)
    plt.show()

l = lattice(5, 5, 0.5)
l.visual()