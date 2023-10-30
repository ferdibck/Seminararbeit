import pandas as pd
import matplotlib.pyplot as plt

def plot_dfs(dfs):
    plt.clf()
    colors = ["b", "g", "r", "c", "m", "y", "k"] 
    color_index = 0

    for i, df in enumerate(dfs):
        xvalues = df.iloc[:, 0]
        yvalues = df.iloc[:, 1]

        plt.plot(xvalues, yvalues, label=f"Simulation{i+1}", color=colors[color_index])
        
        color_index = (color_index + 1) % len(colors)
    
    plt.xlabel("p")
    plt.ylabel("Leitfähigkeit (σ)")
    plt.grid(linestyle = ":")
    plt.legend()
    plt.savefig("simulation.png", dpi = 300)
    #plt.show()

def save_dfs(dfs):
    for i, df in enumerate(dfs):
        df.to_csv(f"simulation3_{i+1}", index = False)