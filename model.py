import numpy as np
import random

class Lattice:
  V = None
  x = 0
  y = 0

  # Konstruktor
  def __init__(self, x, y, p):
    V = np.empty((x, y), dtype=object)

    # Array füllen
    for xi in range(x):
      for yi in range(y):
        Gamma = (xi, yi) # Position
        omega = random.choices([1, 0], [p, 1-p], k=1)[0] # Offen / geschlossen

        V[xi][yi] = Vertex(Gamma, omega)

    # Nachbarn definieren
    for xi in range(x):
      for yi in range(y):
        north = V[xi][yi+1] if yi < y else None
        east = V[xi+1][yi] if xi < x else None
        south = V[xi][y-1] if yi > 0 else None
        west = V[xi-1][y] if xi > 0 else None

        neighbours = [north, east, south, west]

        V[xi][yi].set_neighbours(neighbours)

    self.V = V
    self.x = x
    self.y = y

class Vertex:
  Gamma = (None, None)
  omega = 0
  neighbours = [None, None, None, None]
  walkers = None

  def __init__(self, Gamma, omega):
    self.Gamma = Gamma
    self.omega = omega

  def set_neighbours(self, neighbours):
    self.neighbours = neighbours

class Walkermanager:
  walkers = None
  t = 0 # Derzeitiger Schritt
  t_max = 0

  def __init__(self, n_walkers, t_max):
    walkers = [Walker()] * n_walkers
    
    self.walkers = walkers
    self.t_max = t_max

class Walker:
  vertex = None
  pos_at_t = []

  def __init__(self):


class Visualization:

class Simulation:
  lattice = None
  manager = None

  def __init__(self, p, x, y, n_walkers, n_steps, n_sims, Temp, ptunneling):
    self.lattice = Lattice(x, y, p)
    manager = Walkermanager(n_walkers, n_steps)