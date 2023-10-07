import numpy as np
import random
import matplotlib.pyplot as plt

class walker:
  vertex = None
  time_at_step = []
  pos_at_step = []

  def __init__(self):
    self.vertex = None
    self.time_at_step = []
    self.pos_at_step = []

  def assign_to_vertex(self, v):
    self.vertex = v
    v.set_has_walker(True)
    self.time_at_step.append(0)
    self.pos_at_step.append(v.get_Gamma())

  def update(self, v, t):
    self.vertex.set_has_walker(False)
    self.vertex = v
    v.set_has_walker(True)
    self.time_at_step.append(t)
    self.pos_at_step.append(v.get_Gamma())

  def move(self, t):
    neighbours = self.vertex.get_edges()
    valid_neighbours = [n for n in neighbours if not n.get_has_walker()]

    if valid_neighbours != []:
      new_vertex = random.choice(valid_neighbours)
      self.update(new_vertex, t)

  def get_pos_at_step(self):
    return self.pos_at_step
  
  def get_time_at_step(self):
    return self.time_at_step

class vertex:
  omega = None
  Gamma = (None, None)
  neighbours = [None, None, None, None] # N O S W

  has_walker = False

  def __init__(self):
    self.omega = None
    self.Gamma = (None, None)
    self.neighbours = [None, None, None, None]
    self.has_walker = False

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
    edges = [n for n in neighbors if (n is not None and n.get_omega() == 1 and self.omega == 1)]
    return edges
  
  def set_has_walker(self, w):
    self.has_walker = w

  def get_has_walker(self):
    return self.has_walker
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

  def random_walk(self, t):
    V = self.V

    walker_list = []

    for yi in range(len(V[0])):
      walker_obj = walker()
      walker_obj.assign_to_vertex(V[0][yi])
      walker_list.append(walker_obj)

    for ti in range(t):
      random.shuffle(walker_list)

      for w in walker_list:
        w.move(ti)
      
    return walker_list
  
  def visualize_random_walk(self, t):
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

    colors = ["blue", "yellow", "orange", "green", "cyan", "magenta"]

    walker_list = self.random_walk(t)

    for i, w in enumerate(walker_list):
      c = colors[i % 6]

      values = w.get_pos_at_step()
      xvalues, yvalues = zip(*values)

      plt.plot(xvalues, yvalues, "x", color=c, markersize=15, label=f'Walker {i+1}',alpha = 0.7)
      plt.plot(xvalues, yvalues, "-", color=c, linewidth=2, alpha = 0.7)

    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')
      
    plt.xticks(range(0, len(V[0])), fontsize=12)
    plt.yticks(range(0, len(V)), fontsize=12)
    plt.grid(True)
    plt.show()

  def calc_D(self, t):
    walker_list = self.random_walk(t)

    sum_of_dists = 0

    for w in walker_list:
      x0, y0 = w.get_pos_at_step()[0]
      xt, yt = w.get_pos_at_step()[-1]

      dx = xt - x0
      dy = yt - y0

      dist = np.sqrt(dx**2 + dy**2)
      
      sum_of_dists += dist

    avg_dist = sum_of_dists/len(walker_list)
    
    D = avg_dist**2/(2*2*t)

    return D

    """
    time_intervals_sum = 0
    squared_step_size = 0
    n = 0

    for w in walker_list:
      time = w.get_time_at_step()

      values = w.get_pos_at_step()
      xvalues, yvalues = zip(*values)

      for i in range(1,len(time)):
        time[i] = time[i] - time[i-1]
        time_intervals_sum += time[i]

      for j in range(1,len(xvalues)):
        n += len(xvalues)
        dx = xvalues[j] - xvalues[j-1]
        dy = yvalues[j] - yvalues[j-1]
        squared_step_size += dx**2 + dy**2

    if time_intervals_sum == 0:
      return 0
    
    avg_time_interval = time_intervals_sum/t
    avg_squared_step_size = squared_step_size/t

    D = avg_squared_step_size/avg_time_interval
    
    return D
    """
  
  def calc_sigma(self, t, T):
    V = self.V

    n = len(V[0])
    q = 1.6 * 10**(-19)
    kb = 1.38 * 10**(-23)
    D = self.calc_D(t)

    sigma = n* (q**2 / (kb*T))*D
    print(sigma)
    return sigma

  def visualize(self):
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

# Define a range of p values to test
p_values = np.linspace(0.0, 1, 20)  # Adjust the range as needed

# Initialize an empty list to store sigma values
sigma_values = []

# Loop through different p values and calculate sigma
for p in p_values:
    l = lattice(250, 250, p)
    sigma = l.calc_sigma(2500, 273)
    sigma_values.append(sigma)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(p_values, sigma_values, marker='o', linestyle='-')
plt.xlabel('p')
plt.ylabel('Sigma (σ)')
plt.title('Sigma vs. p')
plt.grid(True)
plt.show()