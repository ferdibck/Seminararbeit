# Änderungen am Programm

## Beispiel.txt

In "Beispiel.txt" (s. "Files 4 Trinket" und repl.it) sind andere Eingabebeispiele gezeigt.

## (Gerichteter) Random Walk

Der gerichtete Random Walk wird nahezu identisch zum Random Walk aufgerufen. Eine Leitfähigkeitssimulation mit dem gerichteten Random Walk wird bspw. so aufgerufen,

"
model = model.Simulation(x, y, num_walkers, num_steps, num_sims, Temp, p_tunneling)
dfs = model.run_dir_simulations()
plotter.save_dfs(dfs)
plotter.plot_dfs(dfs)
"

Der Prefix "dir" steht für directed.