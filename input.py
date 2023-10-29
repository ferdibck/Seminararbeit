import model
import plotter
import visualization

""" 
Inputvariablen:
▪️ x, y; Größe des Gitters
▪️ num_walkers; Anzahl an Walkern
▪️ num_steps; Anzahl an Schritten bzw. Zeitpunkten
▪️ num_sims; Anzahl an versch. Simulationen
▪️ Temp; Temparatur
▪️ p_tunneling; Tunnelwahrscheinlichkeit (s. Arbeit)
"""

x = 250
y = 250
num_walkers = 500
num_steps = 200
num_sims = 5
Temp = 293
p_tunneling = 0.05

#model = model.Simulation(x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling)

#dfs = model.run_dir_simulations()

#plotter.plot_dfs(dfs)

lattice = model.Lattice(20, 20)
lattice.percolation_config(0.7)
#visualization.plot_lattice(lattice)

walkermanager = model.Walkermanager(50, 50, lattice, 0.1)
walkermanager.directed_random_walk()

visualization.animate_random_walk(walkermanager)