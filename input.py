import model

""" 
Inputvariablen:
▪️ x, y; Größe des Gitters
▪️ num_walkers; Anzahl an Walkern
▪️ num_steps; Anzahl an Schritten bzw. Zeitpunkten
▪️ num_sims; Anzahl an versch. Simulationen
▪️ Temp; Temparatur
▪️ p_tunneling; Tunnelwahrscheinlichkeit (s. Arbeit)
"""

x = 100
y = 100
num_walkers = 200
num_steps = 20
num_sims = 1
Temp = 293
p_tunneling = 0.1

model = model.Simulation(x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling)

model.run_simulation()