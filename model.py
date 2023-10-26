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

        V[xi][yi] = Vertex(Gamma)

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

  def percolation_config(self, p):
    V = self.V
    x = self.x
    y = self.y

    for xi in range(x):
      for yi in range(y):
        omega = random.choices([1, 0], [p, 1-p], k=1)[0] # Offen / geschlossen

        V[xi][yi].set_omega(omega)

class Vertex:
  Gamma = (None, None)
  omega = 0
  neighbours = [None, None, None, None]
  walkers = None

  def __init__(self, Gamma):
    self.Gamma = Gamma

  def set_neighbours(self, neighbours):
    self.neighbours = neighbours

  def set_omega(self, omega):
    self.omega = omega
class Walkermanager:
  walkers = None
  t = 0 # Derzeitiger Schritt
  t_max = 0
  lattice = None

  def __init__(self, n_walkers, t_max, lattice):
    walkers = [Walker()] * n_walkers
    
    self.walkers = walkers
    self.t_max = t_max
    self.lattice = lattice
  
  def run_random_walk(self):
    print()
class Walker:
  vertex = None
  pos_at_t = []

  def __init__(self):


class Visualization:

class Simulation:
  lattice = None
  manager = None
  x = 0
  y = 0
  n_walkers = 0
  n_steps = 0
  n_sims = 0
  Temp = 293
  ptunneling = 0

  def __init__(self, x, y, n_walkers, n_steps, n_sims, Temp, ptunneling):
    self.lattice = Lattice(x, y)
    self.manager = Walkermanager(n_walkers, n_steps, self.lattice)
    self.x = x
    self.y = y
    self.n_walkers = n_walkers
    self.n_steps = n_steps
    self.n_sims = n_sims
    self.Temp = Temp
    self.ptunneling = ptunneling
  
  def run_simulation(self):
    lattice = self.lattice
    manager = self.manager
    n_walkers = self.n_walkers
    n_steps = self.n_steps
    n_sims = self.n_sims
    Temp = self.Temp
    ptunneling = self.ptunneling

    for sim in range(n_sims):
      pvalues = np.linalg(0, 1, 20)

      for p in pvalues:
        lattice.percolation_config(p)
        manager.run_random_walk()

  def calc_sigma():
  
  def calc_D():