import pandas as pd
import matplotlib.pyplot as plt

def plot_csv(files, x, y, name):
    colors = ["b", "g", "r", "c", "m", "y", "k"] 
    color_index = 0

    for file in files:
        df = pd.read_csv(file)

        xvalues = df.iloc[:, 0]
        yvalues = df.iloc[:, 1]

        plt.plot(xvalues, yvalues, label=file, color=colors[color_index])
        
        color_index = (color_index + 1) % len(colors)

    plt.xlabel(x)
    plt.ylabel(y)
    plt.grid(linestyle = ":")
    plt.legend()
    plt.savefig(name, dpi = 300)
    plt.show()

csv = "Simulationen\simulation1_1.csv"
csv2 = "Simulationen\simulation1_2.csv"
csv3 = "Simulationen\simulation1_3.csv"

files = [csv, csv2, csv3]

plot_csv(files, "p", "Leitfähigkeit (σ)", "simulation1.png")