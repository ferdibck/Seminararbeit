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
y = x
num_walkers = x * 4
num_steps = x * 4
num_sims = 3
Temp = 293
p_tunneling = 0.05

model = model.Simulation(x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling)
dfs = model.run_dir_simulations()
plotter.save_dfs(dfs)
plotter.plot_dfs(dfs)
