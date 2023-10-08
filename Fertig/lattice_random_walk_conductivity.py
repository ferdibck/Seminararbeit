import numpy as np
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class walker:
  vertex = None
  time_at_step = []
  pos_at_t = []

  def __init__(self):
    self.vertex = None
    self.pos_at_t = []

  def assign_to_vertex(self, v):
    self.vertex = v
    v.set_has_walker(True)
    self.pos_at_t.append(v.get_Gamma())

  def update(self):
    self.pos_at_t.append(self.vertex.get_Gamma())

  def move(self):
    neighbours = self.vertex.get_edges()
    valid_neighbours = [n for n in neighbours if not n.get_has_walker()]

    if valid_neighbours != []:
      new_vertex = random.choice(valid_neighbours)
      self.vertex.set_has_walker(False)
      self.vertex = new_vertex
      new_vertex.set_has_walker(True)

    self.update()

  def get_pos_at_t(self):
    return self.pos_at_t

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
  x = 0
  y = 0

  def __init__(self, x, y, p):
    probabilities = [p, 1-p]

    self.x = x
    self.y = y

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

  def random_walk(self, t, n):
    V = self.V
    x = len(V)
    y = len(V[0])

    walker_list = []

    for _ in range(n):
      xrand = random.randint(0, x-1)
      yrand = random.randint(0, y-1)

      if not V[xrand][yrand].get_has_walker():
        walker_obj = walker()
        walker_obj.assign_to_vertex(V[xrand][yrand])
        walker_list.append(walker_obj)

    for _ in range(t):
      random.shuffle(walker_list)

      for w in walker_list:
        w.move()

    return walker_list

  def calc_D(self, walker_list):
    sum_of_dists = 0

    t = len(walker_list[0].get_pos_at_t())-1

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
  
  def calc_sigma(self, walker_list, T, t):
    V = self.V

    n = len(V[0])/(self.x * self.y)
    q = 1.6 * 10**(-19)
    kb = 1.38 * 10**(-23)
    D = self.calc_D(walker_list, t)

    sigma = n*(q**2 / (kb*T))*D
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

    plt.xticks(range(0, len(V[0])), fontsize=12)
    plt.yticks(range(0, len(V)), fontsize=12)
    plt.grid(True)
    plt.show()

  def visualize_random_walk(self, walker_list):
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

    for i, w in enumerate(walker_list):
      c = colors[i % 6]

      values = w.get_pos_at_t()
      xvalues, yvalues = zip(*values)

      plt.plot(xvalues, yvalues, "o", color=c, markersize=15, label=f'Walker {i+1}',alpha = 0.4)
      plt.plot(xvalues, yvalues, "-", color=c, linewidth=2, alpha = 0.4)

    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')
      
    plt.xticks(range(0, len(V[0])), fontsize=12)
    plt.yticks(range(0, len(V)), fontsize=12)
    plt.grid(True)
    plt.show()

  def animate_random_walk(self, walker_list):
    V = self.V

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

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
    lines = []

    for i, w in enumerate(walker_list):
        c = colors[i % 6]
        values = w.get_pos_at_t()
        xvalues, yvalues = zip(*values)
        line, = plt.plot([], [], "o", color=c, markersize=15, label=f'Walker {i+1}', alpha=0.4)
        lines.append(line)

    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')

    def update(frame):
        for i, w in enumerate(walker_list):
            values = w.get_pos_at_t()[:frame+1]
            xvalues, yvalues = zip(*values)
            lines[i].set_data(xvalues, yvalues)
        plt.title(f't={frame}')
        return lines

    t = len(walker_list[0].get_pos_at_t())
    ani = FuncAnimation(fig, update, frames=t, interval= 1000, blit=True)
    ani.save("walk.gif", writer='pillow')
      
    plt.xticks(range(0, len(V[0])), fontsize=12)
    plt.yticks(range(0, len(V)), fontsize=12)
    plt.grid(True)
    plt.show()