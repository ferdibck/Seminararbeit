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
num_walkers = 20
num_steps = 200
num_sims = 3
Temp = 293
p_tunneling = 0.05

model = model.Simulation(x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling)

model.run_simulation()