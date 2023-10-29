import pandas as pd
import matplotlib.pyplot as plt

def plot_dfs(dfs):
    colors = ["b", "g", "r", "c", "m", "y", "k"] 
    color_index = 0

    for i, df in enumerate(dfs):
        xvalues = df.iloc[:, 0]
        yvalues = df.iloc[:, 1]

        plt.plot(xvalues, yvalues, label=f"Simulation2_{i+1}", color=colors[color_index])
        
        color_index = (color_index + 1) % len(colors)
    
    plt.xlabel("p")
    plt.ylabel("Leitfähigkeit (σ)")
    plt.grid(linestyle = ":")
    plt.legend()
    plt.save("simulation2.png")
    plt.show()

def save_dfs(dfs):
    for i, df in enumerate(dfs):
        df.to_csv(f"simulation2_{i+1}", index = False)