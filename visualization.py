import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_lattice(lattice):
  V = lattice.V

  fig, ax = plt.subplots()
  ax.set_aspect('equal')

  # Knoten
  for xi in range(lattice.x):
    for yi in range(lattice.y):

      # Knoten
      if V[xi][yi].omega == 1:
        ax.plot(xi, yi, "o", markersize=5, color="red")
      else:
        ax.plot(xi, yi, "o", markersize=5, color="black")

      # Kanten
      if xi > 0 and V[xi][yi].omega == 1 and V[xi-1][yi].omega == 1:
        ax.plot([xi, xi - 1], [yi, yi], color="red")
      if yi > 0 and V[xi][yi].omega == 1 and V[xi][yi-1].omega == 1:
        ax.plot([xi, xi], [yi, yi - 1], color="red")

  plt.xticks(range(0, len(V[0])), fontsize=12)
  plt.yticks(range(0, len(V)), fontsize=12)
  plt.grid(True)
  plt.show()

def animate_random_walk(walkermanager):
    V = walkermanager.lattice.V
    walker_list = walkermanager.walkers

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.set_aspect('equal')

    for xi in range(len(V)):
      for yi in range(len(V[0])):

        # Knoten
        if V[xi][yi].omega == 1:
          ax.plot(xi, yi, "o", markersize=5, color="red")
        else:
          ax.plot(xi, yi, "o", markersize=5, color="black")

        # Kanten
        if xi > 0 and V[xi][yi].omega == 1 and V[xi-1][yi].omega == 1:
          ax.plot([xi, xi - 1], [yi, yi], color="red")
        if yi > 0 and V[xi][yi].omega == 1 and V[xi][yi-1].omega == 1:
          ax.plot([xi, xi], [yi, yi - 1], color="red")

    colors = ["blue", "yellow", "orange", "green", "cyan", "magenta", "red", "purple", "pink", "brown", "gray"]
    lines = []

    for i, w in enumerate(walker_list):
      c = colors[i % 6]
      values = w.pos_at_t
      xvalues, yvalues = zip(*values)
      line, = plt.plot([], [], "o", color=c, markersize=15, label=f'Walker {i+1}', alpha=0.4)
      lines.append(line)

    ax.legend(fontsize=12, bbox_to_anchor=(1.05, 1), loc='upper left')

    def update(frame):
      for i, w in enumerate(walker_list):
        values = w.pos_at_t[frame]
        xvalues, yvalues = values
        lines[i].set_data(xvalues, yvalues)
      plt.title(f't={frame}')
      return lines

    t = walkermanager.t_max
    ani = FuncAnimation(fig, update, frames=t, interval= 1000, blit=True)
    ani.save("test.gif", writer='pillow', dpi = 300)
      
    plt.xticks(range(0, len(V[0])), fontsize=12)
    plt.yticks(range(0, len(V)), fontsize=12)
    plt.grid(True)
    plt.show()