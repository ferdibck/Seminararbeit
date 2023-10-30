import numpy as np
import random
import pandas as pd
import matplotlib.pyplot as plt

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
        north = None
        east = None
        south = None
        west = None

        if yi < y-1:
          north = self.V[xi][yi+1]
        
        if xi < x-1:
          east = self.V[xi+1][yi]

        if yi > 0:
          south = self.V[xi][yi-1]

        if xi > 0:
          west = self.V[xi-1][yi]

        neighbours = [north, east, south, west]

        self.V[xi][yi].neighbours = neighbours

  def percolation_config(self, p):
    for xi in range(self.x):
      for yi in range(self.y):
        omega = random.choices([1, 0], [p, 1-p], k=1)[0] # Offen / geschlossen

        self.V[xi][yi].omega = omega
    
  def get_size(self):
    return (self.x, self.y)
  
  def get_V(self):
    return self.V

class Vertex:
  def __init__(self, Gamma):
    self.Gamma = Gamma
    self.omega = 0
    self.neighbours = [None, None, None]
    self.walkers = 0

  def get_edges(self):
    edges = [n for n in self.neighbours if (n is not None and n.omega == 1 and self.omega == 1)]
    return edges
  
  def get_dir_edges(self):
    neighbours = self.neighbours[0:3]
    edges = [n for n in neighbours if (n is not None and n.omega == 1 and self.omega == 1)]
    return edges

class Walkermanager:
  def __init__(self, n_walkers, t_max, lattice, p_tunneling):
    self.t = 0 # Derzeitiger Schritt
    self.n_walkers = n_walkers
    self.t_max = t_max
    self.lattice = lattice
    self.p_tunneling = p_tunneling
    self.heatmap = None
  
  def random_walk(self):
    self.t = 0
    self.walkers = [Walker(self.t_max) for _ in range(self.n_walkers)]

    for xi in range(self.lattice.x):
      for yi in range(self.lattice.y):
        self.lattice.V[xi][yi].walkers = 0

    self.initialize_walk()
    self.update(self.t)

    for self.t in range(self.t_max):
      self.step()
      self.update(self.t)

  def initialize_walk(self):
    for walker in self.walkers:
      self.assign_walker(walker)
  
  def step(self):
    random.shuffle(self.walkers)
    for walker in self.walkers:
      walker.move(self.p_tunneling)

  def update(self, t):
    for walker in self.walkers:
      walker.add_pos_at_t(t)

  def assign_walker(self, walker):
    x_size, y_size = self.lattice.get_size()
    assigned = False

    while not assigned:
      xrand = random.randint(0, x_size - 1)
      yrand = random.randint(0, y_size - 1)
      vertex = self.lattice.V[xrand][yrand]

      if vertex.walkers < 4:
        walker.vertex = vertex
        vertex.walkers += 1
        assigned = True
  
  def directed_random_walk(self):
    self.t = 0
    _, y = self.lattice.get_size()

    self.walkers = []

    for xi in range(self.lattice.x):
      for yi in range(self.lattice.y):
        self.lattice.V[xi][yi].walkers = 0

    self.initialize_dir_walk()
    self.update(self.t)

    for self.t in range(self.t_max):
      self.dir_step()
      self.update(self.t)

  def initialize_dir_walk(self):
    x, y = self.lattice.get_size()

    for yi in range(y):
      vertex = self.lattice.V[0][yi]

      for _ in range(4):
        walker = Walker(self.t_max)
        walker.vertex = vertex
        vertex.walkers += 1
        self.walkers.append(walker)

  def dir_step(self):
    random.shuffle(self.walkers)
    for walker in self.walkers:
      walker.dir_move(self.p_tunneling)

class Walker:
  def __init__(self, t_max):
    self.vertex = None
    self.pos_at_t = [None] * t_max

  def add_pos_at_t(self, t):
    self.pos_at_t[t] = self.vertex.Gamma

  def move(self, p_tunneling):
    if self.vertex.omega == 0 and random.random() <= p_tunneling:
      vertices = self.vertex.neighbours
    else:
      vertices = self.vertex.get_edges()

    valid_vertices = [vertex for vertex in vertices if vertex and vertex.walkers < 4]

    if valid_vertices:
      new_vertex = random.choice(valid_vertices)
      self.vertex.walkers -= 1
      self.vertex = new_vertex
      self.vertex.walkers += 1

  def dir_move(self, p_tunneling):
    if self.vertex.omega == 0 and random.random() <= p_tunneling:
      vertices = self.vertex.neighbours[0:3]
    else:
      vertices = self.vertex.get_dir_edges()

    valid_vertices = [vertex for vertex in vertices if vertex and vertex.walkers < 4]

    if valid_vertices:
      new_vertex = random.choice(valid_vertices)
      self.vertex.walkers -= 1
      self.vertex = new_vertex
      self.vertex.walkers += 1

class Simulation:
  q = 1.6 * 10**(-19)
  k_B = 1.38 * 10**(-23)

  NUM_OF_P_VALUES = 20

  def __init__(self, x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling):
    self.lattice = Lattice(x, y)
    self.manager = Walkermanager(num_walkers, num_steps, self.lattice, p_tunneling)
    self.x = x
    self.y = y
    self.num_walkers = num_walkers
    self.num_steps = num_steps
    self.num_sims = num_sims
    self.Temp = Temp
    self.p_tunneling = p_tunneling
  
  def run_simulations(self):
    dfs = []

    for _ in range(self.num_sims):
      dfs.append(self.run_simulation())

    return dfs
  
  def run_dir_simulations(self):
    dfs = []

    for _ in range(self.num_sims):
      dfs.append(self.run_dir_simulation())

    return dfs
  

  def run_simulation(self):
    p_values = np.linspace(0, 1, self.NUM_OF_P_VALUES)
    sigma_values = []

    for p in p_values:
      self.lattice.percolation_config(p)
      self.manager.random_walk()
      sigma = self.calc_sigma() 

      sigma_values.append(sigma)

    data = {"p": p_values, "Sigma (σ)": sigma_values}
    df = pd.DataFrame(data)
    print(df)
    return df
  
  def run_dir_simulation(self):
    p_values = np.linspace(0, 1, self.NUM_OF_P_VALUES)
    sigma_values = []

    for p in p_values:
      self.lattice.percolation_config(p)
      self.manager.directed_random_walk()
      sigma = self.calc_sigma() 

      sigma_values.append(sigma)

    data = {"p": p_values, "Sigma": sigma_values}
    df = pd.DataFrame(data)
    print(df)
    return df

  def calc_avg_dist_squared(self):
    sum_of_dists = 0

    for walker in self.manager.walkers:
      x0, y0 = walker.pos_at_t[0]
      x_tmax, y_tmax = walker.pos_at_t[-1]

      dx = x_tmax - x0
      dy = y_tmax - y0

      dist = dx**2 + dy**2
      sum_of_dists += dist

    avg_dist_squared = sum_of_dists / self.num_walkers

    return avg_dist_squared

  def calc_D(self):
    avg_dist_squared = self.calc_avg_dist_squared()

    D = (avg_dist_squared) / (2 * 2 * self.num_steps)

    return D

  def calc_sigma(self):
    D = self.calc_D()

    n = self.num_walkers / (self. x * self.y)

    sigma = n * (self.q**2) / (self.k_B * self.Temp) * D

    return sigma