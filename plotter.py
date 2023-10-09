import pandas as pd
import matplotlib.pyplot as plt

def plot_csv(files, x, y):
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
    plt.legend()
    plt.show()

csv = "test.csv"
csv2 = "test2.csv"

files = [csv, csv2]

plot_csv(files, "p", "Sigma (σ)")