import numpy as np
import random

class Lattice:
  # Konstruktor
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.V = np.empty((x, y), dtype=object)

    # Array füllen
    for xi in range(x):
      for yi in range(y):
        Gamma = (xi, yi) # Position

        self.V[xi][yi] = Vertex(Gamma)

    # Nachbarn definieren
    for xi in range(x):
      for yi in range(y):
        north = self.V[xi][yi+1] if yi < y else None
        east = self.V[xi+1][yi] if xi < x else None
        south = self.V[xi][y-1] if yi > 0 else None
        west = self.V[xi-1][y] if xi > 0 else None

        neighbours = [north, east, south, west]

        self.V[xi][yi].set_neighbours(neighbours)

  def percolation_config(self, p):
    for xi in range(self.x):
      for yi in range(self.y):
        omega = random.choices([1, 0], [p, 1-p], k=1)[0] # Offen / geschlossen

        self.V[xi][yi].set_omega(omega)
    
  def get_size(self):
    return (self.x, self.y)
  
  def get_V(self):
    return self.V

class Vertex:
  def __init__(self, Gamma):
    self.Gamma = Gamma
    self.omega = 0
    self.neighbours = [None, None, None]
    self.num_walkers = 0

  def set_neighbours(self, neighbours):
    self.neighbours = neighbours

  def set_omega(self, omega):
    self.omega = omega

  def set_walker(self, walker):
    self.num_walkers += 1

class Walkermanager:
  def __init__(self, n_walkers, t_max, lattice):
    self.t = 0 # Derzeitiger Schritt
    self.walkers = [Walker(t_max)] * n_walkers
    self.t_max = t_max
    self.lattice = lattice
  
  def run_random_walk(self):
    self.initialize_walk()
    self.update_walkers(self.t)

    for self.t in range(self.t_max):
      self.step()
      self.update(self.t)

  def initialize_walk(self):
    x, y = self.lattice.get_size()
    self.heatmap = np.zeros((x, y))

    for walker in self.walkers:
      self.assign_walker(walker)
  
  def step(self):
    random.shuffle(self.walkers)
    for walker in self.walkers:
      walker.move()

  def update(self, t):
    for walker in self.walkers:
      walker.add_pos_at_t(t)

  def assign_walker(self, walker):
    x_size, y_size = self.lattice.get_size()
    assigned = False

    while not assigned:
      xrand = random.randint(0, x_size - 1)
      yrand = random.randint(0, y_size - 1)
      vertex = self.lattice.get_V()[xrand][yrand]

      if vertex.num_walkers < 4:
        vertex.walkers.append(walker)
        walker.vertex = vertex
        self.heatmap[xrand][yrand] += 1
        assigned = True

class Walker:
  def __init__(self, t_max):
    self.vertex = None
    self.pos_at_t = [None] * t_max

  def add_pos_at_t(self, t):
    self.pos_at_t[t] = self.vertex.Gamma

class Visualization:
  print()

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
    print()
  
  def calc_D():
    print()