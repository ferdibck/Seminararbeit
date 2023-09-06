import matplotlib.pyplot as plt
import numpy as np

def V(x, a):
    if 0 <= x <= a:
        return 0
    else:
        return 100
    
def plot_topf(a):
    x = np.linspace(-10, a+10, 1000)

    y = [V(xi, a) for xi in x]

    #Plotten
    plt.plot(x, y, color = "blue", alpha=1.00)
    plt.fill_between(x, y, 0, color = "blue", alpha = 0.1)

    #Visuell
    plt.xlabel("x", fontsize = 15)
    plt.ylabel("V(x)", fontsize = 15)
    plt.title("Unendlich hoher Potentialtopf", fontsize = 15)
    plt.xlim(-10, a+10)
    plt.ylim(-1, 10)
    plt.yticks([0])

    ax = plt.subplot()
    ax.spines[["right", "top"]].set_visible(False)
    ax.set_xticks([0, a])
    ax.set_xticklabels(["0", "a"]) 

    plt.show()

plot_topf(20)