import numpy as np
import random

class Lattice:
  V = None
  x = 0
  y = 0

  # Konstruktor
  def __init__(self, x, y):
    V = np.empty((x, y), dtype=object)

    for xi in range(x):
      for yi in range(y):
        V[xi][yi] = Datanode()

    for xi in range(x):
      for yi in range(y):
        neighbours = [None, None, None, None]
        

    self.V = V
    self.x = x
    self.y = y

class Datanode:

class Vertex:

class Walkermanager:

class Walker:

class Visualization:

class Calculation:

class Simulation: